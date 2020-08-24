from database.session import get_session
from database.model.Model import *
from datetime import datetime, time

#AulaData=["nome_do_curso", "nome_da_aula" "hInicio", "hTermino", "idPropositor"]

class CreateAulaService:
    def execute(self, AulaData):
        session = get_session()
        QueryTurma = session.query(Turma).filter_by(nome_do_curso=AulaData['nome_do_curso']).first()
        if not QueryTurma:
          return {"Error":"Turma não cadastrada"}

        AulaData['hInicio']=datetime.strptime(AulaData['hInicio'], '%d/%m/%Y-%H:%M:%S')
        AulaData['hTermino']=datetime.strptime(AulaData['hTermino'], '%d/%m/%Y-%H:%M:%S')

        aula = Aula(nome_da_aula = AulaData['nome_da_aula'], aula_id_turma = QueryTurma.id_turma,hora_de_inicio = AulaData['hInicio'], hora_de_termino = AulaData['hTermino'])
        session.add(aula)
        session.commit()
        return {"Sucess":"Aula Cadastrada"}

def sobreposicaoDeHorario(horarioDeInicioDoBD, horarioDeTerminoDoBD, hInicio=None, hTermino=None):
    
    hInicio = hInicio or datetime.utcnow().time()
    hTermino = hTermino or datetime.utcnow().time()
    return (hInicio >= horarioDeInicioDoBD and hInicio <= horarioDeTerminoDoBD) or (hTermino >= horarioDeInicioDoBD and hTermino <= horarioDeTerminoDoBD) or (hInicio <= horarioDeInicioDoBD and hTermino>= horarioDeTerminoDoBD)

    
