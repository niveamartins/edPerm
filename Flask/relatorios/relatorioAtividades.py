# Dado um determinado filtro, o relatorio de atividades vai conter:
# 
# Nome e contato do usuario
# Turmas inseridas
#   Nome, Horarios,ids
#   Cargo na Turma (Aluno, professor, etc)
# Cargo no sistema (adm, gestor, coordenador)
#
# TODO: fala com o matheus para ver se é possivel por um campo de concluido na tabela de turma
#
#   {
#       -fulano_id:{
#           -nome: fulano
#           turmas:{
#               turma_id:{
#                   nomedaturma: calculo
#                   horario: 3
#                   cargonaTurma: professor
#               }
#            }
#            CargonoSistema: gestor  
#       }
#}


# Seriam níveis e combinações de acesso sobre os cursos criados, realizados, os cursistas, carga horária, etc.
class RelatoriosAtividades():
    def __init__(self,usuarios, turmas, alunos, filtro):
        self.usuarios = usuarios
        self.turmas = turmas
        self.alunos = alunos
        self.filtro = filtro

    def Create_Json():
        relatorio = {}
        #TODO: estruturar a comunicação com o banco de dados para realizar as querys
        for usuario in self.usuarios:
            usuarios[usuario.id] = {
                "nome": usuario.nome,
                "cursos":{
                    "criados": {
                        "nomeDoCurso": ,
                        "cargaHoraria": 
                    },
                    "cursados": {
                        "nomeDoCurso": ,
                        "cargaHoraria": ,
                        "Responsavel": 
                    }
                }
            }

        



    def filtroBool(filtro):
        return filtro == 1

    def filtroString(x,filtro):
        return x == filtro































































