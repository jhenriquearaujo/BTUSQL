from sqlalchemy import Column, Integer, String, Date, Time, DECIMAL, ForeignKey, CHAR
from sqlalchemy.orm import relationship
from database import Base

class Funcao(Base):
    __tablename__ = 'funcao'
    FuncaoID = Column(Integer, primary_key=True)
    DescricaoFuncao = Column(String(100), nullable=False)
    freelancers = relationship("Freelancer", back_populates="funcao")
    agendamentos = relationship("Agendamento", back_populates="funcao")
    pagamentos = relationship("Pagamento", back_populates="funcao")
    valores = relationship("ValorDiariaHora", back_populates="funcao")

class Contratante(Base):
    __tablename__ = 'contratante'
    CNPJ = Column(String(18), primary_key=True)
    NomeEstabelecimento = Column(String(100))
    Telefone = Column(String(20))
    Endereco = Column(String(200))
    NomeResponsavel = Column(String(100))
    TipoEstabelecimento = Column(String(50))
    agendamentos = relationship("Agendamento", back_populates="contratante")
    pagamentos = relationship("Pagamento", back_populates="contratante")

class Freelancer(Base):
    __tablename__ = 'freelancer'
    CPF = Column(CHAR(11), primary_key=True)
    Nome = Column(String(100))
    Telefone = Column(String(20))
    FuncaoID = Column(Integer, ForeignKey('funcao.FuncaoID'))
    Disponibilidade = Column(String(50))
    funcao = relationship("Funcao", back_populates="freelancers")
    agendamentos = relationship("Agendamento", back_populates="freelancer")
    pagamentos = relationship("Pagamento", back_populates="freelancer")

class ValorDiariaHora(Base):
    __tablename__ = 'valor_diaria_hora'
    ValorID = Column(Integer, primary_key=True)
    FuncaoID = Column(Integer, ForeignKey('funcao.FuncaoID'))
    Tipo = Column(String(10))
    Valor = Column(DECIMAL(10,2))
    funcao = relationship("Funcao", back_populates="valores")
    pagamentos = relationship("Pagamento", back_populates="valor")

class Agendamento(Base):
    __tablename__ = 'agendamento'
    AgendamentoID = Column(Integer, primary_key=True)
    CNPJ = Column(String(18), ForeignKey('contratante.CNPJ'))
    CPF = Column(CHAR(11), ForeignKey('freelancer.CPF'))
    Data = Column(Date)
    HoraInicio = Column(Time)
    HoraFim = Column(Time)
    Modalidade = Column(String(10))
    FuncaoID = Column(Integer, ForeignKey('funcao.FuncaoID'))
    Status = Column(String(20))
    contratante = relationship("Contratante", back_populates="agendamentos")
    freelancer = relationship("Freelancer", back_populates="agendamentos")
    funcao = relationship("Funcao", back_populates="agendamentos")

class Pagamento(Base):
    __tablename__ = 'pagamento'
    PagamentoID = Column(Integer, primary_key=True)
    CNPJ = Column(String(18), ForeignKey('contratante.CNPJ'))
    CPF = Column(CHAR(11), ForeignKey('freelancer.CPF'))
    FuncaoID = Column(Integer, ForeignKey('funcao.FuncaoID'))
    ValorID = Column(Integer, ForeignKey('valor_diaria_hora.ValorID'))
    DataPagamento = Column(Date)
    Modalidade = Column(String(10))
    MetodoPagamento = Column(String(20))
    ValorCalculado = Column(DECIMAL(10,2))
    contratante = relationship("Contratante", back_populates="pagamentos")
    freelancer = relationship("Freelancer", back_populates="pagamentos")
    funcao = relationship("Funcao", back_populates="pagamentos")
    valor = relationship("ValorDiariaHora", back_populates="pagamentos")
