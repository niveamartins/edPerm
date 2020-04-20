#CPF/Nome: quais cursos foram propostos e cursados por Usuários.

#  {
#       turma_id:{
#               fulano1:{
#                   nome/cpf/proposto?
#}
#       }
#}



class RelatorioCPFNome():
    def __init__(self,alunos,Turmas):
        self.alunos = alunos
        self.turmas = Turmas
    
    def CriarJson(self):
        Relatorio = {}
        for i in self.turmas:
            Relatorio[i.id]={
                "nomedaturma":i.nome,
                "propositor":i.id_responsavel,
                "alunos" = {}
                }
            for j in self.alunos:
                Relatorio[i.id]["alunos"][j.id] = {
                    "nome": j.nome,
                    "cpf": j.cpf
                }
        return Relatorio


class Turma():
    def __init__(self, nome, id_responsavel):
        self.nome = nome
        self.id_responsavel = id_responsavel


   
class Alunos():
    def __init__(self, nome, cpf, id, id_turma):
                 