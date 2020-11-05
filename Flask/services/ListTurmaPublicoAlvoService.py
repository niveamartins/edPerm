import sys

from utilities.loggers import get_logger
from sqlalchemy.exc import InternalError
from database.session import get_session
from sqlalchemy.exc import InternalError
from database.model.Model import User, Turma, Aluno, alunoXturma, publicoAlvoXturma, PublicoAlvo
from utilities.montaRelatorio import frequencia

def ListPublicoAlvo(publicoAlvo):
    return {
        'nome_publicoAlvo': f'{publicoAlvo.nome_publicoAlvo}'
    }	


class ListTurmaPublicoAlvoService:
    def execute(self, turma):
        logger = get_logger(sys.argv[0])
        try:
            session = get_session()
            QueryTurma = session.query(Turma).filter(Turma.nome_do_curso == turma["nome_do_curso"]).first()
            PublicoAlvos = []
            for i in QueryTurma.PublicosAlvo:
                PublicoAlvos.append(ListPublicoAlvo(i))
            session.close()
            return PublicoAlvos
        except InternalError:
            logger.error("Banco de dados (EdPermanente) desconhecido")
            return "502ERROR"
