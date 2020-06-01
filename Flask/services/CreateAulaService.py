import sys

from database.session import get_session
from sqlalchemy.exc import InternalError
from database.model.Model import *
from utilities.loggers import get_logger



class CreateAulaService:
    def execute(self, aulaData):
        #logger = get_logger(sys.argv[0])
        #aulaDataFields = ["Turma", "Inicio", "Termino"]
        try:
            session = get_session()
            QueryTurma = session.query(Turma).filter_by(nome_do_curso=aulaData['Turma']).first()
            if (QueryTurma != None):
                aula = Aula(aula_id_turma = QueryTurma.id_turma, aula_inicio = aulaData['Inicio'], aula_termino = aulaData['Termino'])
                session.add_all([aula])
                session.commit()
                #return cadastrar.as_dict()
                return "Aula cadastrada"
            else:
                return "Turma não cadastrada", 400
        except InternalError:
            logger.error("Banco de dados (EdPermanente) desconhecido")
            return "502ERROR"
