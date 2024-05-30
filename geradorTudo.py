import random

def generate_sql(start, end): # gera pacientes
    for i in range(start, end):
        ssn = f"{50000000001 + i:11d}"
        nif = f"{600000001 + i:09d}"
        nome = f"Pa{i+1}"
        telefone = f"{960000001 + i:09d}"
        morada = f"Avenida{i+1} 1 1ºesq 8000-000 Lisboa"
        dia_nasc = '2000-01-01'
        print(f"('{ssn}', '{nif}', '{nome}', '{telefone}', '{morada}', '{dia_nasc}'),")

#generate_sql(0, 1000)
#generate_sql(1000, 2000)
#generate_sql(2000, 3000)
#generate_sql(3000, 4000)
#generate_sql(4000, 5000)

def generate_consultas1(num_pacientes): #gera consultas
    clinicas = ['Clinica Santa Marta', 'Clinica dos Platanos', 'Clinica Sao Jose', 'Clinica Solaia', 'Clinica Sao Joao']
    #codigo_sns = 100000002640  # Inicialização do código SNS
    ssn =  50000004800
    i = 0
    j = 4800
    for clinica in clinicas:
        consultas_agendadas = set()
        for _ in range(24):  # 24 consultas por clínica
            # Geração aleatória do ssn e nif para cada paciente
            ssn += 1
            nif = f"{200000001 + (i // 2):09d}"
            i += 1
            
            hour = random.choice([8, 9, 10, 11, 12, 14, 15, 16, 17, 18])
            minute = random.choice([0, 30])
            formatted_time = f"{hour:02d}:{minute:02d}"
            
            # Adicionar este horário às consultas agendadas
            consultas_agendadas.add(formatted_time)
            j += 1
            # Incrementar o código SNS
            #codigo_sns += 1
            
            # Consulta no formato SQL
            consulta = f"({j}, '{ssn}', '{nif}', '{clinica}', '{'2024-12-02'}', '{formatted_time}', {None}),"
            
            print(consulta)

def generate_consultas2(num_pacientes): #gera consultas
    clinicas = ['Clinica Santa Marta', 'Clinica dos Platanos', 'Clinica Sao Jose', 'Clinica Solaia', 'Clinica Sao Joao']
    #codigo_sns = 100000002760  # Inicialização do código SNS
    ssn =  50000004920
    i = 0
    j = 4920
    for clinica in clinicas:
        consultas_agendadas = set()
        for _ in range(24):  # 24 consultas por clínica
            # Geração aleatória do ssn e nif para cada paciente
            ssn += 1
            nif = f"{200000001 + (i // 2):09d}"
            i += 1
            
            hour = random.choice([8, 9, 10, 11, 12, 14, 15, 16, 17, 18])
            minute = random.choice([0, 30])
            formatted_time = f"{hour:02d}:{minute:02d}"

            
            # Adicionar este horário às consultas agendadas
            consultas_agendadas.add(formatted_time)
            j += 1
            # Incrementar o código SNS
            #codigo_sns += 1
            
            # Consulta no formato SQL
            consulta = f"({j}, '{ssn}', '{nif}', '{clinica}', '{'2024-12-03'}', '{formatted_time}', {None}),"
            
            print(consulta)

def generate_consultas3(num_pacientes): #gera consultas
    clinicas = ['Clinica Santa Marta', 'Clinica dos Platanos', 'Clinica Sao Jose', 'Clinica Solaia', 'Clinica Sao Joao']
    #codigo_sns = 100000002880  # Inicialização do código SNS
    ssn =  50000004080
    i = 0
    j = 4080
    for clinica in clinicas:
        consultas_agendadas = set()
        for _ in range(24):  # 24 consultas por clínica
            # Geração aleatória do ssn e nif para cada paciente
            ssn += 1
            nif = f"{200000001 + (i // 2):09d}"
            i += 1
            
            hour = random.choice([8, 9, 10, 11, 12, 14, 15, 16, 17, 18])
            minute = random.choice([0, 30])
            formatted_time = f"{hour:02d}:{minute:02d}"


            # Adicionar este horário às consultas agendadas
            consultas_agendadas.add(formatted_time)
            j += 1
            # Incrementar o código SNS
            #codigo_sns += 1
            
            # Consulta no formato SQL
            consulta = f"({j}, '{ssn}', '{nif}', '{clinica}', '{'2024-10-04'}', '{formatted_time}', {None}),"
            
            print(consulta)

def generate_consultas4(num_pacientes): #gera consultas
    clinicas = ['Clinica Santa Marta', 'Clinica dos Platanos', 'Clinica Sao Jose', 'Clinica Solaia', 'Clinica Sao Joao']
    #codigo_sns = 100000002280  # Inicialização do código SNS
    ssn =  50000004200
    i = 0
    j = 4200
    for clinica in clinicas:
        consultas_agendadas = set()
        for _ in range(24):  # 24 consultas por clínica
            # Geração aleatória do ssn e nif para cada paciente
            ssn += 1
            nif = f"{200000001 + (i // 2):09d}"
            i += 1
            
            hour = random.choice([8, 9, 10, 11, 12, 14, 15, 16, 17, 18])
            minute = random.choice([0, 30])
            formatted_time = f"{hour:02d}:{minute:02d}"

                
            # Adicionar este horário às consultas agendadas
            consultas_agendadas.add(formatted_time)
            j += 1
            # Incrementar o código SNS
            #codigo_sns += 1
            
            # Consulta no formato SQL
            consulta = f"({j}, '{ssn}', '{nif}', '{clinica}', '{'2024-11-04'}', '{formatted_time}', {None}),"
            
            print(consulta)

def generate_consultas5(num_pacientes): #gera consultas
    clinicas = ['Clinica Santa Marta', 'Clinica dos Platanos', 'Clinica Sao Jose', 'Clinica Solaia', 'Clinica Sao Joao']
    #codigo_sns = 100000003000  # Inicialização do código SNS
    ssn =  50000004320
    i = 0
    j = 4320
    for clinica in clinicas:
        consultas_agendadas = set()
        for _ in range(24):  # 24 consultas por clínica
            # Geração aleatória do ssn e nif para cada paciente
            ssn += 1
            nif = f"{200000001 + (i // 2):09d}"
            i += 1
            
            hour = random.choice([8, 9, 10, 11, 12, 14, 15, 16, 17, 18])
            minute = random.choice([0, 30])
            formatted_time = f"{hour:02d}:{minute:02d}"

            # Adicionar este horário às consultas agendadas
            consultas_agendadas.add(formatted_time)
            j += 1
            # Incrementar o código SNS
            #codigo_sns += 1
            
            # Consulta no formato SQL
            consulta = f"({j}, '{ssn}', '{nif}', '{clinica}', '{'2024-11-05'}', '{formatted_time}', {None}),"
            
            print(consulta)

def generate_consultas6(num_pacientes): #gera consultas
    clinicas = ['Clinica Santa Marta', 'Clinica dos Platanos', 'Clinica Sao Jose', 'Clinica Solaia', 'Clinica Sao Joao']
    #codigo_sns = 100000003120  # Inicialização do código SNS
    ssn =  50000004440
    i = 0
    j = 4440
    for clinica in clinicas:
        consultas_agendadas = set()
        for _ in range(24):  # 24 consultas por clínica
            # Geração aleatória do ssn e nif para cada paciente
            ssn += 1
            nif = f"{200000001 + (i // 2):09d}"
            i += 1
            
            hour = random.choice([8, 9, 10, 11, 12, 14, 15, 16, 17, 18])
            minute = random.choice([0, 30])
            formatted_time = f"{hour:02d}:{minute:02d}"

            # Adicionar este horário às consultas agendadas
            consultas_agendadas.add(formatted_time)
            j += 1
            # Incrementar o código SNS
            #codigo_sns += 1
            
            # Consulta no formato SQL
            consulta = f"({j}, '{ssn}', '{nif}', '{clinica}', '{'2024-11-06'}', '{formatted_time}', {None}),"
            
            print(consulta)

def generate_consultas7(num_pacientes): #gera consultas
    clinicas = ['Clinica Santa Marta', 'Clinica dos Platanos', 'Clinica Sao Jose', 'Clinica Solaia', 'Clinica Sao Joao']
    #codigo_sns = 1000000026840  # Inicialização do código SNS
    ssn =  50000004560
    i = 0
    j = 4560
    for clinica in clinicas:
        consultas_agendadas = set()
        for _ in range(24):  # 24 consultas por clínica
            # Geração aleatória do ssn e nif para cada paciente
            ssn += 1
            nif = f"{200000001 + (i // 2):09d}"
            i += 1
            
            hour = random.choice([8, 9, 10, 11, 12, 14, 15, 16, 17, 18])
            minute = random.choice([0, 30])
            formatted_time = f"{hour:02d}:{minute:02d}"

            # Adicionar este horário às consultas agendadas
            consultas_agendadas.add(formatted_time)
            j += 1
            # Incrementar o código SNS
            #codigo_sns += 1
            
            # Consulta no formato SQL
            consulta = f"({j}, '{ssn}', '{nif}', '{clinica}', '{'2024-11-07'}', '{formatted_time}', {None}),"
            
            print(consulta)

def generate_consultas8(num_pacientes): #gera consultas
    clinicas = ['Clinica Santa Marta', 'Clinica dos Platanos', 'Clinica Sao Jose', 'Clinica Solaia', 'Clinica Sao Joao']
    #codigo_sns = 100000002760  # Inicialização do código SNS
    ssn =  50000004680
    i = 0
    j = 4680
    for clinica in clinicas:
        consultas_agendadas = set()
        for _ in range(24):  # 24 consultas por clínica
            # Geração aleatória do ssn e nif para cada paciente
            ssn += 1
            nif = f"{200000001 + (i // 2):09d}"
            i += 1
            
            hour = random.choice([8, 9, 10, 11, 12, 14, 15, 16, 17, 18])
            minute = random.choice([0, 30])
            formatted_time = f"{hour:02d}:{minute:02d}"

            # Adicionar este horário às consultas agendadas
            consultas_agendadas.add(formatted_time)
            j += 1
            # Incrementar o código SNS
            #codigo_sns += 1
            
            # Consulta no formato SQL
            consulta = f"({j}, '{ssn}', '{nif}', '{clinica}', '{'2024-11-08'}', '{formatted_time}', {None}),"
            
            print(consulta)

def generate_consultas9(num_pacientes): #gera consultas
    clinicas = ['Clinica Santa Marta', 'Clinica dos Platanos', 'Clinica Sao Jose', 'Clinica Solaia', 'Clinica Sao Joao']
    codigo_sns = 100000002040  # Inicialização do código SNS
    ssn =  50000002040
    i = 0
    j = 2040
    for clinica in clinicas:
        consultas_agendadas = set()
        for _ in range(24):  # 24 consultas por clínica
            # Geração aleatória do ssn e nif para cada paciente
            ssn += 1
            nif = f"{200000001 + (i // 2):09d}"
            i += 1
            
            hour = random.choice([8, 9, 10, 11, 12, 14, 15, 16, 17, 18])
            minute = random.choice([0, 30])
            formatted_time = f"{hour:02d}:{minute:02d}"

            # Adicionar este horário às consultas agendadas
            consultas_agendadas.add(formatted_time)
            j += 1
            # Incrementar o código SNS
            codigo_sns += 1
            
            # Consulta no formato SQL
            consulta = f"({j}, '{ssn}', '{nif}', '{clinica}', '{'2023-02-09'}', '{formatted_time}', '{codigo_sns}'),"
            
            print(consulta)

def generate_consultas10(num_pacientes): #gera consultas
    clinicas = ['Clinica Santa Marta', 'Clinica dos Platanos', 'Clinica Sao Jose', 'Clinica Solaia', 'Clinica Sao Joao']
    codigo_sns = 100000000900  # Inicialização do código SNS
    ssn =  50000000900
    i = 0
    j = 900
    for clinica in clinicas:
        consultas_agendadas = set()
        for _ in range(24):  # 24 consultas por clínica
            # Geração aleatória do ssn e nif para cada paciente
            ssn += 1
            nif = f"{200000001 + (i // 2):09d}"
            i += 1
            
            hour = random.choice([8, 9, 10, 11, 12, 14, 15, 16, 17, 18])
            minute = random.choice([0, 30])
            formatted_time = f"{hour:02d}:{minute:02d}"

            # Adicionar este horário às consultas agendadas
            consultas_agendadas.add(formatted_time)
            j += 1
            # Incrementar o código SNS
            codigo_sns += 1
            
            # Consulta no formato SQL
            consulta = f"('{j}', '{ssn}', '{nif}', '{clinica}', '{'2023-02-10'}', '{formatted_time}', '{codigo_sns}'),"
            
            print(consulta)

# Gerar consultas para 5 clínicas
#generate_consultas1(20)
#generate_consultas2(20)
#generate_consultas3(20)
#generate_consultas4(20)
#generate_consultas5(20)
#generate_consultas6(20)
#generate_consultas7(20)
#generate_consultas8(20)
#generate_consultas9(20)
#generate_consultas10(20)


def generate_receita(start, end): # gera receitas
    medicamentos = ["Medicamento01", "Medicamento02", "Medicamento03", "Medicamento04", "Medicamento05", "Medicamento06", "Medicamento07", "Medicamento08", "Medicamento09", "Medicamento10", "Medicamento11", "Medicamento12", "Medicamento13", "Medicamento14", "Medicamento15", "Medicamento16", "Medicamento17", "Medicamento18", "Medicamento19", "Medicamento20", "Medicamento21", "Medicamento22", "Medicamento23", "Medicamento24", "Medicamento25", "Medicamento26", "Medicamento27", "Medicamento28", "Medicamento29", "Medicamento30"]
    quantidade = [1, 2, 3]
    codigo_sns = 100000001000  # Inicialização do código SNS
    for _ in range(start, end):
        codigo_sns += 1
        meds_usados = set()
        for _ in range(2):
            meds = random.choice(medicamentos)
            while meds in meds_usados:
                meds = random.choice(medicamentos)
            meds_usados.add(meds)
            quant = random.choice(quantidade)
            receita = f"('{codigo_sns:012d}', '{meds}', {quant}),"
            print(receita)

#generate_receita(0, 180)

sintomas = ['Sint01', 'Sint02', 'Sint03', 'Sint04', 'Sint05', 'Sint06', 'Sint07', 'Sint08', 'Sint09', 'Sint10', 'Sint11', 'Sint12', 'Sint13', 'Sint14', 'Sint15', 'Sint16', 'Sint17', 'Sint18', 'Sint19', 'Sint20', 'Sint21', 'Sint22', 'Sint23', 'Sint24', 'Sint25', 'Sint26', 'Sint27', 'Sint28', 'Sint29', 'Sint30', 'Sint31', 'Sint32', 'Sint33', 'Sint34', 'Sint35', 'Sint36', 'Sint37', 'Sint38', 'Sint39', 'Sint40', 'Sint41', 'Sint42', 'Sint43', 'Sint44', 'Sint45', 'Sint46', 'Sint47', 'Sint48', 'Sint49', 'Sint50']
metricas = ['Met01', 'Met02', 'Met03', 'Met04', 'Met05', 'Met06', 'Met07', 'Met08', 'Met09', 'Met10', 'Met11', 'Met12', 'Met13', 'Met14', 'Met15', 'Met16', 'Met17', 'Met18', 'Met19', 'Met20']
valores = [1.83, 2.34, 3.83, 4.04, 4.18, 6.90, 7.12, 8.14, 8.66, 8.82, 9.68, 10.90, 11.78, 12.65, 13.54, 14.20, 14.41, 14.76, 15.89, 17.63]

def generate_obs_par(start, end): # gera observações para consultas
    idee = 3120
    for _ in range (80):  
        idee += 1
        observp = set()
        observm = set()
        for _ in range(5):
            parametro = random.choice(sintomas)
            observacaop = f"{parametro}"
            while observacaop in observp:
                parametro = random.choice(sintomas)
                observacaop = f"{parametro}"
            observp.add(observacaop)

            observacaop = f"({idee}, '{parametro}', {None}),"
            print(observacaop)

        for _ in range(3):
            metrica = random.choice(metricas)
            observacaom = f"{metrica}"
            while observacaom in observm:
                metrica = random.choice(metricas)
                observacaom = f"{metrica}"
            observm.add(observacaom)

            valor = random.choice(valores)
            observacaom = f"({idee}, '{metrica}', {valor}),"
            print(observacaom)

#generate_obs_par(0, 1)