from sqlalchemy import create_engine, Colum, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base


db = create_engine("sqlite:///banco.db");

Base = declarative_base();

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Colum("id", Integer, primary_key=True, autoincrement=True);
    nome = Colum("id", String, nullable=False);
    email = Colum("id", String, nullable=False);
    senha = Colum("id", String);
    ativo = Colum("id", Boolean);
    admin = Colum("id", Boolean);

