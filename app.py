#!/usr/bin/python3
import os
from logging.config import dictConfig

import psycopg
from datetime import datetime
from flask import Flask, jsonify, request
from psycopg.rows import namedtuple_row

# Use the DATABASE_URL environment variable if it exists, otherwise use the default.
DATABASE_URL = os.environ.get("DATABASE_URL", "postgres://saude:1234@postgres/saude")

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
            doctors = cur.execute(
                """
                WITH future_appointments AS (
                    SELECT DISTINCT ON (c.nif, c.data, c.hora) c.nif, c.data, c.hora
                    FROM consulta c
                    JOIN medico m ON c.nif = m.nif
                    JOIN trabalha t ON m.nif = t.nif
                    WHERE m.especialidade = %(especialidade)s 
                    AND t.nome = %(clinica)s 
                    AND (c.data, c.hora) > (CURRENT_DATE, CURRENT_TIME)
                    ORDER BY c.data, c.hora
                    LIMIT 3
                )
                SELECT m.nome, fa.data, fa.hora
                FROM medico m
                JOIN trabalha t ON m.nif = t.nif
                JOIN future_appointments fa ON m.nif = fa.nif
                WHERE m.especialidade = %(especialidade)s 
                AND t.nome = %(clinica)s
                ORDER BY fa.data, fa.hora;
                """,
                {"clinica": clinica, "especialidade": especialidade},
            ).fetchall()
    return jsonify([
        {
            "nome": doctor.nome,
            "data": doctor.data.isoformat(),
            "hora": doctor.hora.strftime('%H:%M:%S')  # Converting time to string
        } for doctor in doctors
    ])



@app.route("/a/<clinica>/registar/", methods=("POST",))
def register_appointment(clinica):
    paciente = request.json.get("paciente")
    medico = request.json.get("medico")
    datahora = request.json.get("datahora")

    if not paciente or not medico or not datahora:
        return "Paciente, médico e data/hora são obrigatórios.", 400
    if datahora <= datetime.now():
        return "A data/hora da consulta deve ser no futuro.", 400

    data = datahora.date()
    hora = datahora.time()

    with psycopg.connect(conninfo=DATABASE_URL) as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(
                    """
                    INSERT INTO consulta (ssn, nif, data, hora, nome)
                    VALUES (%(paciente)s, %(medico)s, %(data)s, %(hora)s, %(clinica)s)
                    ON CONFLICT (nif, data, hora) DO NOTHING;
                    """,
                    {"paciente": paciente, "medico": medico, "data": data, "hora": hora, "clinica": clinica},
                )
                if cur.rowcount == 0:
                    return "Conflito de agendamento: o médico já tem uma consulta marcada para essa data e hora.", 409

                conn.commit()
            except Exception as e:
                conn.rollback()
                return str(e), 400

    return "Consulta registrada com sucesso.", 201


@app.route("/a/<clinica>/cancelar/", methods=("POST",))
def cancel_appointment(clinica):
    paciente = request.json.get("paciente")
    medico = request.json.get("medico")
    datahora = request.json.get("datahora")

    if not paciente or not medico or not datahora:
        return "Paciente, médico e data/hora são obrigatórios.", 400

    with psycopg.connect(conninfo=DATABASE_URL) as conn:
        with conn.cursor() as cur:
            try:
                cur.execute(
                    """
                    DELETE FROM consulta
                    WHERE paciente = %(paciente)s AND medico = %(medico)s AND datahora = %(datahora)s AND clinica = %(clinica)s;
                    """,
                    {"paciente": paciente, "medico": medico, "datahora": datahora, "clinica": clinica},
                )
                conn.commit()
            except Exception as e:
                conn.rollback()
                return str(e), 400
    return "Consulta cancelada com sucesso.", 200


if __name__ == "__main__":
    app.run()
