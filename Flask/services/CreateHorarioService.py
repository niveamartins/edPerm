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
            QueryTurma = session.query(Turma).filter_by(nome_do_curso=horarioData['Turma']).first()
            if (QueryTurma != None):
                QueryUsuario = session.query(User).filter_by(usuario=horarioData['Propositor']).first()
                if (QueryUsuario != None):
                    if(QueryTurma.id_responsavel == QueryUsuario.Id):
                        horario = Horario(HorarioIdTurma = QueryTurma.id_turma, DiaDaSemana = horarioData['DiaDaSemana'],HorarioInicio = horarioData['Inicio'], HorarioTermino = horarioData['Termino'])
                        session.add_all([horario])
                        session.commit()
                        return horario.as_dict()
                    else:
                        return "Usuario não é o responsavel pela turma", 400
                else:
                    return "Usuario não cadastrado", 400
            else:
                return "Turma não cadastrada", 400
        except InternalError:
            logger.error("Banco de dados (EdPermanente) desconhecido")
            return "502ERROR"
