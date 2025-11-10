from pydantic import BaseModel
from typing import Optional

class UsuarioSchema(BaseModel):
        nome: str
        email: str
        senha: str
        ativo: Optional[bool] 
        admin: Optional[bool]

        class Config:
            from_attributes = True

class PedidosSchemas(BaseModel):
        usuario: int
        status: Optional[str]
        preco: Optional[float]

        class Config:
            from_attributes = True


