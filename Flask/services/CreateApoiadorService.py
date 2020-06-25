import sys

from database.session import get_session
from sqlalchemy.exc import InternalError
from database.model.Model import *
from utilities.loggers import get_logger

#cadastro data = {["email_apoiador", "id_turma"]}

class CreateApoiadorService:
    def execute(self, cadastroData):
        logger = get_logger(sys.argv[0])
       # try:
        session = get_session()
        TuplaUserTurma = session.query(User,Turma).filter(User.email == cadastroData["email_apoiador"], Turma.id_turma == cadastroData["id_turma"]).first()
        
        if not TuplaUserTurma:
            return {"Error":"Email invalido"}, 502

        apoiador = AlunoApoiador(apoiador_id_turma=TuplaUserTurma[1].id_turma,apoiador_id_user=TuplaUserTurma[0].Id)
        session.add(apoiador)
        TuplaUserTurma[1].AlunosApoiadores.append(apoiador)
        session.commit()
        session.close()

        return {"Sucess":"Aluno Apoiador cadastrado"}, 200
