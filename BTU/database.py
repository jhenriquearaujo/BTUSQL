#import sqlalchemy # Manter esta linha se for usada implicitamente ou para outras funcionalidades
#import psycopg2 
#from sqlalchemy import create_engine
#from sqlalchemy.orm import sessionmaker, declarative_base
#
##DATABASE_URL = "postgresql://postgres:xina@localhost:5432/BTUSQL"
#DATABASE_URL = "postgresql+psycopg2cffi://postgres:xina@localhost:5432/BTUSQL"
#
#engine = create_engine(DATABASE_URL, echo=False)
#Session = sessionmaker(bind=engine)
#
#Base = declarative_base()
#
#print("aaa")

#import pg8000
#
## Parâmetros de conexão
#host = "localhost"         # ou IP do servidor PostgreSQL
#port = 5432                # porta padrão
#database = "postgres"     # nome do banco de dados
#user = "postgres"       # nome do usuário
#password = "xina"   # senha do usuário
#
#try:
#    # Conectando ao PostgreSQL
#    conexao = pg8000.connect(
#        user=user,
#        password=password,
#        host=host,
#        port=port,
#        database=database
#    )
#
#    # Criando cursor
#    cursor = conexao.cursor()
#
#    # Executando uma consulta
#    cursor.execute("SELECT version();")
#    resultado = cursor.fetchone()
#    print(f"Conectado ao PostgreSQL: {resultado[0]}")
#
#    # Fechando
#    cursor.close()
#    conexao.close()
#
#except Exception as erro:
#    print(f"Erro ao conectar: {erro}")

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL de conexão com pg8000 como driver
DATABASE_URL = "postgresql+pg8000://postgres:xina@localhost:5432/postgres"

# Cria o engine usando pg8000
engine = create_engine(DATABASE_URL, echo=False)

# Cria a base para os modelos
Base = declarative_base()

# Cria a fábrica de sessões
Session = sessionmaker(bind=engine)
