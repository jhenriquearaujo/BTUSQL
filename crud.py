
from sqlalchemy.orm import Session
from models import Funcao, Freelancer, Contratante, Agendamento, Pagamento, ValorDiariaHora

# ---------------- FUNCÃO ----------------
def criar_funcao(db: Session, descricao: str):
    nova = Funcao(DescricaoFuncao=descricao)
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

def listar_funcoes(db: Session):
    return db.query(Funcao).all()

def atualizar_funcao(db: Session, funcao_id: int, nova_desc: str):
    funcao = db.query(Funcao).filter(Funcao.FuncaoID == funcao_id).first()
    if funcao:
        funcao.DescricaoFuncao = nova_desc
        db.commit()
    return funcao

def deletar_funcao(db: Session, funcao_id: int):
    funcao = db.query(Funcao).filter(Funcao.FuncaoID == funcao_id).first()
    if funcao:
        db.delete(funcao)
        db.commit()

# ---------------- FREELANCER ----------------
def criar_freelancer(db: Session, cpf, nome, telefone, funcao_id, disponibilidade):
    novo = Freelancer(CPF=cpf, Nome=nome, Telefone=telefone, FuncaoID=funcao_id, Disponibilidade=disponibilidade)
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

def listar_freelancers(db: Session):
    return db.query(Freelancer).all()

def atualizar_freelancer_nome(db: Session, cpf: str, novo_nome: str):
    freelancer = db.query(Freelancer).filter(Freelancer.CPF == cpf).first()
    if freelancer:
        freelancer.Nome = novo_nome
        db.commit()
    return freelancer

def deletar_freelancer(db: Session, cpf: str):
    freelancer = db.query(Freelancer).filter(Freelancer.CPF == cpf).first()
    if freelancer:
        db.delete(freelancer)
        db.commit()

# ---------------- CONTRATANTE ----------------
def criar_contratante(db: Session, cnpj, nome_estab, telefone, endereco, responsavel, tipo):
    novo = Contratante(CNPJ=cnpj, NomeEstabelecimento=nome_estab, Telefone=telefone,
                       Endereco=endereco, NomeResponsavel=responsavel, TipoEstabelecimento=tipo)
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

def listar_contratantes(db: Session):
    return db.query(Contratante).all()

def atualizar_contratante_telefone(db: Session, cnpj: str, novo_tel: str):
    c = db.query(Contratante).filter(Contratante.CNPJ == cnpj).first()
    if c:
        c.Telefone = novo_tel
        db.commit()
    return c

def deletar_contratante(db: Session, cnpj: str):
    c = db.query(Contratante).filter(Contratante.CNPJ == cnpj).first()
    if c:
        db.delete(c)
        db.commit()

# ---------------- AGENDAMENTO ----------------
def criar_agendamento(db: Session, freelancer_cpf, contratante_cnpj, funcao_id, data, hora_inicio, hora_fim):
    novo = Agendamento(CPF=freelancer_cpf, CNPJ=contratante_cnpj,
                       FuncaoID=funcao_id, Data=data, HoraInicio=hora_inicio, HoraFim=hora_fim)
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

def listar_agendamentos(db: Session):
    return db.query(Agendamento).all()

def deletar_agendamento(db: Session, agendamento_id: int):
    ag = db.query(Agendamento).filter(Agendamento.AgendamentoID == agendamento_id).first()
    if ag:
        db.delete(ag)
        db.commit()

# ---------------- PAGAMENTO ----------------
def criar_pagamento(db: Session, contratante_cnpj, freelancer_cpf, funcao_id, valor_id, valor, data_pagamento, modalidade, metodo):
    novo = Pagamento(CNPJ=contratante_cnpj, CPF=freelancer_cpf, FuncaoID=funcao_id, ValorID=valor_id, DataPagamento=data_pagamento, Modalidade=modalidade, MetodoPagamento=metodo, ValorCalculado=valor)
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

def listar_pagamentos(db: Session):
    return db.query(Pagamento).all()

def deletar_pagamento(db: Session, pagamento_id: int):
    pag = db.query(Pagamento).filter(Pagamento.PagamentoID == pagamento_id).first()
    if pag:
        db.delete(pag)
        db.commit()

# ---------------- VALOR DIÁRIA/HORA ----------------
def criar_valor_diaria_hora(db: Session, funcao_id, tipo_pagamento, valor):
    novo = ValorDiariaHora(FuncaoID=funcao_id, Tipo=tipo_pagamento, Valor=valor)
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

def listar_valores_diaria_hora(db: Session):
    return db.query(ValorDiariaHora).all()

def deletar_valor_diaria_hora(db: Session, id_valor: int):
    valor = db.query(ValorDiariaHora).filter(ValorDiariaHora.ValorID == id_valor).first()
    if valor:
        db.delete(valor)
        db.commit()

def freelancers_por_funcao(db: Session):
    resultados = db.query(Funcao.DescricaoFuncao, Freelancer.Nome) \
                   .join(Freelancer, Funcao.FuncaoID == Freelancer.FuncaoID) \
                   .order_by(Funcao.DescricaoFuncao) \
                   .all()
    return resultados