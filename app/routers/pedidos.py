# app/routers/pedidos.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import schemas, crud, database
from app.routers.auth import get_current_user

router = APIRouter()

# Endpoint para criar um pedido
@router.post("/pedidos/", response_model=schemas.Pedido)
def criar_pedido(pedido: schemas.PedidoCreate, db: Session = Depends(database.get_db), current_user=Depends(get_current_user)):
    return crud.criar_pedido(db, pedido)

# Endpoint para listar pedidos
@router.get("/pedidos/", response_model=List[schemas.Pedido])
def listar_pedidos(skip: int = 0, limit: int = 10, db: Session = Depends(database.get_db), current_user=Depends(get_current_user)):
    return crud.listar_pedidos(db, skip=skip, limit=limit)

# Endpoint para obter um pedido específico
@router.get("/pedidos/{pedido_id}", response_model=schemas.Pedido)
def obter_pedido(pedido_id: str, db: Session = Depends(database.get_db), current_user=Depends(get_current_user)):
    pedido = crud.obter_pedido(db, pedido_id)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return pedido

# Endpoint para deletar um pedido
@router.delete("/pedidos/{pedido_id}")
def deletar_pedido(pedido_id: str, db: Session = Depends(database.get_db), current_user=Depends(get_current_user)):
    pedido = crud.deletar_pedido(db, pedido_id)
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    return {"message": "Pedido deletado com sucesso"}
