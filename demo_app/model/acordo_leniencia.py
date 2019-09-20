from sqlalchemy import Column, Integer, ForeignKey, DateTime

from declarative import Base


class AcordoLeniencia(Base):
    id = Column(Integer, primary_key=True)
    dataFimAcordo = Column(DateTime)
    dataInicioAcordo = Column(DateTime)
    idEmpresa = Column(Integer, ForeignKey('empresa.id'))
