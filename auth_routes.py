from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/autenticcao")
async def autenticacao():
    return {"mensagem": "Você acessou a rota de autenticação"}