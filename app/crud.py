
# app/crud.py

from sqlalchemy.orm import Session
from app import models, schemas

# Criar um novo pedido
def criar_pedido(db: Session, pedido: schemas.PedidoCreate):
    db_pedido = models.Pedido(**pedido.dict())
    db.add(db_pedido)
    db.commit()
    db.refresh(db_pedido)
    return db_pedido

# Listar todos os pedidos
def listar_pedidos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Pedido).offset(skip).limit(limit).all()

# Obter um pedido por ID
def obter_pedido(db: Session, pedido_id: str):
    return db.query(models.Pedido).filter(models.Pedido.id == pedido_id).first()

# Atualizar um pedido
def atualizar_pedido(db: Session, pedido_id: str, pedido: schemas.PedidoCreate):
    db_pedido = obter_pedido(db, pedido_id)
    if not db_pedido:
        return None
    for key, value in pedido.dict().items():
        setattr(db_pedido, key, value)
    db.commit()
    db.refresh(db_pedido)
    return db_pedido

# Deletar um pedido
def deletar_pedido(db: Session, pedido_id: str):
    db_pedido = obter_pedido(db, pedido_id)
    if not db_pedido:
        return None
    db.delete(db_pedido)
    db.commit()
    return db_pedido
