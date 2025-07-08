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
        Contratante(CNPJ="42370268000199", NomeEstabelecimento="Bar do Ze", Telefone="44998123456", Endereco="Rua das Flores, 100", NomeResponsavel="Jose Silva", TipoEstabelecimento="Bar"),
        Contratante(CNPJ="09182734000155", NomeEstabelecimento="Lanchonete Sabor", Telefone="44998234567", Endereco="Av. Brasil, 200", NomeResponsavel="Ana Costa", TipoEstabelecimento="Lanchonete"),
        Contratante(CNPJ="31654987000120", NomeEstabelecimento="Restaurante Delicia", Telefone="44998345678", Endereco="Rua Central, 300", NomeResponsavel="Mario Lima", TipoEstabelecimento="Restaurante"),
        Contratante(CNPJ="72093556000181", NomeEstabelecimento="Pizzaria Massa", Telefone="44998456789", Endereco="Av. Sao Paulo, 400", NomeResponsavel="Laura Souza", TipoEstabelecimento="Pizzaria"),
        Contratante(CNPJ="87564320000133", NomeEstabelecimento="Cafe Aroma", Telefone="44998567890", Endereco="Rua das Palmeiras, 500", NomeResponsavel="Paulo Ramos", TipoEstabelecimento="Cafe"),
        Contratante(CNPJ="26143978000177", NomeEstabelecimento="Hamburgueria Top", Telefone="44998678901", Endereco="Av. Parana, 600", NomeResponsavel="Luciana Alves", TipoEstabelecimento="Hamburgueria"),
        Contratante(CNPJ="53001749000114", NomeEstabelecimento="Bar da Esquina", Telefone="44998789012", Endereco="Rua 7 de Setembro, 700", NomeResponsavel="Carlos Mendes", TipoEstabelecimento="Bar"),
        Contratante(CNPJ="64839225000169", NomeEstabelecimento="Espetinho Bom", Telefone="44998890123", Endereco="Av. Getulio Vargas, 800", NomeResponsavel="Fernanda Dias", TipoEstabelecimento="Espetaria"),
        Contratante(CNPJ="79432111000188", NomeEstabelecimento="Tapiocaria Saborosa", Telefone="44998901234", Endereco="Rua dos Comerciantes, 900", NomeResponsavel="Juliana Castro", TipoEstabelecimento="Tapiocaria"),
        Contratante(CNPJ="10345678000101", NomeEstabelecimento="Sushi Place", Telefone="44999012345", Endereco="Av. Japao, 1000", NomeResponsavel="Takashi Ito", TipoEstabelecimento="Restaurante Japones")
    ])

    session.add_all([
        Freelancer(CPF="12345678900", Nome="Carlos Martins", Telefone="44998011111", FuncaoID=1, Disponibilidade="Noite"),
        Freelancer(CPF="23456789012", Nome="Ana Beatriz", Telefone="44998022222", FuncaoID=2, Disponibilidade="Tarde"),
        Freelancer(CPF="34567890123", Nome="Bruno Lima", Telefone="44998033333", FuncaoID=3, Disponibilidade="Manha"),
        Freelancer(CPF="45678901234", Nome="Camila Rocha", Telefone="44998044444", FuncaoID=4, Disponibilidade="Noite"),
        Freelancer(CPF="56789012345", Nome="Daniel Souza", Telefone="44998055555", FuncaoID=5, Disponibilidade="Tarde"),
        Freelancer(CPF="67890123456", Nome="Elisa Ferreira", Telefone="44998066666", FuncaoID=6, Disponibilidade="Manha"),
        Freelancer(CPF="78901234567", Nome="Felipe Andrade", Telefone="44998077777", FuncaoID=7, Disponibilidade="Noite"),
        Freelancer(CPF="89012345678", Nome="Gabriela Nunes", Telefone="44998088888", FuncaoID=8, Disponibilidade="Tarde"),
        Freelancer(CPF="90123456789", Nome="Henrique Oliveira", Telefone="44998099999", FuncaoID=9, Disponibilidade="Manha"),
        Freelancer(CPF="01234567890", Nome="Isabela Mendes", Telefone="44998101010", FuncaoID=10, Disponibilidade="Tarde")
    ])

    session.add_all([
        ValorDiariaHora(ValorID=1, FuncaoID=1, Tipo="hora", Valor=20.00),
        ValorDiariaHora(ValorID=2, FuncaoID=1, Tipo="diaria", Valor=160.00),
        ValorDiariaHora(ValorID=3, FuncaoID=2, Tipo="hora", Valor=25.00),
        ValorDiariaHora(ValorID=4, FuncaoID=2, Tipo="diaria", Valor=200.00),
        ValorDiariaHora(ValorID=5, FuncaoID=3, Tipo="hora", Valor=18.00),
        ValorDiariaHora(ValorID=6, FuncaoID=4, Tipo="diaria", Valor=150.00),
        ValorDiariaHora(ValorID=7, FuncaoID=5, Tipo="hora", Valor=22.00),
        ValorDiariaHora(ValorID=8, FuncaoID=6, Tipo="diaria", Valor=140.00),
        ValorDiariaHora(ValorID=9, FuncaoID=7, Tipo="hora", Valor=19.00),
        ValorDiariaHora(ValorID=10, FuncaoID=8, Tipo="diaria", Valor=145.00)
    ])

    session.add(
       Agendamento(AgendamentoID=1, CNPJ="42370268000199", CPF="12345678900", Data=date(2025, 7, 1), HoraInicio=time(18, 0), HoraFim=time(23, 0), Modalidade="hora", FuncaoID=1, Status="confirmado"),
        Agendamento(AgendamentoID=2, CNPJ="09182734000155", CPF="23456789012", Data=date(2025, 7, 2), HoraInicio=time(10, 0), HoraFim=time(16, 0), Modalidade="diaria", FuncaoID=2, Status="pendente"),
        Agendamento(AgendamentoID=3, CNPJ="31654987000120", CPF="34567890123", Data=date(2025, 7, 3), HoraInicio=time(8, 0), HoraFim=time(12, 0), Modalidade="hora", FuncaoID=3, Status="confirmado"),
        Agendamento(AgendamentoID=4, CNPJ="72093556000181", CPF="45678901234", Data=date(2025, 7, 4), HoraInicio=time(14, 0), HoraFim=time(22, 0), Modalidade="diaria", FuncaoID=4, Status="cancelado"),
        Agendamento(AgendamentoID=5, CNPJ="87564320000133", CPF="56789012345", Data=date(2025, 7, 5), HoraInicio=time(15, 0), HoraFim=time(20, 0), Modalidade="hora", FuncaoID=5, Status="confirmado"),
        Agendamento(AgendamentoID=6, CNPJ="26143978000177", CPF="67890123456", Data=date(2025, 7, 6), HoraInicio=time(9, 0), HoraFim=time(17, 0), Modalidade="diaria", FuncaoID=6, Status="pendente"),
        Agendamento(AgendamentoID=7, CNPJ="53001749000114", CPF="78901234567", Data=date(2025, 7, 7), HoraInicio=time(12, 0), HoraFim=time(18, 0), Modalidade="hora", FuncaoID=7, Status="confirmado"),
        Agendamento(AgendamentoID=8, CNPJ="64839225000169", CPF="89012345678", Data=date(2025, 7, 8), HoraInicio=time(17, 0), HoraFim=time(22, 0), Modalidade="diaria", FuncaoID=8, Status="confirmado"),
        Agendamento(AgendamentoID=9, CNPJ="79432111000188", CPF="90123456789", Data=date(2025, 7, 9), HoraInicio=time(7, 0), HoraFim=time(13, 0), Modalidade="hora", FuncaoID=9, Status="pendente"),
        Agendamento(AgendamentoID=10, CNPJ="10345678000101", CPF="01234567890", Data=date(2025, 7, 10), HoraInicio=time(16, 0), HoraFim=time(22, 0), Modalidade="diaria", FuncaoID=10, Status="confirmado")
    )

    session.add(
        Pagamento(PagamentoID=1, CNPJ="42370268000199", CPF="12345678900", FuncaoID=1, ValorID=1, DataPagamento=date(2025, 7, 1), Modalidade="hora", MetodoPagamento="PIX", ValorCalculado=100.00),
        Pagamento(PagamentoID=2, CNPJ="09182734000155", CPF="23456789012", FuncaoID=2, ValorID=4, DataPagamento=date(2025, 7, 2), Modalidade="diaria", MetodoPagamento="Cartao", ValorCalculado=200.00),
        Pagamento(PagamentoID=3, CNPJ="31654987000120", CPF="34567890123", FuncaoID=3, ValorID=5, DataPagamento=date(2025, 7, 3), Modalidade="hora", MetodoPagamento="Dinheiro", ValorCalculado=72.00),
        Pagamento(PagamentoID=4, CNPJ="72093556000181", CPF="45678901234", FuncaoID=4, ValorID=6, DataPagamento=date(2025, 7, 4), Modalidade="diaria", MetodoPagamento="PIX", ValorCalculado=150.00),
        Pagamento(PagamentoID=5, CNPJ="87564320000133", CPF="56789012345", FuncaoID=5, ValorID=7, DataPagamento=date(2025, 7, 5), Modalidade="hora", MetodoPagamento="Cartao", ValorCalculado=110.00),
        Pagamento(PagamentoID=6, CNPJ="26143978000177", CPF="67890123456", FuncaoID=6, ValorID=8, DataPagamento=date(2025, 7, 6), Modalidade="diaria", MetodoPagamento="Dinheiro", ValorCalculado=140.00),
        Pagamento(PagamentoID=7, CNPJ="53001749000114", CPF="78901234567", FuncaoID=7, ValorID=9, DataPagamento=date(2025, 7, 7), Modalidade="hora", MetodoPagamento="PIX", ValorCalculado=95.00),
        Pagamento(PagamentoID=8, CNPJ="64839225000169", CPF="89012345678", FuncaoID=8, ValorID=10, DataPagamento=date(2025, 7, 8), Modalidade="diaria", MetodoPagamento="Cartao", ValorCalculado=145.00),
        Pagamento(PagamentoID=9, CNPJ="79432111000188", CPF="90123456789", FuncaoID=9, ValorID=9, DataPagamento=date(2025, 7, 9), Modalidade="hora", MetodoPagamento="Dinheiro", ValorCalculado=114.00),
        Pagamento(PagamentoID=10, CNPJ="10345678000101", CPF="01234567890", FuncaoID=10, ValorID=10, DataPagamento=date(2025, 7, 10), Modalidade="diaria", MetodoPagamento="PIX", ValorCalculado=145.00)
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

    alterar2 = session.query(Funcao).filter_by(FuncaoID=2).first()
    alterar2.DescricaoFuncao = "Cozinheiro Chef"
    session.commit()

    excluir2 = session.query(Freelancer).filter_by(CPF="56789012345").first()
    session.delete(excluir2)
    session.commit()

    novopagamento = Pagamento(
        PagamentoID=11,
        CNPJ="42370268000199",
        CPF="23456789012",
        FuncaoID=2,
        ValorID=4,
        DataPagamento=date(2025, 7, 11),
        Modalidade="Diária",
        MetodoPagamento="Cartão",
        ValorCalculado=210.00
    )
    session.add(novopagamento)
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

def freelancersporcontratante(cnpj):
    print(f"\nFreelancers contratados por {cnpj}:")
    agendamentos = session.query(Agendamento).filter_by(CNPJ=cnpj).all()
    for a in agendamentos:
        freelancer = session.query(Freelancer).filter_by(CPF=a.CPF).first()
        print(f"- {freelancer.Nome} (CPF: {freelancer.CPF})")

def contratantesdofreelancer(cpf):
    print(f"\nContratantes que contrataram o freelancer {cpf}:")
    agendamentos = session.query(Agendamento).filter_by(CPF=cpf).all()
    for a in agendamentos:
        contratante = session.query(Contratante).filter_by(CNPJ=a.CNPJ).first()
        print(f"- {contratante.NomeEstabelecimento} (CNPJ: {contratante.CNPJ})")

def listaragendamentoscomnomes():
    print("\nAgendamentos:")
    agendamentos = session.query(Agendamento).all()
    for a in agendamentos:
        freelancer = session.query(Freelancer).filter_by(CPF=a.CPF).first()
        contratante = session.query(Contratante).filter_by(CNPJ=a.CNPJ).first()
        print(f"{a.Data} | {freelancer.Nome} -> {contratante.NomeEstabelecimento} | Status: {a.Status}")


if __name__ == "__main__":
    #reset_db()
    #insert_initial_data()
    show_antes()
    crud()
    show_depois()
    listaragendamentoscomnomes()
    contratantesdofreelancer()
    freelancersporcontratante()