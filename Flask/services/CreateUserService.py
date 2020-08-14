import sys

from database.session import get_session
from sqlalchemy.exc import InternalError
from database.model.Model import User
from utilities.loggers import get_logger
from werkzeug.security import generate_password_hash

#userDataFields = ["usuario", "email", "senha", "cpf", "telefone", "tipo", "funcao", "profissao", "UnidadeBasicadeSaude", "CAP"]

class CreateUserService:
    def execute(self, userData):
        logger = get_logger(sys.argv[0])
        try:
            session = get_session()
            userAlreadyExists = session.query(User).filter(
                User.usuario == userData['usuario']).first()

            

            if userAlreadyExists:
                return "User Already Exists", 400

            #Depois deixar bonito
            checarcpf = session.query(User).filter(
                User.cpf == userData['cpf']).first()

            if checarcpf:
                return "cpf ja em uso", 400

            userData["senha"] = generate_password_hash(userData["senha"])

            if(userData["usuario"].find(" ") != -1):
                return "Proibido uso de espaço no usuario", 400

            user = User(usuario=userData["usuario"], email=userData["email"], senha=userData["senha"],
                        cpf=userData["cpf"], telefone=userData["telefone"], tipo=userData["tipo"], funcao=userData["funcao"],
                        profissao=userData["profissao"], UnidadeBasicadeSaude=userData["UnidadeBasicadeSaude"], CAP=userData["CAP"])
            session.add(user)
            session.commit()

            userDict =  user.as_dict()
            #remove user password from return 
            userDict.pop("senha")

            return {**userDict}
        except InternalError:
            logger.error("Banco de dados (EdPermanente) desconhecido")
            return "502ERROR"
