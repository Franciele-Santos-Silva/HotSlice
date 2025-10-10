from sqlalchemy import create_engine, Colum, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils.types import ChoiceType

db = create_engine("sqlite:///banco.db");

Base = declarative_base();

class Usuario(Base):
    __tablename__ = "usuarios"

id = Colum("id", Integer, primary_key=True, autoincrement=True);
nome = Colum("nome", String);
email = Colum("email", String, nullable=False);
senha = Colum("senha", String);
ativo = Colum("ativo", Boolean);
admin = Colum("admin", Boolean, default=False);

def __init__(self, nome, email, senha, ativo = True, admin = False ): 
    self.nome = nome
    self.email = email
    self.senha = senha
    self.ativo = ativo
    self.admin = admin

class Pedidos(Base):
     __tablename__ = "pedidos"

STATUS_PEDIDOS = (
    ("PENDENTE", "PENDENTE"),
    ("CANCELADO", "CANCELADO"),
    ("FINALIZADO", "FINALIZADO")
)

id = Colum("id", Integer, primary_key=True, autoincrement=True);
status = Colum("status", ChoiceType(choices = STATUS_PEDIDOS));
usuario = Colum("usuario", String, ForeignKey("usuarios.id"));
preco = Colum("preco", Float );

def __init__(self, usuario, status = "PENDENTE", preco = 0): 
    self.status = status
    self.usuario = usuario
    self.preco = preco


class ItemPedido(Base):
    __tablename__ = "pedido_itens"

