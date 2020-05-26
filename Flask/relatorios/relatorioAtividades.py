# Dado um determinado filtro, o relatorio de atividades vai conter:



#{
#    -turma_id:{
#        nome_do_curso: "tal",
#        IsRealizado: 0,
#        id_do_Propositor:2142,
#        nome_do_propositor:"candango"
#        cargaHoraria:3,
#        cursistas:{
#            id_do_aluno:{
#                nomeUsuario:"fulano",
#                cpf:"32454325"
#            }
#        }
#    }
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































































