import sys

from database.session import get_session
from sqlalchemy.exc import InternalError
from database.model.Model import *
from utilities.loggers import get_logger

#Não testado a parte dos Json

class CreateAlunoService:
    def execute(self, cadastroData):
        logger = get_logger(sys.argv[0])
        try:
            print(cadastroData)
            session = get_session()
            QueryUsuario = session.query(User).filter_by(usuario=cadastroData['usuario']).first()
            if (QueryUsuario != None):
                QueryTurma = session.query(Turma).filter_by(nome_do_curso=cadastroData['nome_do_curso']).first()
                if (QueryTurma != None):
                    if(QueryUsuario.tipo == 'cursista'):
                        for alunos in QueryTurma.Alunos:
                            buscaDoUsuario = session.query(User).filter_by(Id = alunos.alunos_id_user).first()
                            if(buscaDoUsuario.usuario == QueryUsuario.usuario):
                                return "Aluno ja cadastrado na turma"
                        if (QueryUsuario.Aluno != None):
                            QueryTurma.Alunos.append(QueryUsuario.Aluno)
                            session.commit()
                            return QueryUsuario.Aluno.as_dict()
                        else: 
                            aluno = Aluno(alunos_id_user=QueryUsuario.Id)
                            session.add_all([aluno])
                            session.commit()
                            QueryTurma.Alunos.append(QueryUsuario.Aluno)
                            session.commit()
                            return QueryUsuario.Aluno.as_dict()
                    else:
                       return "Usuario não é um cursista", 400
                else:
                    return "Turma não cadastrada", 400
            else:
                return "Usuario não cadastrado", 400
        except InternalError:
            logger.error("Banco de dados (EdPermanente) desconhecido")
            return "502ERROR"
