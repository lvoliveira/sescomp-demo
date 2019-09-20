from sqlalchemy import Column, Integer, String

from declarative import Base


class Empresa(Base):
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cnpj = Column(String)
    razaoSocial = Column(String)
