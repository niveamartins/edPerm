from database.session import get_session
from database.model.Model import *

#dados = ['idTurma','presencas','HorarioDeTermino']
class makeValidacaoService:
    def execute(self, dados):
        session = get_session()
        presencas = session.query(Presenca,PresencaTot).filter(Presenca.presencaValidade==0,Presenca.presenca_id_turma==dados['idTurma'],PresencaTot.presencatot_id_turma==dados['idTurma']).all()
        horarioTermino = session.query(Turma.)
        if not presencas:
            return {'Error':'Não há presencas no banco de dados'}

        for presenca in presencas[0]:
            if presenca is in dados['presencas']:
                presenca.presencaValidade = 1
                delta = presenca.CheckIn.time()- dados['HorarioDeTermino']
                for presencatot in presencas[1]:

            else:
                session.delete(presenca)