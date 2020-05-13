#CPF/Nome: quais cursos foram propostos e cursados por Usuários.

#  {
#       turma_id:{
#               fulano1:{
#                   nome/cpf/proposto?
#}
#       }
#}
import json
class RelatorioCPFNome():
    def __init__(self,alunos,Turmas):
        self.alunos = alunos
        self.turmas = Turmas
    
    def CriarJson(self):
        Relatorio = {}
        for turma in self.turmas:
            Relatorio[turma.id]={
                "nomedaturma":turma.nome,
                "propositor":turma.id_responsavel,
                "alunos": {}
                }
            for aluno in self.alunos:
                if(aluno.turma_id == turma.id):
                    Relatorio[turma.id]["alunos"][aluno.id] = {
                        "nome": aluno.nome,
                        "cpf": aluno.cpf
                    }
        return json.dumps(Relatorio, indent=4)


class Turma():
    def __init__(self, nome, id_responsavel, id):
        self.nome = nome
        self.id_responsavel = id_responsavel
        self.id = id


   
class Alunos():
    def __init__(self, nome, cpf, id, turma_id):
        self.nome = nome
        self.turma_id = turma_id
        self.id = id
        self.cpf = cpf

t1= Turma("matematica", 1, 1)
t2= Turma("portugues", 2, 2)
t3= Turma("historia", 2, 3)

a = Alunos("joao", 1234234, 1, 1)
b = Alunos("joao", 1234234, 2, 3)
c = Alunos("joao", 1234234, 3, 2)
d = Alunos("joao", 1234234, 4, 1)
e = Alunos("joao", 1234234, 5, 3)

alunos = [a,b,c,d,e]
turmas= [t1,t2,t3]

relatorio = RelatorioCPFNome(alunos, turmas)
print(relatorio.CriarJson())