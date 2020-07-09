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

            userQuery = session.query(User).filter_by(usuario = usuario).first()
            if not userQuery or not check_password_hash(userQuery.as_dict()["senha"], senha):
                return {"Error":"Usuario ou senha incorretos."}, 400
            user = userQuery.as_dict()
            user = {
                "id": user["Id"],
                "usuario": user["usuario"]
            }
            expires = timedelta(hours=24)
            access_token = create_access_token(identity=user, expires_delta=expires)
            response= {"access_token":access_token}
            return response

        except InternalError:
            logger.error("Banco de dados (EdPermanente) desconhecido")
            return "502ERROR"