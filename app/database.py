# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexão com o PostgreSQL
DATABASE_URL = "postgresql+psycopg2://postgres:123456@localhost:5432/pedidos_db"

# Cria o engine de conexão
engine = create_engine(DATABASE_URL)

# Cria uma instância de sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para criação dos modelos
Base = declarative_base()

# Função para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
