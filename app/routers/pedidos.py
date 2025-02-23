
# app/routers/pedidos.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas, crud, database

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])

# Rota para criar um pedido
@router.post("/", response_model=schemas.Pedido)
def criar_pedido(pedido: schemas.PedidoCreate, db: Session = Depends(database.get_db)):
    return crud.criar_pedido(db, pedido)

# Rota para listar todos os pedidos
@router.get("/", response_model=List[schemas.Pedido])
def listar_pedidos(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db)):
    return crud.listar_pedidos(db, skip=skip, limit=limit)

# Rota para obter um pedido por ID
@router.get("/{pedido_id}", response_model=schemas.Pedido)
def obter_pedido(pedido_id: str, db: Session = Depends(database.get_db)):
    pedido = crud.obter_pedido(db, pedido_id)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return pedido

# Rota para atualizar um pedido
@router.put("/{pedido_id}", response_model=schemas.Pedido)
def atualizar_pedido(pedido_id: str, pedido: schemas.PedidoCreate, db: Session = Depends(database.get_db)):
    pedido_atualizado = crud.atualizar_pedido(db, pedido_id, pedido)
    if not pedido_atualizado:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return pedido_atualizado

# Rota para deletar um pedido
@router.delete("/{pedido_id}")
def deletar_pedido(pedido_id: str, db: Session = Depends(database.get_db)):
    pedido_deletado = crud.deletar_pedido(db, pedido_id)
    if not pedido_deletado:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return {"message": "Pedido deletado com sucesso"}
