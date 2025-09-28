from sqlalchemy import create_engine, Colum, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base

db = create_engine("sqlite:///banco.db");

Base = declarative_base();

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Colum("id", Integer, primary_key=True, autoincrement=True);
    nome = Colum("nome", String);
    email = Colum("email", String, nullable=False);
    senha = Colum("senha", String);
    ativo = Colum("ativo", Boolean);
    admin = Colum(" admin", Boolean, default=False);

    def __init__(self, nome, email, senha, ativo = True, admin = False ): 
        self.nome = nome
        self.nome = email
        self.nome = senha
        self.nome = ativo
        self.nome = admin


