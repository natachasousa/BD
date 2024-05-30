#!/usr/bin/python3
import os
from logging.config import dictConfig

import psycopg
from datetime import datetime
from flask import Flask, jsonify, request
from psycopg.rows import namedtuple_row

# Use the DATABASE_URL environment variable if it exists, otherwise use the default.
DATABASE_URL = os.environ.get("DATABASE_URL", "postgres://postgres:postgres@postgres/postgres")

dictConfig(
    {
        "version": 1,
        "formatters": {
            "default": {
                "format": "[%(asctime)s] %(levelname)s in %(module)s:%(lineno)s - %(funcName)20s(): %(message)s",
            }
        },
        "handlers": {
            "wsgi": {
                "class": "logging.StreamHandler",
                "stream": "ext://flask.logging.wsgi_errors_stream",
                "formatter": "default",
            }
        },
        "root": {"level": "INFO", "handlers": ["wsgi"]},
    }
)

app = Flask(__name__)
app.config.from_prefixed_env()
log = app.logger


@app.route("/", methods=("GET",))
def list_clinics():
    with psycopg.connect(conninfo=DATABASE_URL, autocommit=True) as conn:
        with conn.cursor(row_factory=namedtuple_row) as cur:
            clinics = cur.execute(
                """SELECT nome, morada FROM clinica;""",
                {},
            ).fetchall()
    return jsonify(clinics)


@app.route("/c/<clinica>/", methods=("GET",))
def list_specialties(clinica):
    with psycopg.connect(conninfo=DATABASE_URL, autocommit=True) as conn:
        with conn.cursor(row_factory=namedtuple_row) as cur:
            specialties = cur.execute(
                """
                SELECT DISTINCT m.especialidade
                FROM medico m
                JOIN trabalha t ON m.nif = t.nif
                WHERE t.nome = %(clinica)s;
                """,
                {"clinica": clinica},
            ).fetchall()
    return jsonify(specialties)


@app.route("/c/<clinica>/<especialidade>/", methods=("GET",))
def list_doctors_and_availability(clinica, especialidade):
    with psycopg.connect(conninfo=DATABASE_URL, autocommit=True) as conn:
        with conn.cursor(row_factory=namedtuple_row) as cur:
            # Get all doctors of the specified specialty working at the specified clinic
            cur.execute(
                """
                SELECT DISTINCT m.nif, m.nome
                FROM medico m
                JOIN trabalha t ON m.nif = t.nif
                WHERE m.especialidade = %s AND t.nome = %s
                """,
                (especialidade, clinica)
            )
            doctors = cur.fetchall()

            # Prepare a list to hold the final result
            result = []

            for doctor in doctors:
                # Get the next 3 available appointment slots for the current doctor
                cur.execute(
                    """
                    SELECT c.data, c.hora
                    FROM consulta c
                    WHERE c.nif = %s AND (c.data > CURRENT_DATE OR (c.data = CURRENT_DATE AND c.hora > CURRENT_TIME))
                    ORDER BY c.data, c.hora
                    LIMIT 3
                    """,
                    (doctor.nif,)
                )
                appointments = cur.fetchall()

                for appointment in appointments:
                    result.append({
                        "nome": doctor.nome,
                        "data": appointment.data.isoformat(),
                        "hora": appointment.hora.strftime('%H:%M:%S')
                    })
    if not result:
        return jsonify("Esta especialidade não se encontra nesta clínica.")
    
    return jsonify(result)



@app.route("/a/<clinica>/registar/", methods=("POST",))
def register_appointment(clinica):
    paciente = request.args.get("paciente")
    medico = request.args.get("medico")
    data = request.args.get("data")
    hora = request.args.get("hora")

    if not paciente or not medico or not data or not hora:
        return "Paciente, médico e data/hora são obrigatórios.", 400
    appointment_datetime = datetime.strptime(f"{data} {hora}", "%Y-%m-%d %H:%M:%S")
    if appointment_datetime <= datetime.now():
        return "A data/hora da consulta deve ser no futuro.", 400

    with psycopg.connect(conninfo=DATABASE_URL, autocommit=True) as conn:
        with conn.cursor() as cur:
            try:
                # Fetch the current maximum ID
                cur.execute("SELECT COALESCE(MAX(id), 0) FROM consulta")
                last_id = cur.fetchone()[0]
                new_id = last_id + 1

                cur.execute(
                    """
                    INSERT INTO consulta (id, ssn, nif, nome, data, hora, codigo_sns)
                    VALUES (%(id)s, %(paciente)s, %(medico)s, %(clinica)s, %(data)s, %(hora)s, NULL)
                    ON CONFLICT (nif, data, hora) DO NOTHING;
                    """,
                    {"id": new_id, "paciente": paciente, "medico": medico, "clinica": clinica, "data": data, "hora": hora},
                )
                if cur.rowcount == 0:
                    return "Conflito de agendamento: o médico já tem uma consulta marcada para essa data e hora.", 409

            except Exception as e:
                conn.rollback()
                return str(e), 400

    return "Consulta registada com sucesso.", 201


@app.route("/a/<clinica>/cancelar/", methods=("POST",))
def cancel_appointment(clinica):
    paciente = request.args.get("paciente")
    medico = request.args.get("medico")
    data = request.args.get("data")
    hora = request.args.get("hora")

    if not paciente or not medico or not data or not hora:
        return "Paciente, médico e data/hora são obrigatórios.", 400

    with psycopg.connect(conninfo=DATABASE_URL, autocommit=True) as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(
                    """
                    DELETE FROM consulta
                    WHERE ssn = %(paciente)s AND nif = %(medico)s AND nome = %(clinica)s AND data = %(data)s AND hora = %(hora)s;
                    """,
                    {"paciente": paciente, "medico": medico,"clinica": clinica ,"data": data, "hora": hora},
                )
            except Exception as e:
                conn.rollback()
                return str(e), 400
    return "Consulta cancelada com sucesso.", 200


if __name__ == "__main__":
    app.run()
