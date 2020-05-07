from sqlalchemy import Column, String, Integer, Time, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from database.model.Base.Base import Base

class Horario(Base):
    __tablename__ = 'Horario'
    idHorario = Column(Integer, primary_key=True)
    HorarioIdTurma = Column(Integer, ForeignKey('Turma.idTurma'), nullable=False)
    DiaDaSemana = Column(String(20), nullable=False)
    HorarioInicio = Column(Time, nullable=False)
    HorarioTermino = Column(Time, nullable=False)
