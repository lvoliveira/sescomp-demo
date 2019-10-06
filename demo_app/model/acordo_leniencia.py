from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from declarative import Base
from model.empresa import Empresa


class AcordoLeniencia(Base):
    id = Column(Integer, primary_key=True)
    dataFimAcordo = Column(DateTime)
    dataInicioAcordo = Column(DateTime)
    idEmpresa = Column(Integer, ForeignKey('empresa.id'))
    empresa = relationship(Empresa)
