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
            if (QueryUsuario == None):
                return "Usuario não cadastrado", 400

            QueryTurma = session.query(Turma).filter_by(nome_do_curso=cadastroData['nome_do_curso']).first()
            if (QueryTurma == None):
                return "Turma não cadastrada", 400
            
            QueryComplemento = session.query(UserComplemento).filter_by(id_do_user=QueryUsuario.Id).first()           
            if (QueryComplemento == None):
                return "Dados Complementares não preenchidos", 400

            if(QueryUsuario.tipo != 'cursista'):
                return "Usuario não é um cursista", 400

            for alunos in QueryTurma.Alunos:
                if(alunos.alunos_id_user == QueryUsuario.Id):
                    return "Aluno ja cadastrado na turma"
                            
            if (QueryUsuario.Aluno != None):
                QueryTurma.Alunos.append(QueryUsuario.Aluno)
                session.commit()
                return QueryUsuario.Aluno.as_dict()
            else: 
                aluno = Aluno(alunos_id_user=QueryUsuario.Id, alunos_id_complemento=QueryComplemento.id_complemento)
                session.add_all([aluno])
                session.commit()
                QueryTurma.Alunos.append(QueryUsuario.Aluno)
                session.commit()
                return QueryUsuario.Aluno.as_dict()

        except InternalError:
            logger.error("Banco de dados (EdPermanente) desconhecido")
            return "502ERROR"
