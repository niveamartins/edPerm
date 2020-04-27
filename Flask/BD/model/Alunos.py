from sqlalchemy import Column, String, Integer, Time, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from BD.model.Base.Base import Base

class Alunos(Base):
    __tablename__ = 'Alunos'
    idAluno = Column(Integer,primary_key=True)
    AlunosIdTurma = Column(Integer, ForeignKey('Turma.IdTurma'), nullable=False)
    AlunosIdUser = Column(Integer, ForeignKey('User.Id'), nullable=False)
    Presenca = Column(Integer, nullable=False)