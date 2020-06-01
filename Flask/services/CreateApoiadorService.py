import sys

from database.session import get_session
from sqlalchemy.exc import InternalError
from database.model.Model import *
from utilities.loggers import get_logger



class CreateApoiadorService:
    def execute(self, cadastroData):
        #logger = get_logger(sys.argv[0])
        #apoiadorDataFields = ["usuario", "nome_do_curso"]
        try:
            session = get_session()
            QueryUsuario = session.query(User).filter_by(usuario=cadastroData['usuario']).first()
            if (QueryUsuario != None):
                QueryTurma = session.query(Turma).filter_by(nome_do_curso=cadastroData['nome_do_curso']).first()
                if (QueryTurma != None):
                    QueryComplemento = session.query(UserComplemento).filter_by(id_do_user=QueryUsuario.Id).first()
                    if (QueryComplemento != None):
                        if(QueryUsuario.tipo == 'apoiador'):
                            for apoiadores in QueryTurma.AlunosApoiadores:
                                buscaDoUsuario = session.query(User).filter_by(Id = apoiadores.apoiador_id_user).first()
                                if(buscaDoUsuario.usuario == QueryUsuario.usuario):
                                    return "Apoiador ja cadastrado na turma"
                            if (QueryUsuario.AlunoApoiador != None):
                                QueryTurma.AlunosApoiadores.append(QueryUsuario.AlunoApoiador)
                                session.commit()
                                #return cadastrar.as_dict()
                                return "Apoiador cadastrado na turma"
                            else: 
                                apoiador = AlunoApoiador(apoiador_id_turma=QueryTurma.id_turma, apoiador_id_user=QueryUsuario.Id)
                                session.add_all([apoiador])
                                session.commit()
                                QueryTurma.AlunosApoiadores.append(QueryUsuario.AlunoApoiador)
                                session.commit()
                                return "Apoiador criado e cadastrado na turma"
                        else:
                            return "Usuario não é um apoiador", 400
                    else:
                        return "Dados Complementares não preenchidos", 400
                else:
                    return "Turma não cadastrada", 400
            else:
                return "Usuario não cadastrado", 400
        except InternalError:
            logger.error("Banco de dados (EdPermanente) desconhecido")
            return "502ERROR"
