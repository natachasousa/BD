-- EXERCÍCIO 5

-- 1

WITH ortopedia_observacoes AS (
    SELECT
        id,
        ssn,
        nif,
        nome,
        data,
        chave,
        LAG(data) OVER (PARTITION BY ssn, chave ORDER BY data) AS prev_data
    FROM
        historial_paciente
    WHERE
        especialidade = 'ortopedia'
        AND tipo = 'observacao'
        AND valor IS NULL
),
intervalos AS (
    SELECT
        ssn,
        nome,
        chave,
        EXTRACT(EPOCH FROM (data - prev_data)) / 86400 AS dias_entre_observacoes
    FROM
        ortopedia_observacoes
    WHERE
        prev_data IS NOT NULL
),
max_intervalo AS (
    SELECT
        ssn,
        nome,
        MAX(dias_entre_observacoes) AS max_dias
    FROM
        intervalos
    GROUP BY
        ssn,
        nome
)
SELECT
    ssn,
    nome,
    max_dias
FROM
    max_intervalo
ORDER BY
    max_dias DESC
LIMIT 1;



-- 2

WITH cardiologia_receitas AS (
    SELECT
        ssn,
        chave AS medicamento,
        DATE_TRUNC('month', data) AS mes,
        COUNT(*) AS num_receitas
    FROM
        historial_paciente
    WHERE
        especialidade = 'Cardiologia'
        AND tipo = 'receita'
        AND data >= NOW() - INTERVAL '12 months'
    GROUP BY
        ssn,
        medicamento,
        mes
),
receitas_por_paciente AS (
    SELECT
        ssn,
        medicamento,
        COUNT(DISTINCT mes) AS meses_com_receita
    FROM
        cardiologia_receitas
    GROUP BY
        ssn,
        medicamento
),
medicamentos_continuos AS (
    SELECT
        medicamento
    FROM
        receitas_por_paciente
    WHERE
        meses_com_receita = 12
    GROUP BY
        medicamento
)
SELECT DISTINCT
    medicamento
FROM
    medicamentos_continuos;

-- 3
SELECT
    chave AS medicamento,
    SUM(valor::integer) AS quantidade_total
FROM
    historial_paciente
WHERE
    ano = 2023
    AND tipo = 'receita'
GROUP BY
    medicamento
ORDER BY
    quantidade_total DESC;

-- Por Localidade
SELECT
    localidade,
    chave AS medicamento,
    SUM(valor::integer) AS quantidade_total
FROM
    historial_paciente
WHERE
    ano = 2023
    AND tipo = 'receita'
GROUP BY
    localidade, medicamento
ORDER BY
    localidade, quantidade_total DESC;

-- Por Clínica dentro de Localidade
SELECT
    localidade,
    clinica,
    chave AS medicamento,
    SUM(valor::integer) AS quantidade_total
FROM
    historial_paciente
WHERE
    ano = 2023
    AND tipo = 'receita'
GROUP BY
    localidade, clinica, medicamento
ORDER BY
    localidade, clinica, quantidade_total DESC;

-- Por Mês
SELECT
    mes,
    chave AS medicamento,
    SUM(valor::integer) AS quantidade_total
FROM
    historial_paciente
WHERE
    ano = 2023
    AND tipo = 'receita'
GROUP BY
    mes, medicamento
ORDER BY
    mes, quantidade_total DESC;

-- Por Dia do Mês dentro de Mês
SELECT
    mes,
    dia_do_mes,
    chave AS medicamento,
    SUM(valor::integer) AS quantidade_total
FROM
    historial_paciente
WHERE
    ano = 2023
    AND tipo = 'receita'
GROUP BY
    mes, dia_do_mes, medicamento
ORDER BY
    mes, dia_do_mes, quantidade_total DESC;

-- Por Especialidade
SELECT
    especialidade,
    chave AS medicamento,
    SUM(valor::integer) AS quantidade_total
FROM
    historial_paciente
WHERE
    ano = 2023
    AND tipo = 'receita'
GROUP BY
    especialidade, medicamento
ORDER BY
    especialidade, quantidade_total DESC;

-- Por Nome do Médico dentro de Especialidade
SELECT
    especialidade,
    nome,
    chave AS medicamento,
    SUM(valor::integer) AS quantidade_total
FROM
    historial_paciente
WHERE
    ano = 2023
    AND tipo = 'receita'
GROUP BY
    especialidade, nome, medicamento
ORDER BY
    especialidade, nome, quantidade_total DESC;


-- 4

SELECT
    chave AS parametro,
    AVG(valor::numeric) AS valor_medio,
    STDDEV(valor::numeric) AS desvio_padrao
FROM
    historial_paciente
WHERE
    tipo = 'observacao'
    AND valor IS NOT NULL
GROUP BY
    parametro
ORDER BY
    parametro;


-- Por Especialidade
SELECT
    especialidade,
    chave AS parametro,
    AVG(valor::numeric) AS valor_medio,
    STDDEV(valor::numeric) AS desvio_padrao
FROM
    historial_paciente
WHERE
    tipo = 'observacao'
    AND valor IS NOT NULL
GROUP BY
    especialidade, parametro
ORDER BY
    especialidade, parametro;

-- Por Nome do Médico dentro de Especialidade
SELECT
    especialidade,
    nome AS medico,
    chave AS parametro,
    AVG(valor::numeric) AS valor_medio,
    STDDEV(valor::numeric) AS desvio_padrao
FROM
    historial_paciente
WHERE
    tipo = 'observacao'
    AND valor IS NOT NULL
GROUP BY
    especialidade, medico, parametro
ORDER BY
    especialidade, medico, parametro;

-- Por Clínica dentro de Especialidade e Nome do Médico
SELECT
    especialidade,
    nome AS medico,
    localidade,
    clinica,
    chave AS parametro,
    AVG(valor::numeric) AS valor_medio,
    STDDEV(valor::numeric) AS desvio_padrao
FROM
    historial_paciente
WHERE
    tipo = 'observacao'
    AND valor IS NOT NULL
GROUP BY
    especialidade, medico, localidade, clinica, parametro
ORDER BY
    especialidade, medico, localidade, clinica, parametro;
