from fastapi import APIRouter, Depends
from models import Pedidos
from schemas import PedidosSchema
from sqlalchemy.orm import Session
from dependecies import pegar_sessao

order_router = APIRouter(prefix="/pedidos", tags=["pedidos"])

@order_router.get("/")
async def pedidos():
    return{"mensagem": "Você acessou a rota de pedidos"}

@order_router.post("/pedido")
async def criar_pedido(pedido_schema: PedidosSchema, session: Session = Depends(pegar_sessao)):
    novo_pedido = Pedidos(pedido_schema.usuario, pedido_schema.status, pedido_schema.preco)
    session.add(novo_pedido)
    session.commit()
    return {"messagem": "Pedido feito com sucesso"}
    
