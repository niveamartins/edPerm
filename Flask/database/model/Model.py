from sqlalchemy import Column, String, Integer,Text, Enum, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from database.model.Base.Base import Base

# ASSOCIATIONS TABLES
 
alunoApoiadoXturma = Table('aaxt',
    Column('alunoApoiador_id',Integer, ForeignKey('alunoApoiador.id_alunoApoiador')),
    Column('turma_id',Integer, ForeignKey('turma.id_turma'))
)

alunoXturma = Table('axt',
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
    UserComplemento = relationship('UserComplemento', uselist=False, backref="user")
    Aluno = relationship('Aluno', uselist=False, backref='aluno')
    AlunoApoiador = relationship('AlunoApoiador', uselist=False, backref='alunoApoiador')
    
    #ONE TO MANY
    Turma = relationship('Turma', backref='turma')

    def format(self):
        return {
          "id": f'{self.Id}',
          "nome": f'{self.usuario}',
          "email":f'{self.email}', 
          "telefone":f'{self.telefone}'
        }

class Aluno(Base):
    __tablename__ = 'aluno'
    id_aluno = Column(Integer,primary_key=True)
    alunos_id_turma = Column(Integer, ForeignKey('turma.id_turma'), nullable=False)
    alunos_id_user = Column(Integer, ForeignKey('user.Id'), nullable=False, unique=True)
    presenca = Column(Integer, nullable=False)

class Turma(Base):
    __tablename__ = 'turma'
    id_turma = Column(Integer,primary_key=True)
    id_responsavel = Column(Integer, ForeignKey('user.Id'), nullable=False)
    nome_do_curso = Column(String(50), nullable=False)
    carga_horaria_total = Column(Integer, nullable=False)
    tolerancia = Column(Integer, nullable=False)
    modalidade = Column(String, nullable=False)
    turma_tag = Column(String, nullable=False)

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
    tag = Column(String, nullable=False)
    profissao = Column(String, nullable=False)
    funcao = Column(String, nullable=False)
    superintendenciaDaSUBPAV = Column(String, nullable=False)
    CAP = Column(String, nullable=False)
    unidadeBasicaDeSaude = Column(String, nullable=False)

class AlunoApoiador(Base):
    __tablename__ = 'alunoApoiador'
    id_alunoApoiador = Column(Integer, primary_key=True)
    apoiador_id_turma = Column(Integer, ForeignKey('turma.id_turma'), nullable=False)
    apoiador_id_user = Column(Integer, ForeignKey('user.Id'), nullable=False, unique=True)
