import sys

from utilities.loggers import get_logger
from sqlalchemy.exc import InternalError
from database.session import get_session
from sqlalchemy.exc import InternalError
from database.model.Model import User, Turma, Aluno, alunoXturma
from utilities.montaRelatorio import frequencia


def turma_info(turma):
    return {
        'nomeDoPropositor': f'{turma.propositor.usuario}',
        'id_turma': f'{turma.id_turma}',
        'nome_do_curso': f'{turma.nome_do_curso}',
        'id_do_responsavel': f'{turma.id_responsavel}',
        'Carga_Horaria_Total': f'{turma.carga_horaria_total}'
    }


class ListTurmaService:
    def execute(self):
        logger = get_logger(sys.argv[0])
        try:
            session = get_session()
            data = session.query(Turma).all()
            turmas = [turma_info(i) for i in data]
            #data = session.query(Aluno).filter(
             #   Aluno.alunos_id_user == user_id)
            #turmas = []
            #for row in data:
            #    for turma in row.MinhasTurmas:
            #        turmas.append(turma_info(turma))
            session.close()
            return turmas
        except InternalError:
            logger.error("Banco de dados (EdPermanente) desconhecido")
            return "502ERROR"
