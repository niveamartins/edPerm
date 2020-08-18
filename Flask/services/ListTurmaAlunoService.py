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


class ListTurmaAlunoService:
    def execute(self, apoiadorData):
        logger = get_logger(sys.argv[0])
        try:
            session = get_session()
            QueryUsuario = session.query(User).filter(User.usuario == apoiadorData["usuario"]).first()
            if not QueryUsuario:
                return {"Error":"Usuario não cadastrado"}, 502
            if not QueryUsuario.Aluno:
                return {"Error":"Usuario não está inscrito em nenhuma turma"}, 502
            data = session.query(Turma).all()
            turmas = []
            for i in data:
                if(QueryUsuario.Aluno in i.Alunos):
                    turmas.append(turma_info(i))
            session.close()
            return turmas
        except InternalError:
            logger.error("Banco de dados (EdPermanente) desconhecido")
            return "502ERROR"
