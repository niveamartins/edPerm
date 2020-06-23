import sys

from database.session import get_session
from sqlalchemy.exc import InternalError
from database.model.Model import *
from utilities.loggers import get_logger

#Não testado a parte dos Json

class CreateHorarioService:
    def execute(self, horarioData):
        logger = get_logger(sys.argv[0])
        try:
            session = get_session()
            QueryTurma = session.query(Turma).filter_by(id_turma =horarioData['Turma']).first()
            if (QueryTurma == None):
              return "Turma não cadastrada"
            for horarios in QueryTurma.Horarios:
              if(horarios.DiaDaSemana == horarioData['DiaDaSemana'] and horarios.HorarioInicio == horarioData['Inicio'] and horarios.HorarioTermino == horarioData['Termino']):
                return "Horario ja cadastrado"
            horario = Horario(HorarioIdTurma = QueryTurma.id_turma, DiaDaSemana = horarioData['DiaDaSemana'],HorarioInicio = horarioData['Inicio'], HorarioTermino = horarioData['Termino'])
            session.add_all([horario])
            session.commit()
            return horario.as_dict()

        except InternalError:
            logger.error("Banco de dados (EdPermanente) desconhecido")
            return "502ERROR"
