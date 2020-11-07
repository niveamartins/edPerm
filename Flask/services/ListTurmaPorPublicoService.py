import sys

from utilities.loggers import get_logger
from sqlalchemy.exc import InternalError
from database.session import get_session
from sqlalchemy.exc import InternalError
from database.model.Model import *
from utilities.montaRelatorio import frequencia


def turma_info(turma):
    return {
        'nomeDoPropositor': f'{turma.propositor.usuario}',
        'id_turma': f'{turma.id_turma}',
        'nome_do_curso': f'{turma.nome_do_curso}',
        'id_do_responsavel': f'{turma.id_responsavel}',
        'Carga_Horaria_Total': f'{turma.carga_horaria_total}'
    }


class ListTurmaPorPublicoService:
    def execute(self,userData):
        logger = get_logger(sys.argv[0])
        try:
            session = get_session()
            QueryAluno = session.query(User).filter(User.Id == userData["Id"]).first()
            QueryPublicoAlvo = session.query(PublicoAlvo).filter(PublicoAlvo.nome_publicoAlvo == QueryAluno.profissao).first()
            if(QueryPublicoAlvo):
                turmas = [turma_info(i) for i in QueryPublicoAlvo.turmasPublicoAlvo]
            else:
                turmas = {"Error":"Não encontramos nenhuma turma."}, 400
            session.close()
            return turmas
        except InternalError:
            logger.error("Banco de dados (EdPermanente) desconhecido")
            return "502ERROR"
