
# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import pedidos
from app.database import engine, Base

# Criação das tabelas no banco
Base.metadata.create_all(bind=engine)

# Inicialização do FastAPI
app = FastAPI(
    title="Sistema de Gestão de Pedidos",
    description="API para gerenciar pedidos de clientes",
    version="1.0.0"
)

# Configuração do CORS para permitir o acesso do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # URL do frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Rota raiz
@app.get("/")
def read_root():
    return {"message": "API de Gestão de Pedidos está rodando!"}

# Incluindo as rotas de pedidos
app.include_router(pedidos.router, prefix="/api")
