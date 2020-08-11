from database.session import get_session
from sqlalchemy.exc import InternalError
from database.model.Model import *
from datetime import datetime

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
            return {"Success":"Aluno cadastrado na turma"}, 200 
        if TuplaUserTurma[0].Aluno in TuplaUserTurma[1].Alunos:
            return {"Error":"Aluno já cadastrado na turma"}, 502

        TuplaUserTurma[1].Alunos.append(TuplaUserTurma[0].Aluno)
        session.commit()
        session.close()

        return {"Success":"Aluno cadastrado na turma"}, 200

    #cadastroData=["cpf","token"]
    def executeAluno(self, cadastroData):
        session = get_session()

        TuplaLinkTurmaUser=session.query(LinkCadastramento,Turma,User).filter(LinkCadastramento.token==cadastroData['tokenTurma'],Turma.id_turma==LinkCadastramento.link_id_turma,User.cpf==cadastroData['cpf']).first()

        if not TuplaLinkTurmaUser:
            return {"Error":"Link não existe ou está expirado"}

        if datetime.now() > TuplaLinkTurmaUser[0].validade:
            session.delete(TuplaLinkTurmaUser[0])
            session.commit()
            session.close()
            return {"Error":"Link não existe ou está expirado"}


        if not(TuplaLinkTurmaUser[2].Aluno):
            aluno = Aluno(alunoUser=TuplaLinkTurmaUser[2])
            session.add(aluno)
            TuplaLinkTurmaUser[1].Alunos.append(aluno)
            session.commit()
            session.close()
            return {"Success":"Aluno cadastrado na turma"}, 200 
        if TuplaLinkTurmaUser[0].Aluno in TuplaLinkTurmaUser[1].Alunos:
            return {"Error":"Aluno já cadastrado na turma"}, 502

        alunos = TuplaLinkTurmaUser[1].Alunos
        alunos.append(TuplaLinkTurmaUser[2].Aluno)
        session.commit()
        session.close()
        return {"Success":"Aluno cadastrado"}

