from database.session import get_session
from database.model.Model import *
from datetime import datetime, time

#horarioData=["idTurma", "DiaDaSemana","hInicio", "hTermino","idPropositor"]

class CreateHorarioService:
    def execute(self, horarioData):
        session = get_session()
        QueryTurma = session.query(Turma).filter_by(id_turma=horarioData['idTurma'],id_responsavel=horarioData["idPropositor"]).first()
        if not QueryTurma:
          return {"Error":"Turma não cadastrada"}

        horarioData['hInicio']=datetime.strptime(horarioData['hInicio'], '%H:%M:%S').time()
        horarioData['hTermino']=datetime.strptime(horarioData['hTermino'], '%H:%M:%S').time()

        for horarios in QueryTurma.Horarios:
          diaDaSemanaSobreposto = (horarios.DiaDaSemana == horarioData['DiaDaSemana'])
          horarioSobreposto = sobreposicaoDeHorario(horarios.HorarioInicio,horarios.HorarioTermino,horarioData['hInicio'],horarioData['hTermino'])
          if (diaDaSemanaSobreposto and horarioSobreposto):
            return {"Error":"Horario sobreposto"}
        horario = Horario(HorarioIdTurma = QueryTurma.id_turma, DiaDaSemana = horarioData['DiaDaSemana'],HorarioInicio = horarioData['hInicio'], HorarioTermino = horarioData['hTermino'])
        session.add(horario)
        session.commit()
        return {"Sucess":"Horario Cadastrado"}

def sobreposicaoDeHorario(horarioDeInicioDoBD, horarioDeTerminoDoBD, hInicio=None, hTermino=None):
    
    hInicio = hInicio or datetime.utcnow().time()
    hTermino = hTermino or datetime.utcnow().time()
    return (hInicio >= horarioDeInicioDoBD and hInicio <= horarioDeTerminoDoBD) or (hTermino >= horarioDeInicioDoBD and hTermino <= horarioDeTerminoDoBD) or (hInicio <= horarioDeInicioDoBD and hTermino>= horarioDeTerminoDoBD)

    
