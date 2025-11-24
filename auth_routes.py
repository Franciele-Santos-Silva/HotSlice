from fastapi import APIRouter, Depends, HTTPException
from models import Usuario
from dependecies import pegar_sessao, verificar_token
from main import bcrypt_context, ALGORITHM, ACESS_TOKEN_EXPIRE_MINUTES, SERCRET_KEY
from schemas import UsuarioSchema, LoginSchema
from sqlalchemy.orm import Session 
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone

auth_router = APIRouter(prefix="/auth", tags=["auth"])

def criar_token(id_usuario, duracao_token= timedelta(minutes=ACESS_TOKEN_EXPIRE_MINUTES)):
    data_expiração = datetime.now(timezone.utc) + duracao_token
    dic_info = {
        "sub": id_usuario,
        "exp": data_expiração
    }
    jwt_codificado = jwt.encode(dic_info, SERCRET_KEY, algorithm= ALGORITHM)
    return jwt_codificado

def autenticar_usuario(email, senha, session):
    usuario = session.query(Usuario).filter(Usuario.email == email).first()

    if not usuario:
        return False
    elif not bcrypt_context.verify(senha, usuario.senha):  
        return False

    return usuario

@auth_router.get("/")
async def home():
    return {"mensagem": "Você acessou a rota de autenticação", "autenticado": False}

@auth_router.post("/criar_conta")
async def criar_conta(usuario_schema: UsuarioSchema, session: Session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email == usuario_schema.email).first()
    if usuario:
        raise HTTPException(status_code=400, detail="Já existe uma conta com esse e-mail")
    else:
        senha_criptografada = bcrypt_context.hash(usuario_schema.senha)
        novo_usuario = Usuario(
            nome=usuario_schema.nome,
            email=usuario_schema.email,
            senha=senha_criptografada,
            ativo=usuario_schema.ativo,
            admin=usuario_schema.admin
        )
        session.add(novo_usuario)
        session.commit()
        return {"mensagem": f"Usuário {usuario_schema.email} cadastrado com sucesso"}

@auth_router.post("/login")
async def login(login_schema: LoginSchema, session: Session = Depends(pegar_sessao)):
    usuario = autenticar_usuario(login_schema.email, login_schema.senha, session)
    if not usuario:
        raise HTTPException(status_code=400, detail="Usuário não encontrado ou credenciais inválidas")  # Corrigido
    else:
        access_token = criar_token(usuario.id)
        refresh_token = criar_token(usuario.id, duracao_token= timedelta(days= 7))  
        return {
            "access_token": access_token, 
            "refresh_token": refresh_token,
            "token_type": "bearer"
        }

@auth_router.get("/refresh")
async def use_refresh_token(usuario: Usuario = Depends(verificar_token)):
    usuario = verificar_token(token)
    access_token = criar_token(usuario.id)
    return {
        "access_token": access_token,
        "token_type": "bearer"
    }