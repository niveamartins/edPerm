import datetime
import json
import aux_functions.registerDateTime as registerDateTime

'''
Frequência: frequência computada em dias, horas e minutos com base no horário de check-in do cursista. 
Ele poderá acompanhar a própria carga-horária com base na tolerância informada pelo propositor da atividade.

'''

class RelatorioFrequencia():    
    def __init__(self, alunos,turma, cargaHoraria):
        self.alunos = alunos # array de alunos em uma determinada turma
        self.turma = turma # a turma dos candangos
        self.cargaHoraria = cargaHoraria # carga horaria da turma/materia
        self.DataeHoraDeCriacao = registerDateTime.registerDateTime()

    def FrequenciaPorAluno(self):
        ListaDasFrequencias = {}
        for aluno in self.alunos:
            ListaDasFrequencias[aluno.name] = aluno.Frequencia
        return ListaDasFrequencias

    def CriarJson(self):
        frequencia = self.FrequenciaPorAluno()
        #TODO: checar a tolerancia de cada aluno de acordo com a tolerancia da turma e retornar um bool
        JSON = {
            "turma" : self.turma,
            "DataeHoraDeCriacao" : self.DataeHoraDeCriacao,
            "CargaHoraria": self.cargaHoraria,
            "alunosEfrequencias":frequencia
        }
        print(json.dumps(JSON, indent=4))

#Classe alunos abaixo é para efetuar teste apenas
class Alunos():

    def __init__(self,name,Frequencia):
        self.name = name
        self.Frequencia = Frequencia



#a = Alunos('Josnei',4)
#b = Alunos('Maria',3)
#c = Alunos('Pedro',7)

#Relatorio1 = RelatorioFrequencia([a,b,c], 'Calculo' , 60)

#Relatorio1.CriarJson()