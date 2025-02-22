from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import pedidos
from app.database import engine, Base

# Cria as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

# Inicialização do FastAPI
app = FastAPI(
    title="Sistema de Gestão de Pedidos",
    description="API para gerenciar pedidos de clientes",
    version="1.0.0"
)

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Permite apenas o frontend local
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "API de Gestão de Pedidos está rodando!"}

# Incluindo as rotas do módulo de pedidos
app.include_router(pedidos.router, prefix="/api", tags=["Pedidos"])
