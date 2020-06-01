import sys

from database.session import get_session
from sqlalchemy.exc import InternalError
from database.model.Model import *
from utilities.loggers import get_logger

#Não testado a parte dos Json

class CreateTurmaService:
    def execute(self, turmaData):
        logger = get_logger(sys.argv[0])
        #Permito cadastrar 2 turmas com mesmo nome
        #Pois a mesma turma pode ser lançada em momentos diferentes
        #Isso pode gerar um problema, perguntar para secretaria
        try:
            session = get_session()
            busca = session.query(User).filter_by(usuario=turmaData['responsavel']).first()
            if (busca != None):
                cadastrar = Turma(id_responsavel = busca.Id, IsConcluido = False, nome_do_curso = turmaData['nome_do_curso'] ,carga_horaria_total = turmaData['carga_horaria_total'], tolerancia = turmaData['tolerancia'], modalidade = turmaData['modalidade'], turma_tag = turmaData['turma_tag'])
                session.add_all([cadastrar])
                session.commit()
                return cadastrar.as_dict()
            else:
                return "Responsavel não cadastrado", 400
        except InternalError:
            logger.error("Banco de dados (EdPermanente) desconhecido")
            return "502ERROR"
