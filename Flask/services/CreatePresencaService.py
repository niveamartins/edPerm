from sqlalchemy import desc
from database.session import get_session
from database.model.Model import Presenca, PresencaTot,User, Aluno
from datetime import datetime, timedelta
class CreatePresencaService:
    def execute(self, presencaData):
        session = get_session()

        Usercheck = session.query(User).filter_by(email=presencaData['emailAluno']).first()

        presenca =  Presenca(presenca_id_aluno= Usercheck.Aluno.id_aluno,presenca_id_turma=presencaData["idTurma"],CheckIn=datetime.now(),presencaValidade=1)
        
        if not Usercheck.Aluno.presencatot:
            a = PresencaTot(presencatot_id_aluno=Usercheck.Aluno.id_aluno,presencatot_id_turma=presencaData["idTurma"],presenca_total=timedelta(hours=int(presencaData['Horas'])))
            session.add(a)
        else:
            b = session.query(Aluno).filter_by(alunos_id_user=Usercheck.Id).first()
            c = b.presencatot.presencatotal + timedelta(hours=int(presencaData['Horas']))
            print(c)
            b.presencatot.presencatotal= b.presencatot.presencatotal + timedelta(hours=int(presencaData['Horas']))
        
        session.add(presenca)
        session.commit()
        session.close()
        return {"Sucess":"Presenca cadastrada"}
