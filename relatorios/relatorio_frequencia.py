#TODO: fazer uma classe que cujos atributos são os campos do json que será emitido
#TODO: FALAR COM O MATHEUS SOBRE UM ALUNO SÓ PODER ESTAR EM UMA TURMA
#TODO: 
import datetime
import json

class RelatorioFrequencia():    
    def __init__(self, alunos,turma, cargaHoraria):
        tempo = str(datetime.datetime.now()).split(' ')
        self.alunos = alunos #array de alunos em uma determinada turma
        self.turma = turma # a turma dos candangos
        self.cargaHoraria = cargaHoraria # carga horaria da turma/materia
        self.DataeHoraDeCriacao = tempo[0]+' '+tempo[1].split('.')[0]

    def FrequenciaPorAluno(self):
        ListaDasFrequencias = {}
        for aluno in self.alunos:
            ListaDasFrequencias[aluno.name] = aluno.Frequencia
        return ListaDasFrequencias

    def CriarJson(self):
        frequencia = self.FrequenciaPorAluno()
        JSON = {
            "turma" : self.turma,
            "DataeHoraDeCriacao" : self.DataeHoraDeCriacao,
            "CargaHoraria": self.cargaHoraria,
            "alunosEfrequencias":frequencia
        }
        print(json.dumps(JSON, indent=4))


class Alunos():

    def __init__(self,name,Frequencia):
        self.name = name
        self.Frequencia = Frequencia



a = Alunos('Josnei',4)
b = Alunos('Maria',3)
c = Alunos('Pedro',7)

Relatorio1 = RelatorioFrequencia([a,b,c], 'Calculo' , 60)

Relatorio1.CriarJson()