# BTUSQL

# ✅ Windows (cmd ou PowerShell)

.\venv\Scripts\activate

# ✅ Linux (bash/zsh)

bash
source venv/bin/activate

# ✅ macOS (bash/zsh)

bash 
source venv/bin/activate

Para sair do ambiente virtual: deactivate

# Dependencias dentro do venv
- pip install sqlAlchemy
- pip install pg8000
- Se não me engano: pip install Alembic

# Para executar

Mudar no database.py de acordo com sua máquina
DATABASE_URL = "postgresql+pg8000://postgres:xina@localhost:5432/postgres"

python main.py