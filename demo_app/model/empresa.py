from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from declarative import Base


class Empresa(Base):
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    cnpj = Column(String)
    razaoSocial = Column(String)
    acordoLeniencia = relationship("AcordoLeniencia")
