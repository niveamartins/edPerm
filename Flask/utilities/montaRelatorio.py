from datetime import datetime

from database.session import get_session 
from database.model.Model import *


def relatorioatividades(TipoDeFiltro,Valor):
    session = get_session()
    data = session.query(Turma).all()
    JSON = [atividade_turma(i,TipoDeFiltro) for i in data]
    for (i,j) in zip(data,JSON):
        for k in i.Alunos:
            aux = atividade_aluno(k)
            print(i.nome_do_curso,aux[TipoDeFiltro],Valor)
            if aux[TipoDeFiltro] != Valor:
                continue
            j['cursistas'].append(aux)
        if j['cursistas'] == []:
            index = JSON.index(j)
            del JSON[index]
    if JSON == []:
        err = -1
    else:
        err = 0
    session.close()
    return JSON, err


def relatoriocontato(User):
    return {
          "tipoDeRelatorio":"Contato",
          "id": f'{self.Id}',
          "nome": f'{self.usuario}',
          "email":f'{self.email}', 
          "telefone":f'{self.telefone}'
        }


def Rcpfnome(Turma):
        return {
            "tipoDeRelatorio":"CPF",
            "id_turma": f'{Turma.id_turma}',
            "nomeDoCurso": f'{Turma.nome_do_curso}',
            "idPropositor": f'{Turma.propositor.Id}',
            "propositor": f'{Turma.propositor.usuario}',
            "alunos": []           
        }

def RcpfnomeAlunos(Aluno):
        return {
                "id_User":f'{Aluno.alunoUser.Id}',
                "id_aluno":f'{Aluno.id_aluno}',
                "nomeDoAluno":f'{Aluno.alunoUser.usuario}',
                "cpfDoAluno":f'{Aluno.alunoUser.cpf}'
        }
        

def listar_turmas(Turma,tipoDeRelatorio):
    return {
        'tipoDeRelatorio': f'{tipoDeRelatorio}',
        'id_turma': f'{Turma.id_turma}',
        'nome_do_curso':f'{Turma.nome_do_curso}',
        'id_responsavel':f'{Turma.id_responsavel}',
        'Carga_Horaria_Total':f'{Turma.carga_horaria_total}',
        'cursistas':[]
    }


def listaturma(Turma):

    return {
        'id_turma': f'{Turma.id_turma}', 
        'nome_do_curso':f'{Turma.nome_do_curso}',
        'id_responsavel':f'{Turma.id_responsavel}',
        'nome_responsavel':f'{Turma.propositor.usuario}'
        'Carga_Horaria_Total':f'{Turma.carga_horaria_total}',
        'tag_turma':f'{Turma.tag_turma}',
        'tolerancia':f'{Turma.tolerancia}',
        'modalidade':f'{Turma.modalidade}'
    }




def atividade_aluno(Aluno):
    return {
            'id_aluno':f'{Aluno.id_aluno}',
            'profissao':f'{Aluno.complementoUser.profissao}',
            'funcao':f'{Aluno.complementoUser.funcao}',
            'superintendenciadaSUBPAV':f'{Aluno.complementoUser.superintendenciaDaSUBPAV}',
            'CAP':f'{Aluno.complementoUser.CAP}',
            'unidade':f'{Aluno.complementoUser.unidadeBasicaDeSaude}',
            'id_user':f'{Aluno.alunoUser.Id}',
            'aluno_nome':f'{Aluno.alunoUser.usuario}'
        
    }

def concluintes(Turma):
    return {
        "tipoDeRelatorio":"concluintes",
        'id_turma' : f'{Turma.id_turma}',
        'nome_do_curso' : f'{Turma.nome_do_curso}', 
        'id_do_responsavel' : f'{Turma.id_responsavel}',
        'nomeDoPropositor': f'{Turma.propositor.usuario}',
        'Carga_Horaria_Total' : f'{Turma.carga_horaria_total}',
        'cursistas':[]
    }        

def frequencia(Aluno):
    return {
        "tipoDeRelatorio":"frequencia",
        'Nome': f'{Aluno.complementoUser.usuario}',
        'cpf': f'{Aluno.complementoUser.cpf}',
        'id_aluno' : f'{Aluno.id_aluno}',
        'id_user_aluno' : f'{Aluno.alunos_id_user}',
        'Turma' : []
     }


def atualizapresenca(Presenca, Horario):
    DeltaTime = Horario.HorarioTermino - Presenca.ultimoCheckIn.time()
    
    