import sys

from utilities.loggers import get_logger
from sqlalchemy.exc import InternalError
from database.session import get_session
from sqlalchemy.exc import InternalError
from database.model.Model import Turma, Aula
from utilities.montaRelatorio import frequencia

def aula_info(aula):
    return {
        'id_aula': f'{aula.id_aula}',
        'nome_da_aula': f'{aula.nome_da_aula}'
    }


class ListAulaService:
    def execute(self, turmaData):
        logger = get_logger(sys.argv[0])
        try:
            session = get_session()
            QueryTurma = session.query(Turma).filter(Turma.nome_do_curso == turmaData["nome_do_curso"]).first()
            aulas = []
            if not QueryTurma:
                return {"Error":"Turma não encontrada"}, 400
            if not QueryTurma.Aulas:
                return {"Error":"A turma não possui nenhuma aula cadastrada"}, 400
            for i in QueryTurma.Aulas:
                aulas.append(aula_info(i))
            session.close()
            return aulas
        except InternalError:
            logger.error("Banco de dados (EdPermanente) desconhecido")
            return "502ERROR"
