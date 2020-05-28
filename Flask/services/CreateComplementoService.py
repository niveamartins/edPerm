import sys

from database.session import get_session
from sqlalchemy.exc import InternalError
from database.model.Model import *
from utilities.loggers import get_logger



class CreateComplementoService:
    def execute(self, complementoData):
        #logger = get_logger(sys.argv[0])
        #Pois a mesma turma pode ser lançada em momentos diferentes
        #complementoData = {"usuario":usuarioDoUser, "tag":tagDoComplemento, "profissao":profissaoDoComplemento, "funcao":funcaoDoComplemento, "superintendenciaDaSUBPAV":superentendenciaDoComplemento, "CAP":capDoComplemento, "unidadeBasicaDeSaude":unidadeDoComplemento}


        try:
            session = get_session()
            busca = session.query(User).filter_by(usuario=complementoData['usuario']).first()
            if (busca != None):
                busca2 = session.query(UserComplemento).filter_by(id_do_user=busca.Id).first()
                if (busca2 == None):
                    #Criar
                    cadastrar = UserComplemento(id_do_user = busca.Id, tag = complementoData['tag'], profissao = complementoData['profissao'], funcao = complementoData['funcao'], superintendenciaDaSUBPAV = complementoData['superintendenciaDaSUBPAV'], CAP = complementoData['CAP'], unidadeBasicaDeSaude = complementoData['unidadeBasicaDeSaude'])
                    session.add_all([cadastrar])
                    session.commit()
                    #return cadastrar.as_dict()
                    return "Dados complementares adicionados"

                else:
                    #Atualizar
                    busca2.tag = complementoData['tag']
                    busca2.profissao = complementoData['profissao']
                    busca2.funcao = complementoData['funcao']
                    busca2.superintendenciaDaSUBPAV = complementoData['superintendenciaDaSUBPAV']
                    busca2.CAP = complementoData['CAP']
                    busca2.unidadeBasicaDeSaude = complementoData['unidadeBasicaDeSaude']
                    session.commit()
                    #return cadastrar.as_dict()
                    return "Dados atualizados"

            else:
                #Não existe o usuario
                return "Usuario não cadastrado", 400
        except InternalError:
            logger.error("Banco de dados (EdPermanente) desconhecido")
            return "502ERROR"


