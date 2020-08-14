import sys

from database.session import get_session
from sqlalchemy.exc import InternalError
from database.model.Model import User
from utilities.loggers import get_logger
from werkzeug.security import generate_password_hash

#userDataFields = ["usuario", "email", "senha", "cpf", "telefone", "tipo", "funcao", "profissao", "UnidadeBasicadeSaude", "CAP"]

class AtualizarUserService:
    def execute(self, userData):
        logger = get_logger(sys.argv[0])
        try:
            session = get_session()
            user = session.query(User).filter(
                User.Id == userData['id']).first()


            if not user:
                return "Usuario nao encontrado", 400

            if(userData["usuario"].find(" ") != -1):
                return "Proibido uso de espaço no usuario", 400

            #Depois deixar bonito
            checarusuario = session.query(User).filter(
                User.usuario == userData['usuario']).first()

            if checarusuario:
                if (user.usuario.lower() != userData['usuario'].lower()):
                    return "nome de usuario ja em uso", 400

            checarcpf = session.query(User).filter(
                User.cpf == userData['cpf']).first()

            if checarcpf:
                if (user.cpf != userData['cpf']):
                    return "cpf ja em uso", 400

            checaremail = session.query(User).filter(
                User.email == userData['email']).first()

            if checaremail:
                if (user.email != userData['email']):
                    return "Email ja em uso", 400

            #atualizações começo
            if not(userData['usuario'] == ""):
                user.usuario = userData['usuario']

            if not(userData['email'] == ""):
                user.email = userData['email']

            if not(userData['senha'] == ""):
                userData["senha"] = generate_password_hash(userData["senha"])
                user.senha = userData['senha']

            if not(userData['cpf'] == ""):
                user.cpf = userData['cpf']

            if not(userData['telefone'] == ""):
                user.telefone = userData['telefone']

            if not(userData['tipo'] == ""):
                user.tipo = userData['tipo']

            if not(userData['funcao'] == ""):
                user.funcao = userData['funcao']

            if not(userData['profissao'] == ""):
                user.profissao = userData['profissao']

            if not(userData['UnidadeBasicadeSaude'] == ""):
                user.UnidadeBasicadeSaude = userData['UnidadeBasicadeSaude']

            if not(userData['CAP'] == ""):
                user.CAP = userData['CAP']

            session.commit()
            #atualizações fim

            userDict =  user.as_dict()
            #remove user password from return 
            userDict.pop("senha")

            return {**userDict}
        except InternalError:
            logger.error("Banco de dados (EdPermanente) desconhecido")
            return "502ERROR"

            user.name = 'New Name'
            db.session.commit()
