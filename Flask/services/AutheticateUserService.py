import sys

from database.session import get_session
from sqlalchemy.exc import InternalError
from database.model.Model import User
from utilities.loggers import get_logger
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash
from datetime import timedelta


class AutheticateUserService:
    def execute(self, usuario, senha):
        logger = get_logger(sys.argv[0])
        try:
            session = get_session()

            user = session.query(User).filter_by(usuario = usuario).first().as_dict()

            if not user or not check_password_hash(user["senha"], senha):
                return "Usuario ou senha incorretos.", 400
            user = {
                "id": user["Id"],
                "usuario": user["usuario"]
            }
            expires = timedelta(hours=24)
            access_token = create_access_token(identity=user, expires_delta=expires)

            return access_token

        except InternalError:
            logger.error("Banco de dados (EdPermanente) desconhecido")
            return "502ERROR"
