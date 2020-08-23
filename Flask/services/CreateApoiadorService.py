import sys

from database.session import get_session
from sqlalchemy.exc import InternalError
from database.model.Model import *
from utilities.loggers import get_logger

#cadastro data = {["email_apoiador", "id_turma", idDoPropositor]}

class CreateApoiadorService:
    def execute(self, cadastroData):
        logger = get_logger(sys.argv[0])
       # try:
        session = get_session()
        TuplaUserTurma = session.query(User,Turma).filter(User.email == cadastroData["email_apoiador"], Turma.id_turma == cadastroData["id_turma"]).first()
        
        if not TuplaUserTurma:
            return {"Error":"Email invalido"}, 400

        if not (TuplaUserTurma[1].id_responsavel == cadastroData['idDoPropositor']):
            return {"Error":"Você não tem permissão para cadastrar um apoiador nessa turma"}, 400
        
        if not (TuplaUserTurma[0].AlunoApoiador):
            apoiador = AlunoApoiador(apoiador_id_user=TuplaUserTurma[0].Id)
            session.add(apoiador)
        else:
            apoiador = TuplaUserTurma[0].AlunoApoiador

        if (apoiador in TuplaUserTurma[1].AlunosApoiadores):
            return {"Error":"Usuario ja é apoiador desta turma!"}, 400
        TuplaUserTurma[1].AlunosApoiadores.append(apoiador)
        session.commit()
        session.close()

        return {"Sucess":"Aluno Apoiador cadastrado"}, 200
