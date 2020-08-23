import sys

from database.session import get_session
from sqlalchemy.exc import InternalError
from database.model.Model import *
from utilities.loggers import get_logger

#deleteDataFields = ["cpfApoiador", "idTurma", "idDoPropositor"]

class DeleteApoiadorService:
    def execute(self, deleteData):
        logger = get_logger(sys.argv[0])
        try:
            session = get_session()
            TuplaUserTurma = session.query(User,Turma).filter(User.cpf == deleteData["cpfApoiador"], Turma.id_turma == deleteData["idTurma"]).first()

            if not (TuplaUserTurma[1].id_responsavel == deleteData['idDoPropositor']):
                return {"Error":"Você não tem permissão para deletar um apoiador dessa turma"}, 400

            if not TuplaUserTurma:
                return "Usuario nao encontrado", 400

            if not (TuplaUserTurma[0].AlunoApoiador in TuplaUserTurma[1].AlunosApoiadores):
                return "Usuario não é apoiador da turma", 400

            apoiador = session.query(alunoApoiadoXturma).filter(alunoApoiadoXturma.aaxt_apoiadorid == TuplaUserTurma[0].AlunoApoiador.id_alunoApoiador,
            alunoApoiadoXturma.aaxt_turmaid == TuplaUserTurma[1].id_turma).first()
            session.delete(apoiador)
            session.commit()


            return "Apoiador removido da turma com sucesso"
        except InternalError:
            logger.error("Banco de dados (EdPermanente) desconhecido")
            return "502ERROR"
