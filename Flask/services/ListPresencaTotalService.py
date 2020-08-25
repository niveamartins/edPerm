import sys

from utilities.loggers import get_logger
from sqlalchemy.exc import InternalError
from database.session import get_session
from sqlalchemy.exc import InternalError
from database.model.Model import Turma, User, Aluno, PresencaTotal
from utilities.montaRelatorio import frequencia

def Presencastotais_info(presenca, usuario):
    return {
        'numero_de_presencas': f'{presenca.numero_de_presencas}',
        'horas': f'{presenca.horas}',
        'minutos': f'{presenca.minutos}',
        'segundos': f'{presenca.segundos}',
        'nome': f'{usuario.nome}'
    }


class ListPresencaTotalService:
    def execute(self, turmaData):
        logger = get_logger(sys.argv[0])
        try:
            session = get_session()
            QueryUsuarios = session.query(User).all()
            QueryTurma = session.query(Turma).filter(Turma.nome_do_curso == turmaData["nome_do_curso"]).first()
            PresencasTotais = []
            if not QueryTurma:
                return {"Error":"Turma não encontrada"}, 400
            if not QueryUsuarios:
                return {"Error":"Nenhum usuario encontrado"}, 400
            for i in QueryTurma.Presencastotais:
                PresencasTotais.append(Presencastotais_info(i,i.alunoDono.alunoUser))
            session.close()
            return PresencasTotais
        except InternalError:
            logger.error("Banco de dados (EdPermanente) desconhecido")
            return "502ERROR"


