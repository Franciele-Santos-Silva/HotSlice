from fastapi import APIRouter
from models import Usuario, db
from sqlalchemy.orm import sessionmaker

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/")
async def home():
    return {"mensagem": "Você acessou a rota de autenticação", "autenticado": False}

@auth_router.post("/criar_conta")
async def criar_conta(email: str, senha: str, nome: str):
    Session = sessionmaker(bind=db)
    session = Session()
    usuario = session.query(Usuario).filter(Usuario.email == email).all()
    if usuario:
        return {"mensagem": "Email já cadastrado", "sucesso": False}
    else:
        novo_usuario =Usuario(nome, email, senha)
        session.add(novo_usuario)