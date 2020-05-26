from sqlalchemy import Column, String, Integer,Text, Enum, ForeignKey, Table, Time, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from database.model.Base.Base import Base

# ASSOCIATIONS TABLES
 
alunoApoiadoXturma = Table('aaxt', Base.metadata,
    Column('alunoApoiador_id',Integer, ForeignKey('alunoApoiador.id_alunoApoiador')),
    Column('turma_id',Integer, ForeignKey('turma.id_turma'))
)

alunoXturma = Table('axt', Base.metadata,
    Column('aluno_id',Integer, ForeignKey('aluno.id_aluno')),
    Column('turma_id',Integer, ForeignKey('turma.id_turma'))
)



# MODELS

class User(Base):
    __tablename__ = 'user'
    Id       = Column(Integer,primary_key=True)
    usuario  = Column(Text, nullable=False)
    email    = Column(Text, nullable=False)
    senha    = Column(Text, nullable=False)
    cpf      = Column(String(11), nullable=False)
    telefone = Column(String(9), nullable=False)
    tipo     = Column(Enum('adm','gestor','coordenador','propositor','cursista','apoiador'), nullable=False)

    #ONE TO ONE
    
    Aluno = relationship('Aluno', uselist=False, backref='alunoUser')
    AlunoApoiador = relationship('AlunoApoiador', uselist=False, backref='alunoApoiadorUser')
    
    
    #ONE TO MANY
    TurmaProposta = relationship('Turma', backref='propositor')

class Aluno(Base):
    __tablename__ = 'aluno'
    id_aluno = Column(Integer,primary_key=True)
    alunos_id_user = Column(Integer, ForeignKey('user.Id'), nullable=False, unique=True)
    alunos_id_complemento = Column(Integer, ForeignKey('userComplemento.id_complemento'), nullable=False, unique=True)

    #ONE TO ONE
    complementoUser = relationship('UserComplemento', uselist=False, backref="AlunocomplementoUser")

class Turma(Base):
    __tablename__ = 'turma'
    id_turma = Column(Integer,primary_key=True)
    id_responsavel = Column(Integer, ForeignKey('user.Id'), nullable=False)
    IsConcluido = Column(Boolean, nullable=False)
    nome_do_curso = Column(String(30), nullable=False)
    carga_horaria_total = Column(Integer, nullable=False)
    tolerancia = Column(Integer, nullable=False)
    modalidade = Column(String(20), nullable=False)
    turma_tag = Column(String(20), nullable=False)

    #ONE TO MANY
    Horarios = relationship('Horario', backref="Horarios")

    #MANY TO MANY
    Alunos = relationship('Aluno',secondary=alunoXturma, backref=backref('MinhasTurmas', lazy='dynamic'))
    AlunosApoiadores = relationship('AlunoApoiador', secondary=alunoApoiadoXturma, backref=backref('turmasApoiadas', lazy='dynamic'))


class Horario(Base):
    __tablename__ = 'horario'
    id_horario = Column(Integer, primary_key=True)
    HorarioIdTurma = Column(Integer, ForeignKey('turma.id_turma'), nullable=False)
    DiaDaSemana = Column(String(20), nullable=False)
    HorarioInicio = Column(Time, nullable=False)
    HorarioTermino = Column(Time, nullable=False)

class UserComplemento(Base):
    __tablename__ = 'userComplemento'
    id_complemento = Column(Integer, primary_key=True)
    id_do_user = Column(Integer, ForeignKey('user.Id'), nullable=False, unique=True)
    tag = Column(String(20), nullable=False)
    profissao = Column(String(20), nullable=False)
    funcao = Column(String(20), nullable=False)
    superintendenciaDaSUBPAV = Column(String(30), nullable=False)
    CAP = Column(String(20), nullable=False)
    unidadeBasicaDeSaude = Column(String(30), nullable=False)

    user = relationship('User', uselist=False, backref="complementoUser",foreign_keys=id_do_user)

class AlunoApoiador(Base):
    __tablename__ = 'alunoApoiador'
    id_alunoApoiador = Column(Integer, primary_key=True)
    apoiador_id_turma = Column(Integer, ForeignKey('turma.id_turma'), nullable=False)
    apoiador_id_user = Column(Integer, ForeignKey('user.Id'), nullable=False, unique=True)


class Presenca(Base):
    __tablename__ = 'presenca'
    id_presenca = Column(Integer, primary_key=True)
    presenca_id_aluno = Column(Integer, ForeignKey('aluno.id_aluno'), nullable=False)
    presenca_id_turma = Column(Integer, ForeignKey('turma.id_turma'), nullable=False)
    presencaNaTurma = Column(Integer, nullable=False)