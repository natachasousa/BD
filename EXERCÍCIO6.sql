-- EXERCÍCIO 6

-- 6.1

SELECT nome
FROM paciente
JOIN consulta USING (ssn)
JOIN observacao USING (id)
WHERE parametro = 'pressão diastólica'
AND valor >= 9;

-- corrigir parmetro para:

CREATE INDEX idx_observacao_param_valor ON observacao (parametro, valor);

/*
Este índice composto ajuda a acelerar a procura nas colunas: parametro e valor, 
particularmente útil para consultas que filtram por parametro e depois aplicam uma condição no valor.


Colunas parametro e valor: A consulta filtra os registos onde parametro é a 'pressão diastólica' e o valor é maior ou igual a 9.
Um índice composto em (parametro, valor) permite que a base de dados filtre rapidamente os registos relevantes.

Benefício: Este índice composto acelera as procuras pela combinação de parametro e valor,
 melhorando significativamente o tempo de resposta para consultas que aplicam condições em ambas as colunas
*/

-- melhorar a eficiência da junção entre consulta e observação 

CREATE INDEX idx_consulta_id ON consulta (id);

/*
Como id é usado para unir-se com a tabela observacao, um índice nesta coluna acelera a união.

Coluna id: Utilizada na união entre consulta e observacao. Um índice nesta coluna permite que a base de dados 
aceda rapidamente os registos da tabela observacao correspondentes a cada registo em consulta.

Benefício: Reduz o tempo necessário para realizar a união ao permitir procuras eficientes pela coluna id.

*/

-- juntar paciente e consulta

 CREATE INDEX idx_paciente_ssn ON paciente (ssn);

/*
Este índice acelera a união entre paciente e consulta com base na coluna ssn.

Coluna ssn: Utilizada na união entre paciente e consulta. Um índice nesta coluna permite que a base de dados
encontre rapidamente os registos correspondentes na tabela consulta.

Benefício: Acelera a operação de união, melhorando o desempenho geral da consulta.

*/

-- RESUMO:

/*
Índice idx_observacao_param_valor: Otimiza a operação de filtro nas colunas: parametro e valor, 
tornando a procura por observações específicas mais eficiente.

Índice idx_consulta_id: Acelera a união  entre consulta e observacao ao permitir acessos mais rápidos 
aos registos correspondentes na tabela observacao.

Índice idx_paciente_ssn: Acelera a união entre paciente e consulta ao permitir acessos mais rápidos
 aos registos correspondentes na tabela paciente.
*/


-- 6.2

SELECT especialidade, SUM(quantidade) AS qtd
 FROM medico
 JOIN consulta USING (nif)
 JOIN receita USING (codigo_ssn)
WHERE data BETWEEN ‘2023-01-01’ AND ‘2023-12-31’
 GROUP BY especialidade
 SORT BY qtd;

-- juntar consulta com a receita
CREATE INDEX idx_consulta_codigo_ssn ON consulta (codigo_ssn);

/*
 Como codigo_ssn é usado para unir com a tabela receita, um índice nesta coluna acelera a operação de união.

 Coluna codigo_ssn: Como codigo_ssn é usado para unir a tabela consulta com a tabela receita, um índice nesta coluna permite
  que a base de dados encontre rapidamente os registos correspondentes em receita durante a operação de união, 
  reduzindo o tempo necessário para a operação.
*/

-- juntar médico e consulta 
CREATE INDEX idx_medico_nif ON medico (nif);

/*
 Este índice acelera a união entre medico e consulta com base na coluna nif.

 Coluna nif: Este índice acelera a união entre as tabelas medico e consulta com base na coluna nif,
  que é a chave usada para unir as duas tabelas. 
  Com este índice, a base de dados pode localizar rapidamente os registos em consulta que correspondem a cada registo em medico.
*/

--  Este índice acelera a junção entre medico e consulta com base na coluna nif.
CREATE INDEX idx_receita_data_codigo_ssn ON receita (data, codigo_ssn);

/*
Este índice composto melhora o desempenho do filtro pela coluna data e otimiza a união pela coluna codigo_ssn.

Colunas data e codigo_ssn: Este índice composto melhora o desempenho do filtro pela coluna data,
  acelerando a seleção dos registos que correspondem ao intervalo de datas especificas.
  Além disso, a inclusão de codigo_ssn no índice otimiza a união entre receita e consulta,
  já que codigo_ssn é a chave usada para unir essas tabelas. 
  Este índice permite que a base de dados realize ambas as operações de forma mais eficiente.
*/

-- RESUMO 

/*
Índice idx_consulta_codigo_ssn: Acelera a união entre consulta e receita, 
permitindo acessos mais rápidos aos registos correspondentes na tabela receita.

Índice idx_medico_nif: Acelera a união entre medico e consulta, 
permitindo acessos mais rápidos aos registos correspondentes na tabela consulta.

Índice idx_receita_data_codigo_ssn: Otimiza a filtragem pela coluna data e melhora
 a eficiência da união entre receita e consulta, reduzindo o número de registos que precisam de ser varridos.
*/


