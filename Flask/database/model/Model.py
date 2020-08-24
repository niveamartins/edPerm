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
    presencatotal = relationship('PresencaTotal', backref='alunoDono')

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
    Aulas = relationship('Aula', backref="Turma")

    # MANY TO MANY
    Alunos = relationship('Aluno', secondary='axt',
                          backref=backref('MinhasTurmas', lazy='dynamic'))
    AlunosApoiadores = relationship(
        'AlunoApoiador', secondary='aaxt', backref=backref('turmasApoiadas', lazy='dynamic'))

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


class Aula(Base):
    __tablename__ = 'aula'
    id_aula = Column(Integer, primary_key=True)
    nome_da_aula = Column(Text, nullable=False)
    aula_id_turma = Column(Integer, ForeignKey('turma.id_turma'), nullable=False)
    hora_de_inicio = Column(DateTime, nullable=False)
    hora_de_termino = Column(DateTime, nullable=False)


class Presenca(Base):
    __tablename__ = 'presenca'
    id_presenca = Column(Integer, primary_key=True)
    presenca_id_aluno = Column(Integer, ForeignKey('aluno.id_aluno'), nullable=False)
    presenca_id_aula = Column(Integer, ForeignKey('aula.id_aula'), nullable=False)
    CheckIn = Column(DateTime, nullable=True)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class PresencaTotal(Base):
    __tablename__ = 'presencatotal'
    id_presencatotal = Column(Integer, primary_key=True)
    presencatotal_id_aluno = Column(Integer, ForeignKey('aluno.id_aluno'), nullable=False)
    presencatotal_id_turma = Column(Integer, ForeignKey('turma.id_turma'), nullable=False)
    numero_de_presencas = Column(Integer, nullable=False)
    horas = Column(Integer, nullable=False)
    minutos = Column(Integer, nullable=False)
    segundos = Column(Integer, nullable=False)


class LinkCadastramento(Base):
    __tablename__ = 'link'
    token = Column(String(36), primary_key=True, default=str(uuid.uuid4()))
    link_id_turma = Column(Integer, ForeignKey('turma.id_turma'),
            nullable=False)
    validade = Column(DateTime,
            nullable=False,default=datetime.now()+timedelta(weeks=1))
    
    def as_dict(self):
        return {c.name:getattr(self,c.name) for c in self.__table__.columns}
