
# app/schemas.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID

class PedidoBase(BaseModel):
    cliente: str
    valor: float
    descricao: Optional[str] = None

class PedidoCreate(PedidoBase):
    pass

class Pedido(PedidoBase):
    id: UUID
    data_criacao: datetime

    class Config:
        orm_mode = True
