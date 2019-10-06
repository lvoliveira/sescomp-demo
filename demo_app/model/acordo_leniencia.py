from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from declarative import Base
from model.empresa import Empresa


class AcordoLeniencia(Base):
    id = Column(Integer, primary_key=True)
    dataFimAcordo = Column(String)
    dataInicioAcordo = Column(String)
    idEmpresa = Column(Integer, ForeignKey('empresa.id'))
    empresa = relationship(Empresa)
