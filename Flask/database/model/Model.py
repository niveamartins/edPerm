from sqlalchemy import (Column, String, Integer, Text,
                        Enum, ForeignKey, Table, Time, Boolean, DateTime, Interval)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from database.model.Base.Base import Base
from datetime import datetime,timedelta
import uuid


# MODELS

class User(Base):
    __tablename__ = 'user'
#Infos pessoais
    Id = Column(Integer, primary_key=True)
    nome = Column(Text, nullable=False)
    usuario = Column(Text, nullable=False)
    email = Column(Text, nullable=False)
    senha = Column(Text, nullable=False)
    cpf = Column(String(11), nullable=False)
    telefone = Column(String(9), nullable=False)
#Infos de uso
    adm = Column(Boolean, nullable=False)
    gestor = Column(Boolean, nullable=False)
    coordenador = Column(Boolean, nullable=False)
    propositor = Column(Boolean, nullable=False)
    cursista = Column(Boolean, nullable=False)
    apoiador = Column(Boolean, nullable=False)
#Infos da prefeitura
    funcao = Column(Text,nullable=True)
    profissao = Column(Text,nullable=True)
    UnidadeBasicadeSaude=Column(Text,nullable=True)
    CAP=Column(Text,nullable=True)

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

    # ONE TO ONE
    presencatot = relationship('PresencaTot', backref='alunoDono')

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
    Alunos = relationship('Aluno', secondary='axt',
                          backref=backref('MinhasTurmas', lazy='dynamic'))
    AlunosApoiadores = relationship(
        'AlunoApoiador', secondary='aaxt', backref=backref('turmasApoiadas', lazy='dynamic'))

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

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class AlunoApoiador(Base):
    __tablename__ = 'alunoApoiador'
    id_alunoApoiador = Column(Integer, primary_key=True)
    apoiador_id_user = Column(Integer, ForeignKey(
        'user.Id'), nullable=False, unique=True)

#Tabelas de associação


class alunoXturma(Base):
    __tablename__ = 'axt'
    axt_id = Column(Integer, primary_key=True)
    axt_alunoid = Column(Integer, ForeignKey(
        'aluno.id_aluno'), nullable=False)
    axt_turmaid = Column(Integer, ForeignKey(
        'turma.id_turma'), nullable=False, unique=True)


class alunoApoiadoXturma(Base):
    __tablename__ = 'aaxt'
    aaxt_id = Column(Integer, primary_key=True)
    aaxt_apoiadorid = Column(Integer, ForeignKey(
        'alunoApoiador.id_alunoApoiador'), nullable=False)
    aaxt_turmaid = Column(Integer, ForeignKey(
        'turma.id_turma'), nullable=False, unique=True)



class Presenca(Base):
    __tablename__ = 'presenca'
    id_presenca = Column(Integer, primary_key=True)
    presenca_id_aluno = Column(Integer, ForeignKey('aluno.id_aluno'), nullable=False)
    presenca_id_turma = Column(Integer, ForeignKey('turma.id_turma'), nullable=False)
    CheckIn = Column(DateTime, nullable=True)
    presencaValidade = Column(Boolean, nullable=True)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


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
