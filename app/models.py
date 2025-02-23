
# app/models.py

from sqlalchemy import Column, String, Float, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from app.database import Base
import uuid

class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    cliente = Column(String, nullable=False)
    valor = Column(Float, nullable=False)
    descricao = Column(String, nullable=True)
    data_criacao = Column(DateTime(timezone=True), server_default=func.now())
