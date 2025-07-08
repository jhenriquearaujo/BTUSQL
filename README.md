
# Projeto BTU - Banco de Dados com ORM (SQLAlchemy)

Este projeto implementa a Fase 6 do trabalho de Banco de Dados da UTFPR, usando SQLAlchemy para mapear o banco relacional do BTU.

## ✅ Requisitos

- Python 3.10+
- PostgreSQL
- SQLAlchemy

## 🚀 Como usar

1. Crie o ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate no Windows
```

2. Instale dependências:

```bash
pip install sqlalchemy psycopg2 pg8000
```

3. Configure sua string de conexão em `database.py`

4. Execute o `main.py`:

```bash
python main.py
```

## 📚 Funcionalidades

- Mapeamento completo das tabelas com SQLAlchemy
- Inserção de dados de teste
- CRUD para entidade `Funcao`
- Consultas ORM com joins e filtros

## 📁 Estrutura

- `models.py` – Entidades do banco
- `crud.py` – Operações de CRUD e consultas
- `main.py` – Ponto de entrada
