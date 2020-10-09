import sys

from utilities.loggers import get_logger
from sqlalchemy.exc import InternalError
from database.session import get_session
from sqlalchemy.exc import InternalError
from database.model.Model import User


def usuario_info(user):
    adm = 'Não'
    gestor = 'Não'
    coordenador = 'Não'
    propositor = 'Não'
    cursista = 'Não'
    apoiador = 'Não'
    if(user.adm==1):
        adm = 'Sim'
    if(user.gestor==1):
        gestor = 'Sim'
    if(user.coordenador==1):
        coordenador = 'Sim'
    if(user.propositor==1):
        propositor = 'Sim'
    if(user.cursista==1):
        cursista = 'Sim'
    if(user.apoiador==1):
        apoiador = 'Sim'
    return {
        'Id': f'{user.Id}',
        'Nome': f'{user.nome}',
        'Usuario': f'{user.usuario}',
        'Adm': f'{adm}',
        'Gestor': f'{gestor}',
        'Coordenador': f'{coordenador}',
        'Propositor': f'{propositor}',
        'Cursista': f'{cursista}',
        'Apoiador': f'{apoiador}'
    }


class ListUserService:
    def execute(self):
        try:
            session = get_session()
            data = session.query(User).all()
            usuarios = [usuario_info(i) for i in data]
            session.close()
            return usuarios
        except InternalError:
            return "502ERROR"
