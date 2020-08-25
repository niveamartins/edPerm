from sqlalchemy import desc
from database.session import get_session
from database.model.Model import Presenca, PresencaTotal,User, Aluno, Aula,Turma
from datetime import datetime, timedelta

#presencaDataFields = ["emailAluno","id_aula"]

class CreatePresencaService:
    def execute(self, presencaData):
        session = get_session()

        TuplaUserAula = session.query(User,Aula).filter(User.email == presencaData["emailAluno"], Aula.id_aula == presencaData["id_aula"]).first()

        if not TuplaUserAula:
            return {"Error":"Usuario ou Aula não encontrado"}, 400

        if not TuplaUserAula[0].Aluno:
            return {"Error":"Usuario não é aluno"}, 400

        QueryTurma = session.query(Turma).filter_by(id_turma=TuplaUserAula[1].aula_id_turma).first()

        if not (TuplaUserAula[0].Aluno in QueryTurma.Alunos):
            return {"Error":"Usuario não é aluno da turma"}, 400

        QueryPresenca = session.query(Presenca).filter_by(presenca_id_aluno=TuplaUserAula[0].Aluno.id_aluno,
        presenca_id_aula=TuplaUserAula[1].id_aula).first()

        if QueryPresenca:
            return {"Error":"Usuario já recebeu presenca nessa aula"}, 400

        if(datetime.now() < TuplaUserAula[1].hora_de_inicio):
            return {"Error":"Aula ainda não começou"}, 400

        if(datetime.now() > TuplaUserAula[1].hora_de_termino):
            return {"Error":"Aula já terminou"}, 400

        presenca =  Presenca(presenca_id_aluno= TuplaUserAula[0].Aluno.id_aluno,presenca_id_aula=TuplaUserAula[1].id_aula,CheckIn=datetime.now())
   
        session.add(presenca)
        session.commit()

        if not(TuplaUserAula[0].Aluno.presencatotal):
            presencatotal = PresencaTotal(presencatotal_id_aluno=TuplaUserAula[0].Aluno.id_aluno, presencatotal_id_turma=QueryTurma.id_turma,
            numero_de_presencas=0, horas=0, minutos=0, segundos=0)
            session.add(presencatotal)
            session.commit()

        QueryPresencatotal = session.query(PresencaTotal).filter_by(presencatotal_id_aluno=TuplaUserAula[0].Aluno.id_aluno,
        presencatotal_id_turma=QueryTurma.id_turma).first()

        
        if not QueryPresencatotal:
            return {"Error":"Error inesperado, contate o suporte"}, 400


        totaldapresenca = (TuplaUserAula[1].hora_de_termino - datetime.now()).total_seconds()
        totaldapresenca = int(totaldapresenca)
        segundostotal = totaldapresenca%60
        minutostotal = int((totaldapresenca - segundostotal)/60)
        segundostotal = QueryPresencatotal.segundos + segundostotal
        if(segundostotal >= 60):
            segundostotal = segundostotal - 60
            minutostotal = minutostotal + 1

        horastotal = minutostotal
        minutostotal = minutostotal%60
        horastotal = int((horastotal - minutostotal)/60)
        minutostotal = minutostotal + QueryPresencatotal.minutos

        if(minutostotal >= 60):
            minutostotal = minutostotal - 60
            horastotal = horastotal + 1
        horastotal = horastotal + QueryPresencatotal.horas

        QueryPresencatotal.numero_de_presencas = QueryPresencatotal.numero_de_presencas + 1
 

        QueryPresencatotal.segundos = int(segundostotal)

        QueryPresencatotal.minutos = int(minutostotal)

        QueryPresencatotal.horas = int(horastotal)
        
        session.commit()
        session.close()
        return {"Sucess":"Presenca cadastrada"}
