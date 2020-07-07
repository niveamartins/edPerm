from sqlalchemy import desc
from database.session import get_session
from database.model.Model import Presenca
from datetime import datetime
class CreatePresencaService:
    def execute(self, presencaData):
        session = get_session()

        presencaCheck = session.query(Presenca).filter_by(presenca_id_aluno=presencaData["idAluno"],presenca_id_turma=presencaData["idTurma"],presencaValidade=0).order_by(desc(Presenca.id_presenca)).first()

        if presencaCheck and presencaCheck.CheckIn.date() == datetime.now().date():
            return {"Error":"Presença já foi registrada"}

        presenca =  Presenca(presenca_id_aluno=presencaData["idAluno"],presenca_id_turma=presencaData["idTurma"],CheckIn=datetime.now(),presencaValidade=0)
        session.add(presenca)
        session.commit()
        session.close()
        return {"Sucess":"Presenca cadastrada"}
