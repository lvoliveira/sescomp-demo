from sqlalchemy import Column, Integer, ForeignKey, String

from declarative import Base


class AcordoLeniencia(Base):
    id = Column(Integer, primary_key=True)
    dataFimAcordo = Column(String)
    dataInicioAcordo = Column(String)
    idEmpresa = Column(Integer, ForeignKey('empresa.id'))
