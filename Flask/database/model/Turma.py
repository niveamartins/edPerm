from sqlalchemy import Column, String, Integer,Numeric,Text, Enum, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from database.model.Base.Base import Base

class Turma(Base):
    __tablename__ = 'Turma'
    IdTurma = Column(Integer,primary_key=True)
    IdResponsavel = Column(Integer, ForeignKey('User.Id'), nullable=False)
    NomeCurso = Column(String(50), nullable=False)
    CargaHorariaTotal = Column(Integer, nullable=False)
    Tolerancia = Column(Integer, nullable=False)
    Modalidade = Column(String, nullable=False)
    TurmaTag = Column(String, nullable=False)