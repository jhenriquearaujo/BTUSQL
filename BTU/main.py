from datetime import date, time
from pprint import pprint

from database import Base, Session ,engine
from models import Funcao, Contratante, Freelancer, ValorDiariaHora, Agendamento, Pagamento

session = Session()

def reset_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

def insert_initial_data():
    session.add_all([
        Funcao(FuncaoID=1, DescricaoFuncao='Garcom'),
        Funcao(FuncaoID=2, DescricaoFuncao='Cozinheiro'),
        Funcao(FuncaoID=3, DescricaoFuncao='Auxiliar de Cozinha'),
        Funcao(FuncaoID=4, DescricaoFuncao='Barista'),
        Funcao(FuncaoID=5, DescricaoFuncao='Chapeiro'),
        Funcao(FuncaoID=6, DescricaoFuncao='Limpeza'),
        Funcao(FuncaoID=7, DescricaoFuncao='Caixa'),
        Funcao(FuncaoID=8, DescricaoFuncao='Atendente'),
        Funcao(FuncaoID=9, DescricaoFuncao='Recepcionista'),
        Funcao(FuncaoID=10, DescricaoFuncao='Guardinha')
    ])

    session.add_all([
        Contratante(CNPJ="12345678000101", NomeEstabelecimento="Bar do Ze", Telefone="44999990001", Endereco="Rua das Flores, 100", NomeResponsavel="Jose Silva", TipoEstabelecimento="Bar"),
        Contratante(CNPJ="23456789000102", NomeEstabelecimento="Lanchonete Sabor", Telefone="44999990002", Endereco="Av. Brasil, 200", NomeResponsavel="Ana Costa", TipoEstabelecimento="Lanchonete")
    ])

    session.add_all([
        Freelancer(CPF="11111111111", Nome="Carlos Martins", Telefone="44999880001", FuncaoID=1, Disponibilidade="Noite"),
        Freelancer(CPF="22222222222", Nome="Ana Beatriz", Telefone="44999880002", FuncaoID=2, Disponibilidade="Tarde")
    ])

    session.add_all([
        ValorDiariaHora(ValorID=1, FuncaoID=1, Tipo="hora", Valor=20.00),
        ValorDiariaHora(ValorID=2, FuncaoID=1, Tipo="diaria", Valor=160.00),
        ValorDiariaHora(ValorID=4, FuncaoID=2, Tipo="diaria", Valor=200.00)
    ])

    session.add(
        Agendamento(AgendamentoID=1, CNPJ="12345678000101", CPF="11111111111", Data=date(2025, 7, 1), HoraInicio=time(18, 0), HoraFim=time(23, 0), Modalidade="hora", FuncaoID=1, Status="confirmado")
    )

    session.add(
        Pagamento(PagamentoID=1, CNPJ="12345678000101", CPF="11111111111", FuncaoID=1, ValorID=1, DataPagamento=date(2025, 7, 1), Modalidade="hora", MetodoPagamento="PIX", ValorCalculado=100.00)
    )

    session.commit()

def crud():
    adicionar = Funcao(FuncaoID=11, DescricaoFuncao="DJ")
    session.add(adicionar)
    session.commit()

    alterar = session.query(Funcao).filter_by(FuncaoID=11).first()
    alterar.DescricaoFuncao = "DJ bangela"
    session.commit()

    excluir = session.query(Funcao).filter_by(FuncaoID=4).first()
    session.delete(excluir)
    session.commit()

def show_antes():
    print("\n Funcao Antes:")
    funcoes = session.query(Funcao).all()
    print(f"{'ID':<4} {'Descricao'}")
    print("-" * 30)
    for f in funcoes:
        print(f"{f.FuncaoID:<4} {f.DescricaoFuncao}")

    #print("\n Contratantes:")
    #contratantes = session.query(Contratante).all()
    #print(f"{'CNPJ':<18} {'Nome':<25} {'Responsavel':<20} {'Tipo':<15} {'Telefone':<12} {'Endereco'}")
    #print("-" * 110)
    #for c in contratantes:
    #    print(f"{c.CNPJ:<18} {c.NomeEstabelecimento:<25} {c.NomeResponsavel:<20} {c.TipoEstabelecimento:<15} {c.Telefone:<12} {c.Endereco}")
#
    #print("\n Freelancers:")
    #freelancers = session.query(Freelancer).all()
    #print(f"{'CPF':<12} {'Nome':<20} {'Telefone':<12} {'FuncaoID':<9} {'Disponibilidade'}")
    #print("-" * 70)
    #for f in freelancers:
    #    print(f"{f.CPF:<12} {f.Nome:<20} {f.Telefone:<12} {f.FuncaoID:<9} {f.Disponibilidade}")
#
    #print("\n Valores:")
    #valores = session.query(ValorDiariaHora).all()
    #print(f"{'ID':<4} {'FuncaoID':<9} {'Tipo':<10} {'Valor'}")
    #print("-" * 35)
    #for v in valores:
    #    print(f"{v.ValorID:<4} {v.FuncaoID:<9} {v.Tipo:<10} {v.Valor}")
#
    #print("\n Agendamentos:")
    #agendamentos = session.query(Agendamento).all()
    #print(f"{'ID':<4} {'CPF':<12} {'CNPJ':<18} {'Data':<12} {'Inicio':<8} {'Fim':<8} {'Modalidade':<11} {'FuncaoID':<9} {'Status'}")
    #print("-" * 100)
    #for a in agendamentos:
    #    print(f"{a.AgendamentoID:<4} {a.CPF:<12} {a.CNPJ:<18} {a.Data:<12} {a.HoraInicio:<8} {a.HoraFim:<8} {a.Modalidade:<11} {a.FuncaoID:<9} {a.Status}")
#
#
    #print("\n Pagamentos:")
    #pagamentos = session.query(Pagamento).all()
    #print(f"{'ID':<4} {'CPF':<12} {'CNPJ':<18} {'FuncaoID':<9} {'ValorID':<8} {'Data':<12} {'Modalidade':<11} {'Metodo':<10} {'Valor'}")
    #print("-" * 95)
    #for p in pagamentos:
    #    data = p.DataPagamento.strftime("%d-%m-%Y") if p.DataPagamento else "-"
    #    print(f"{p.PagamentoID:<4} {p.CPF:<12} {p.CNPJ:<18} {p.FuncaoID:<9} {p.ValorID:<8} {p.DataPagamento:} {p.Modalidade:<11} {p.MetodoPagamento:<10} {p.ValorCalculado}")

def show_depois():
    print("\n Funcao Depois:")
    funcoes = session.query(Funcao).all()
    print(f"{'ID':<4} {'Descricao'}")
    print("-" * 30)
    for f in funcoes:
        print(f"{f.FuncaoID:<4} {f.DescricaoFuncao}")

    #print("\n Contratantes:")
    #contratantes = session.query(Contratante).all()
    #print(f"{'CNPJ':<18} {'Nome':<25} {'Responsavel':<20} {'Tipo':<15} {'Telefone':<12} {'Endereco'}")
    #print("-" * 110)
    #for c in contratantes:
    #    print(f"{c.CNPJ:<18} {c.NomeEstabelecimento:<25} {c.NomeResponsavel:<20} {c.TipoEstabelecimento:<15} {c.Telefone:<12} {c.Endereco}")
#
    #print("\n Freelancers:")
    #freelancers = session.query(Freelancer).all()
    #print(f"{'CPF':<12} {'Nome':<20} {'Telefone':<12} {'FuncaoID':<9} {'Disponibilidade'}")
    #print("-" * 70)
    #for f in freelancers:
    #    print(f"{f.CPF:<12} {f.Nome:<20} {f.Telefone:<12} {f.FuncaoID:<9} {f.Disponibilidade}")
#
    #print("\n Valores:")
    #valores = session.query(ValorDiariaHora).all()
    #print(f"{'ID':<4} {'FuncaoID':<9} {'Tipo':<10} {'Valor'}")
    #print("-" * 35)
    #for v in valores:
    #    print(f"{v.ValorID:<4} {v.FuncaoID:<9} {v.Tipo:<10} {v.Valor}")
#
    #print("\n Agendamentos:")
    #agendamentos = session.query(Agendamento).all()
    #print(f"{'ID':<4} {'CPF':<12} {'CNPJ':<18} {'Data':<12} {'Inicio':<8} {'Fim':<8} {'Modalidade':<11} {'FuncaoID':<9} {'Status'}")
    #print("-" * 100)
    #for a in agendamentos:
    #    print(f"{a.AgendamentoID:<4} {a.CPF:<12} {a.CNPJ:<18} {a.Data:<12} {a.HoraInicio:<8} {a.HoraFim:<8} {a.Modalidade:<11} {a.FuncaoID:<9} {a.Status}")
#
#
    #print("\n Pagamentos:")
    #pagamentos = session.query(Pagamento).all()
    #print(f"{'ID':<4} {'CPF':<12} {'CNPJ':<18} {'FuncaoID':<9} {'ValorID':<8} {'Data':<12} {'Modalidade':<11} {'Metodo':<10} {'Valor'}")
    #print("-" * 95)
    #for p in pagamentos:
    #    data = p.DataPagamento.strftime("%d-%m-%Y") if p.DataPagamento else "-"
    #    print(f"{p.PagamentoID:<4} {p.CPF:<12} {p.CNPJ:<18} {p.FuncaoID:<9} {p.ValorID:<8} {p.DataPagamento:} {p.Modalidade:<11} {p.MetodoPagamento:<10} {p.ValorCalculado}")

if __name__ == "__main__":
    #reset_db()
    #insert_initial_data()
    show_antes()
    crud()
    show_depois()