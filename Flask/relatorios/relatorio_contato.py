import json
#from registerDateTime import Hora
import aux_functions.registerDateTime as registerDateTime
#Contato: gerar lista de contato (e-mail e telefone) dos Usuários.

class RelatorioContatos():

    def __init__(self, usuarios):
        self.usuarios = usuarios # puxa all ids do banco
        self.createJson()
        print(registerDateTime.registerDateTime())
        self.DataeHoraDeCriacao = registerDateTime.registerDateTime()

    def createJson(self):
        Json={}
        for usuario in self.usuarios:
            Json[usuario.id] = {
                'nome':usuario.nome,
                'email':usuario.email,
                'telefone':usuario.telefone
            }
        print(json.dumps(Json, indent=4))

#Classe alunos abaixo é para efetuar teste apenas
class Alunos():

    def __init__(self,id,nome,email,telefone):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone



a = Alunos(1,"Josnei","aaaaaaa@.com","2")
b = Alunos(2,"IrmaodoJosnei","bbbbbbb@.com","7")
c = Alunos(3,"Josneia","ccccccc@.com","23")

relat = RelatorioContatos([a,b,c])