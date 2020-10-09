import sys
import uuid

from sqlalchemy import desc
from database.session import get_session
from sqlalchemy.exc import InternalError
from database.model.Model import *
from utilities.loggers import get_logger
#Não testado a parte dos Json

class AdicionarPublicoService:
    def execute(self, turmaData):

        session = get_session()

        busca = session.query(User).filter_by(Id=turmaData['responsavel']).first()

        if (busca != None):
            QueryTurma = session.query(Turma).filter_by(nome_do_curso=turmaData['nome_do_curso']).first()
            if not(QueryTurma):
                return {"Error":"Turma não encontrada."}, 400

            if not(QueryTurma.id_responsavel == busca.Id):
                return {"Error":"Você não é responsavel dessa turma."}, 400

            if (turmaData['publico_alvo']):
                QueryPublicoAlvo = session.query(PublicoAlvo).filter_by(nome_publicoAlvo=turmaData['publico_alvo']).first()
                if not QueryPublicoAlvo:
                    QueryPublicoAlvo = PublicoAlvo(nome_publicoAlvo = turmaData['publico_alvo'])
                    QueryTurma.PublicosAlvo.append(QueryPublicoAlvo)
                else:
                    if not (QueryPublicoAlvo in QueryTurma.PublicosAlvo):
                        QueryTurma.PublicosAlvo.append(QueryPublicoAlvo)
                    else:
                        return {"Error":"Essa turma já possui esse Público-alvo."}, 400
                session.commit()
            else:
                return {"Error":"Não foi informado o público-alvo."}, 400

            return {"Success":"Público-alvo cadastrado na turma"}, 200
        else:
            return {"Error":"Responsavel não cadastrado"}, 400
