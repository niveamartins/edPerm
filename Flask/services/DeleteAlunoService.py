import sys

from database.session import get_session
from sqlalchemy.exc import InternalError
from database.model.Model import *
from utilities.loggers import get_logger

#deleteDataFields = ["cpfAluno", "idTurma", "idDoPropositor"]

class DeleteAlunoService:
    def execute(self, deleteData):
        logger = get_logger(sys.argv[0])
        try:
            session = get_session()
            TuplaUserTurma = session.query(User,Turma).filter(User.cpf == deleteData["cpfAluno"], Turma.id_turma == deleteData["idTurma"]).first()

            if not (TuplaUserTurma[1].id_responsavel == deleteData['idDoPropositor']):
                return {"Error":"Você não tem permissão para deletar um aluno dessa turma"}, 400

            if not TuplaUserTurma:
                return {"Error":"Usuario nao encontrado"}, 400

            if not (TuplaUserTurma[0].Aluno in TuplaUserTurma[1].Alunos):
                return {"Error":"Usuario não é aluno da turma"}, 400


            apoiador = session.query(alunoXturma).filter(alunoXturma.axt_alunoid == TuplaUserTurma[0].Aluno.id_aluno,
            alunoXturma.axt_turmaid == TuplaUserTurma[1].id_turma).first()
            session.delete(apoiador)
            session.commit()


            return {"msg":"Aluno removido da turma com sucesso"}, 200
        except InternalError:
            logger.error("Banco de dados (EdPermanente) desconhecido")
            return "502ERROR"
