from sqlalchemy import Column, String, Integer,Text, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from BD.model.Base.Base import Base
#TODO: estudar e implementar relationships
class User(Base):
    __tablename__ = 'User'
    Id       = Column(Integer,primary_key=True)
    usuario  = Column(Text, nullable=False)
    email    = Column(Text, nullable=False)
    senha    = Column(Text, nullable=False)
    cpf      = Column(String(11), nullable=False)
    telefone = Column(String(10), nullable=False)
    tipo     = Column(Enum(['adm','gestor','coordenador','propositor','cursista','apoiador']), nullable=False)

    def format(self,dic):
        aux = {}

        aux[self.Id]= {
          'nome' = self.nome
          'email' = self.email 
          'telefone' = self.telefone
        } 
        return dic.append(aux)