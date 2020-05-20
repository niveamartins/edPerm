import sys

from database.session import get_session
from sqlalchemy.exc import InternalError
from database.model.Model import *
from utilities.loggers import get_logger
from werkzeug.security import generate_password_hash


class CreateUserService:
    def execute(self, userData):
        logger = get_logger(sys.argv[0])
        try:
            session = get_session()
            userAlreadyExists = session.query(User).filter(
                User.usuario == userData['usuario']).first()

            if userAlreadyExists:
                return "User Already Exists", 400

            userData["senha"] = generate_password_hash(userData["senha"])

            user = User(usuario=userData["usuario"], email=userData["email"], senha=userData["senha"],
                        cpf=userData["cpf"], telefone=userData["telefone"], tipo=userData["tipo"])
            session.add(user)
            session.commit()
            return user.as_dict()
        except InternalError:
            logger.error("Banco de dados (EdPermanente) desconhecido")
            return "502ERROR"
