from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import date, time

from database import Base
from models import Funcao, Freelancer, Contratante, Agendamento, Pagamento, ValorDiariaHora
import crud

DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/btu"  # Edite conforme seu banco

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# Recria o banco (cuidado: apaga os dados)
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

# 1. Criar funções
crud.criar_funcao(session, "Garçom")
crud.criar_funcao(session, "Cozinheiro")

# 2. Criar contratante
crud.criar_contratante(session, "12345678000100", "Bar Central", "44990001122", "Rua A, 123", "Carlos Silva", "Bar")

# 3. Criar freelancer
crud.criar_freelancer(session, "11122233344", "João Pedro", "44991112233", 1, "Noturno")

# 4. Criar agendamento
agendamento = crud.criar_agendamento(
    session,
    freelancer_cpf="11122233344",
    contratante_cnpj="12345678000100",
    funcao_id=1,
    data=date.today(),
    hora_inicio=time(18, 0),
    hora_fim=time(23, 0)
)

# 5. Criar valor de diária
valor_diaria_hr = crud.criar_valor_diaria_hora(session, funcao_id=1, tipo_pagamento="DIARIA", valor=150.00)

# 6. Criar pagamento
crud.criar_pagamento(
    session,
    contratante_cnpj="12345678000100",
    freelancer_cpf="11122233344",
    funcao_id=1,
    valor_id=valor_diaria_hr.ValorID,
    valor=150.00,
    data_pagamento=date.today(),
    modalidade="uma",
    metodo="pix"
)

# 7. Consultar freelancers por função
print("Freelancers por função:")
for desc, nome in crud.freelancers_por_funcao(session):
    print(f"{desc} - {nome}")

# 8. Listar agendamentos
print("Agendamentos:")
for a in crud.listar_agendamentos(session):
    print(vars(a))
