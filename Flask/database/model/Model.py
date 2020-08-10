from sqlalchemy import (Column, String, Integer, Text,
                        Enum, ForeignKey, Table, Time, Boolean, DateTime, Interval)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from database.model.Base.Base import Base
from datetime import datetime,timedelta
import uuid
# ASSOCIATIONS TABLES

alunoApoiadoXturma = Table('aaxt', Base.metadata,
                           Column('alunoApoiador_id', Integer, ForeignKey(
                               'alunoApoiador.id_alunoApoiador')),
                           Column('turma_id', Integer,
                                  ForeignKey('turma.id_turma'))
                           )

alunoXturma = Table('axt', Base.metadata,
                    Column('aluno_id', Integer, ForeignKey('aluno.id_aluno')),
                    Column('turma_id', Integer, ForeignKey('turma.id_turma'))
                    )


# MODELS

class User(Base):
    __tablename__ = 'user'
    Id = Column(Integer, primary_key=True)
    usuario = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    senha = Column(Text, nullable=False)
    cpf = Column(String(11), nullable=False)
    telefone = Column(String(9), nullable=False)
    tipo = Column(Enum('adm', 'gestor', 'coordenador',
                       'propositor', 'cursista', 'apoiador'), nullable=False)
    funcao = Column(Text,nullable=True)
    profissao = Column(Text,nullable=True)
    UnidadeBasicadeSaude=Column(Text,nullable=True)
    CAP=Column(String(4),nullable=True)

    # ONE TO ONE

    Aluno = relationship('Aluno', uselist=False, backref='alunoUser')
    AlunoApoiador = relationship(
        'AlunoApoiador', uselist=False, backref='alunoApoiadorUser')

    # ONE TO MANY
    TurmaProposta = relationship('Turma', backref='propositor')

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Aluno(Base):
    __tablename__ = 'aluno'
    id_aluno = Column(Integer, primary_key=True)
    alunos_id_user = Column(Integer, ForeignKey(
        'user.Id'), nullable=False, unique=True)

    # ONE TO MANY
    presencas = relationship('Presenca', backref='alunoDono')

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}



class Turma(Base):
    __tablename__ = 'turma'
    id_turma = Column(Integer, primary_key=True)
    id_responsavel = Column(Integer, ForeignKey('user.Id'), nullable=False)
    IsConcluido = Column(Boolean, nullable=False)
    nome_do_curso = Column(Text, nullable=False)
    carga_horaria_total = Column(Integer, nullable=False)
    tolerancia = Column(Integer, nullable=False)
    modalidade = Column(Text, nullable=False)
    turma_tag = Column(Text, nullable=True)

    # ONE TO MANY
    Horarios = relationship('Horario', backref="Turma")

    # MANY TO MANY
    Alunos = relationship('Aluno', secondary=alunoXturma,
                          backref=backref('MinhasTurmas', lazy='dynamic'))
    AlunosApoiadores = relationship(
        'AlunoApoiador', secondary=alunoApoiadoXturma, backref=backref('turmasApoiadas', lazy='dynamic'))

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Horario(Base):
    __tablename__ = 'horario'
    id_horario = Column(Integer, primary_key=True)
    HorarioIdTurma = Column(Integer, ForeignKey(
        'turma.id_turma'), nullable=False)
    DiaDaSemana = Column(String(20), nullable=False)
    HorarioInicio = Column(Time, nullable=False)
    HorarioTermino = Column(Time, nullable=False)


class AlunoApoiador(Base):
    __tablename__ = 'alunoApoiador'
    id_alunoApoiador = Column(Integer, primary_key=True)
    apoiador_id_turma = Column(Integer, ForeignKey(
        'turma.id_turma'), nullable=False)
    apoiador_id_user = Column(Integer, ForeignKey(
        'user.Id'), nullable=False, unique=True)


class Presenca(Base):
    __tablename__ = 'presenca'
    id_presenca = Column(Integer, primary_key=True)
    presenca_id_aluno = Column(Integer, ForeignKey('aluno.id_aluno'), nullable=False)
    presenca_id_turma = Column(Integer, ForeignKey('turma.id_turma'), nullable=False)
    CheckIn = Column(DateTime, nullable=True)
    presencaValidade = Column(Boolean, nullable=True)

class PresencaTot(Base):
    __tablename__ = 'presencatot'
    id_presencatot = Column(Integer, primary_key=True)
    presencatot_id_aluno = Column(Integer, ForeignKey('aluno.id_aluno'), nullable=False)
    presencatot_id_turma = Column(Integer, ForeignKey('turma.id_turma'), nullable=False)
    presenca_total = Column(Interval, nullable=False, default=timedelta(seconds=0))


class LinkCadastramento(Base):
    __tablename__ = 'link'
    token = Column(String(36), primary_key=True, default=str(uuid.uuid4()))
    link_id_turma = Column(Integer, ForeignKey('turma.id_turma'),
            nullable=False)
    validade = Column(DateTime,
            nullable=False,default=datetime.now()+timedelta(weeks=1))
    
    def as_dict(self):
        return {c.name:getattr(self,c.name) for c in self.__table__.columns}
