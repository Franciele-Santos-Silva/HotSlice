from fastapi import APIRouter, Depends
from models import Pedidos
from schemas import PedidoSchema
from sqlalchemy.orm import Session
from dependecies import pegar_sessao

order_router = APIRouter(prefix="/pedidos", tags=["pedidos"])

@order_router.get("/")
async def pedidos():
    return{"mensagem": "Você acessou a rota de pedidos"}

@order_router.post("/pedido")
async def criar_pedido(pedido_schema: PedidoSchema, session: Session = Depends(pegar_sessao)):
    novo_pedido = Pedidos(usuario= pedido_schema.id_usuario)
    session.add(novo_pedido)
    session.commit()
    return {"messagem": f"Pedido feito com sucesso. ID do pedido é {novo_pedido.id}"}
    
