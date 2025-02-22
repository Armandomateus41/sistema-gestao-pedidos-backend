from pydantic import BaseModel
from typing import Optional
from uuid import UUID

# ---------------------
# Esquemas para Pedido
# ---------------------

class PedidoBase(BaseModel):
    cliente: str
    valor: float
    descricao: Optional[str] = None

class PedidoCreate(PedidoBase):
    pass

class Pedido(PedidoBase):
    id: UUID

    class Config:
        from_attributes = True  # Atualizado para Pydantic v2

# ---------------------
# Esquemas para Usuário
# ---------------------

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: UUID
    is_admin: bool

    class Config:
        from_attributes = True  # Atualizado para Pydantic v2

# ---------------------
# Esquema para Token
# ---------------------

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
