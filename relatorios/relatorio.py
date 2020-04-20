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

class RelatoriosAtividades():
    def __init__(self,usuarios):
        usuarios = self.usuarios
        relatorio_by_usuarios = {}
        for usuario in usuarios:
            relatorio_by_usuarios[usuario[0]] = {
                "nome": usuario[1]
                
            }
            
    
    def GerarDicCargos():
        relatorio_by_cargos={}
        

# query: alunos(id == id).id_turma 

# 
        
