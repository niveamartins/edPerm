from database.model.Model import *


def Rcpfnome(Turma):
        return {
            "id_turma": f'{Turma.id_turma}',
            "nomeDaTurma": f'{Turma.nome_do_curso}',
            "idPropositor": f'{Turma.propositor.Id}',
            "propositor": f'{Turma.propositor.usuario}',
            "alunos": {}           
        }

def RcpfnomeAlunos(Aluno):
        return {
            f'{Aluno.alunoUser.Id}':{
            "nomeDoAluno":f'{Aluno.alunoUser.usuario}',
            "cpfDoAluno":f'{Aluno.alunoUser.cpf}'
            }
        }