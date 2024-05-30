-- EXERCÍCIO 4

-- Supondo que estamos utilizando um banco de dados PostgreSQL

-- Criação da Vista Materializada
CREATE MATERIALIZED VIEW historial_paciente AS
SELECT 
    c.id AS id,
    p.ssn AS ssn,
    p.nif AS nif,
    p.nome AS nome,
    c.data AS data,
    EXTRACT(YEAR FROM c.data) AS ano,
    EXTRACT(MONTH FROM c.data) AS mes,
    EXTRACT(DAY FROM c.data) AS dia_do_mes,
    EXTRACT(DOW FROM c.data) AS dia_da_semana,
    p.morada AS localidade,
    m.especialidade AS especialidade,
    'observacao' AS tipo,
    o.parametro AS chave,
    o.valor AS valor
FROM 
    consulta c
JOIN 
    paciente p ON c.ssn = p.ssn
JOIN 
    medico m ON c.nif = m.nif
JOIN 
    observacao o ON c.id = o.id

UNION ALL

SELECT 
    c.id AS id,
    p.ssn AS ssn,
    p.nif AS nif,
    p.nome AS nome,
    c.data + c.hora AS data,
    EXTRACT(YEAR FROM (c.data + c.hora)) AS ano,
    EXTRACT(MONTH FROM (c.data + c.hora)) AS mes,
    EXTRACT(DAY FROM (c.data + c.hora)) AS dia_do_mes,
    EXTRACT(DOW FROM (c.data + c.hora)) AS dia_da_semana,
    p.morada AS localidade,
    m.especialidade AS especialidade,
    'receita' AS tipo,
    r.medicamento AS chave,
    r.quantidade AS valor
FROM 
    consulta c
JOIN 
    paciente p ON c.ssn = p.ssn
JOIN 
    medico m ON c.nif = m.nif
JOIN 
    receita r ON c.codigo_sns = r.codigo_sns;

-- Atualização da Vista Materializada (caso necessário, após inserções/atualizações nas tabelas de origem)
REFRESH MATERIALIZED VIEW historial_paciente;


CREATE MATERIALIZED VIEW historial_paciente AS
SELECT
    c.id,
    c.ssn,
    c.nif,
    c.nome,
    c.data,
    EXTRACT(YEAR FROM c.data) AS ano,
    EXTRACT(MONTH FROM c.data) AS mes,
    EXTRACT(DAY FROM c.data) AS dia_do_mes,
    SUBSTRING(cl.morada FROM '[0-9]+ (.+)') AS localidade,
    m.especialidade,
    'observacao' AS tipo,
    o.parametro AS chave,
    o.valor
FROM consulta c
JOIN clinica cl ON c.clinica_id = cl.id
JOIN medico m ON c.medico_id = m.id
LEFT JOIN observacao o ON c.id = o.consulta_id

UNION ALL

SELECT
    c.id,
    c.ssn,
    c.nif,
    c.nome,
    c.data,
    EXTRACT(YEAR FROM c.data) AS ano,
    EXTRACT(MONTH FROM c.data) AS mes,
    EXTRACT(DAY FROM c.data) AS dia_do_mes,
    SUBSTRING(cl.morada FROM '[0-9]+ (.+)') AS localidade,
    m.especialidade,
    'receita' AS tipo,
    r.medicamento AS chave,
    r.quantidade AS valor
FROM consulta c
JOIN clinica cl ON c.clinica_id = cl.id
JOIN medico m ON c.medico_id = m.id
LEFT JOIN receita r ON c.id = r.consulta_id