from models import db
from fastapi import Depends
from sqlalchemy.orm import sessionmaker, Session
from models import Usuario
from fastapi import Depends

def pegar_sessao():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()

def verificar_token(token, session: Session = Depends(pegar_sessao)):

    usuario = session.query(Usuario).filter(Usuario.id == 1).first()
    return usuario