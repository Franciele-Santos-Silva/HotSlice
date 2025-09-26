from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/autenticcao")
async def autenticacao():
    return {"mensagem": "Você acessou a rota de autenticação"}

@auth_router.post("/cadastrar")
async def pedidos():
    return{"mensagem": "Cliente cadastrado com sucesso"}

@auth_router.delete("/deletar")
async def pedidos():
    return{"mensagem": "Cliente deletado com sucesso"}

@auth_router.put("/atualizar")
async def pedidos():
    return{"mensagem": "Cliente atualizado com sucesso"}

@auth_router.patch("/atualizar")
async def pedidos():
    return{"mensagem": "Cliente atualizado com sucesso"}