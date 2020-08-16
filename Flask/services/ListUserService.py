import sys

from utilities.loggers import get_logger
from sqlalchemy.exc import InternalError
from database.session import get_session
from sqlalchemy.exc import InternalError
from database.model.Model import User


def usuario_info(user):
    return {
        'Id': f'{user.Id}',
        'usuario': f'{user.usuario}',
        'tipo': f'{user.tipo}'
    }


class ListUserService:
    def execute(self):
        logger = get_logger(sys.argv[0])
        try:
            session = get_session()
            data = session.query(User).all()
            usuarios = [usuario_info(i) for i in data]
            session.close()
            return usuarios
        except InternalError:
            logger.error("Banco de dados (EdPermanente) desconhecido")
            return "502ERROR"
