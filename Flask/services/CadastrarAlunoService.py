import sys

from database.session import get_session
from sqlalchemy.exc import InternalError
from database.model.Model import *
from utilities.loggers import get_logger

#cadastro data = {["cpf", "id_do_curso"]}

class CadastrarAlunoService:
    def execute(self, cadastroData):
        logger = get_logger(sys.argv[0])
       # try:
        session = get_session()
        TuplaUserTurma = session.query(User,Turma).filter(User.cpf == cadastroData["cpf"], Turma.id_turma == cadastroData["id_do_curso"]).first()
        
        if not TuplaUserTurma:
            return {"Error":"Cpf invalido"}, 502

        TuplaUserTurma[1].Alunos.append(TuplaUserTurma[0].Aluno)
        session.commit()
        session.close()

        return {"Sucess":"Aluno cadastrado na turma"}, 200
