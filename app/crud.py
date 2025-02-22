from sqlalchemy.orm import Session
from app import models, schemas
import uuid

# Criar um novo pedido
def criar_pedido(db: Session, pedido: schemas.PedidoCreate):
    db_pedido = models.Pedido(
        id=uuid.uuid4(),
        cliente=pedido.cliente,
        valor=pedido.valor,
        descricao=pedido.descricao
    )
    db.add(db_pedido)
    db.commit()
    db.refresh(db_pedido)
    return db_pedido

# Listar pedidos com paginação
def listar_pedidos(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Pedido).offset(skip).limit(limit).all()

# Obter um pedido por ID
def obter_pedido(db: Session, pedido_id: str):
    return db.query(models.Pedido).filter(models.Pedido.id == pedido_id).first()

# Deletar um pedido
def deletar_pedido(db: Session, pedido_id: str):
    pedido = obter_pedido(db, pedido_id)
    if pedido:
        db.delete(pedido)
        db.commit()
        return pedido
    return None
