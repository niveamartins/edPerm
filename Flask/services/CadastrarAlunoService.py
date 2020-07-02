from database.session import get_session
from sqlalchemy.exc import InternalError
from database.model.Model import *


#cadastro data = {["cpfAluno", "idTurma","id"]}

class CadastrarAlunoService:
    def execute(self, cadastroData):
        session = get_session()
        TuplaUserTurma = session.query(User,Turma).filter(User.Id==cadastroData["id"],User.cpf==cadastroData["cpfAluno"],Turma.id_turma==cadastroData["idTurma"]).first()
        
        if not TuplaUserTurma:
            return {"Error":"Usuário invalido"}, 502

        if not(TuplaUserTurma[0].Aluno):
            aluno = Aluno(alunoUser=TuplaUserTurma[0])
            session.add(aluno)
            TuplaUserTurma[1].Alunos.append(aluno)
            session.commit()
            session.close()
            return {"Sucess":"Aluno cadastrado na turma"}, 200
      
        if TuplaUserTurma[0].Aluno in TuplaUserTurma[1].Alunos:
            return {"Error":"Aluno já cadastrado na turma"}, 502

        TuplaUserTurma[1].Alunos.append(TuplaUserTurma[0].Aluno)
        session.commit()
        session.close()

        return {"Sucess":"Aluno cadastrado na turma"}, 200
