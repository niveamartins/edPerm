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
          hInicioSobreposto = is_time_between(horarios.HorarioInicio,horarios.HorarioTermino,horarioData['hInicio'])
          hTerminoSobreposto = is_time_between(horarios.HorarioInicio,horarios.HorarioTermino,horarioData['hTermino'])
          #TODO: consertar sobreposição 
          if diaDaSemanaSobreposto and (hInicioSobreposto or hTerminoSobreposto):
            return {"Error":"Horario sobreposto"}
        horario = Horario(HorarioIdTurma = QueryTurma.id_turma, DiaDaSemana = horarioData['DiaDaSemana'],HorarioInicio = horarioData['hInicio'], HorarioTermino = horarioData['hTermino'])
        session.add(horario)
        session.commit()
        return {"Sucess":"Horario Cadastrado"}

def is_time_between(begin_time, end_time, check_time=None):
    
    check_time = check_time or datetime.utcnow().time()
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else:
        return check_time >= begin_time or check_time <= end_time