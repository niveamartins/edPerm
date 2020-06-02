import sys
from datetime import datetime, timezone

from flask import Blueprint, request, jsonify, render_template, redirect, url_for, session, jsonify
from sqlalchemy.exc import InternalError
from flask_jwt_extended import (jwt_required, get_jwt_identity)

from database.db_create import Banco
from database.pessoas import Pessoa
from database.session import get_session
from database.model.Model import *
from utilities.montaRelatorio import *
from utilities.loggers import get_logger
from services.CreateUserService import CreateUserService
from services.CreateTurmaService import CreateTurmaService
from services.CreateComplementoService import CreateComplementoService
from services.CreateAlunoService import CreateAlunoService
from services.CreateApoiadorService import CreateApoiadorService
from services.CreateHorarioService import CreateHorarioService
from services.AutheticateUserService import AutheticateUserService

blueprint = Blueprint('endpoints', __name__)
logger = get_logger(sys.argv[0])


@blueprint.route("/esqueci", methods=['POST'])
def esqueci_():
    email = request.form['email']
    banco = Banco()

    banco.recuperarSenha(email)
    return redirect('/esqueci_a_senha')


# da acesso a rotas protegidas por @jwt_required
@blueprint.route("/logar", methods=['POST'])
def logar():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    usuario = request.json.get('usuario', None)
    senha = request.json.get('senha', None)
    if not usuario:
        return jsonify({"msg": "Missing usuario parameter"}), 400
    if not senha:
        return jsonify({"msg": "Missing senha parameter"}), 400
    authenticateUser = AutheticateUserService()
    access_token = authenticateUser.execute(usuario, senha)

    return jsonify(access_token=access_token), 200


@blueprint.route('/authTest', methods=['GET'])
@jwt_required  # unico requerimento para criar rotas protegidas é adicionar esse decorator
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


@blueprint.route("/sair")
def sair():
    session['logged_in'] = False
    session['user'] = ""
    session['user_id'] = ""
    return redirect('/')


@blueprint.route("/cadastrar", methods=['POST'])
def cadastrar():

    userData = request.get_json()
    userDataFields = ["usuario", "email", "senha", "cpf", "telefone", "tipo"]

    if not all(field in userData for field in userDataFields):
        return "Missing information", 400

    createUser = CreateUserService()

    user = createUser.execute(userData)

    return jsonify(user)

#refatorado
@blueprint.route("/cadastrardadoscomplementares", methods=['POST'])
def cadastrarDadosComplementares():

#Não testado a parte dos Json

    complementoData = request.get_json()

    complementoDataFields = ["usuario", "tag", "profissao", "funcao", "superintendenciaDaSUBPAV", "CAP", "unidadeBasicaDeSaude"]

    if not all(field in complementoData for field in complementoDataFields):
        return "Missing information", 400

    createComplemento = CreateComplementoService()

    Complemento = createComplemento.execute(complementoData)

    return jsonify(Complemento)


#refatorado
@blueprint.route("/cadastrarturma", methods=['POST'])
def cadastrarturma():

#Não testado a parte dos Json

    turmaData = request.get_json()
    turmaDataFields = ["responsavel", "nome_do_curso", "carga_horaria_total", "tolerancia", "modalidade", "turma_tag"]

    if not all(field in turmaData for field in turmaDataFields):
        return "Missing information", 400

    createTurma = CreateTurmaService()

    turma = createTurma.execute(turmaData)

    return jsonify(turma)    


@blueprint.route("/listaturma")
def listarturma():

    #session = get_session()
    #busca = session.query(User).filter_by(usuario='Matheus Feitosa')
    #busca = session.query(User).filter_by(usuario= usuario)
    #busca.email =
    #session.commit()

    #try
    #session = get_session()
    #busca = session.query(Turma)
    #alterar o resto

    banco = Banco()
    return render_template('listaturma.html', eventos=banco.listarTurma())


@blueprint.route('/listaturma/<string:codigo_turma>')
def turma(codigo_turma):
    session['nome_da_turma'] = codigo_turma
    banco = Banco()
    soualuno = banco.buscarAlunoPorUsuarioECodigo(
        session['user'], session['nome_da_turma'])
    if(soualuno != []):
        session['inscrito'] = True
    else:
        session['inscrito'] = False
    eventos = banco.buscarTurmaComProfessor(codigo_turma)
    variavel = eventos[0][0]
    alunodaturma = banco.listarAlunos(variavel)
    evento = banco.buscarTurmaComProfessor(codigo_turma)
    return render_template('listaralunosdaturma.html', eventos=evento, alunosdaturma=alunodaturma)

#precisa ser testado
@blueprint.route("/atualizarpresenca", methods=['POST'])
def atualizarpresenca():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400
    
    apoiador = get_jwt_identity()
    aluno = request.get_json()
    session = get_session()
    alunoApoiadordata = session.query(alunoApoiador).filter_by(apoiador_id_user=apoiador.id).one()
    data = session.query(Presenca).filter_by(presenca_id_aluno=aluno["id_aluno"],presenca_id_turma=alunoApoiadordata.apoiador_id_turma)
    data.ultimoCheckIn = datetime.now().time().replace(tzinfo=timezone.utc)
    data.presencaAtualizada = False
    session.commit()
    session.close()

    return jsonify({"msg": "Presença do aluno contabilizada"}), 200

@blueprint.route("/cadastraraluno", methods=['POST'])
def cadastraraluno():

#Não testado a parte dos Json

    cadastroData = request.get_json()
    cadastroDataFields = ["usuario", "nome_do_curso"]

    if not all(field in cadastroData for field in cadastroDataFields):
        return "Missing information", 400

    cadastrarAluno = CreateAlunoService()

    Aluno = cadastrarAluno.execute(cadastroData)

    return jsonify(Aluno)    

@blueprint.route("/cadastrarapoiador", methods=['POST'])
def cadastrarapoiador():

#Não testado a parte dos Json

    apoiadorData = request.get_json()
    apoiadorDataFields = ["usuario", "nome_do_curso"]

    if not all(field in apoiadorData for field in apoiadorDataFields):
        return "Missing information", 400

    cadastrarApoiador = CreateApoiadorService()

    Apoiador = cadastrarApoiador.execute(apoiadorData)
    return jsonify(Apoiador)    

@blueprint.route("/cadastrarhorario", methods=['POST'])
def cadastrarhorario():


#Não testado a parte dos Json

    horarioData = request.get_json()
    horarioDataFields = ["Turma", "DiaDaSemana", "Inicio", "Termino", "Propositor"]

    if not all(field in horarioData for field in horarioDataFields):
        return "Missing information", 400

    cadastrarHorario = CreateHorarioService()

    Horario = cadastrarHorario.execute(horarioData)
    return jsonify(Horario)

#AINDA NÃO TERMINADA
# @blueprint.route("/chamadavalidar", methods=['POST'])
# def chamadapesquisar():
#     if not request.is_json:
#         return jsonify({"msg": "Missing JSON in request"}), 400
    
#     propositor = get_jwt_identity()
#     turma = request.get_json()
#     session = get_session()
#     data = session.query(Presenca).filter_by(presenca_id_turma=turma["id"],presencaAtualizada=False).all()
#     for i in data:

    


    

### RELATORIOS ###

#RELATORIO CONTATO
@blueprint.route('/relatoriocontato', methods=['GET'])
def get_relatoriocontato():
    session = get_session()
    data = session.query(User).all()
    data = [relatoriocontato(i) for i in data]
    session.close()
    return jsonify(data)

#RELATORIO CPF/NOME
@blueprint.route('/relatoriocpfnome', methods = ['GET'])
def get_relatoriocpfnome():
    session = get_session()
    data = session.query(Turma).all()
    JSON = [Rcpfnome(i) for i in data]
    for (i, j) in zip(data, JSON):
        for z in i.Alunos:
            j["alunos"].append(RcpfnomeAlunos(z))
    session.close()
    return jsonify(JSON)

#RELATORIO FREQUENCIA
#AINDA NÃO SERÁ IMPLEMENTADO, PRECISA DA FUNÇÃO DE CHECKIN
@blueprint.route('/relatoriofrequencia', methods = ['GET'])
def get_relatoriofrequencia():
    '''
    Frequência: frequência computada em dias, horas e minutos com base no horário de check-in do cursista. 
    Ele poderá acompanhar a própria carga-horária com base na tolerância informada pelo propositor da atividade.
    '''
    session = get_session()
    data = session.query(Aluno).all()
    JSON = [frequencia(i) for i in data]
    

    session.close()
    return jsonify()

#RELATORIO PROFISSAO 
@blueprint.route('/relatorioprofissao/<string:NomeDaProfissao>', methods = ['GET','POST'])
def get_relatorioprofissao(NomeDaProfissao):
    JSON, err = relatorioatividades('profissao',NomeDaProfissao)
    if err == -1:
        return "Sem dados para compor o relatório"
    else:
        return jsonify(JSON)

#RELATORIO CAP
@blueprint.route('/relatorioCAP/<string:NomeDoCAP>', methods = ['GET'])
def get_relatorioCAP(NomeDoCAP):
    JSON, err = relatorioatividades('CAP',NomeDoCAP)
    if err == -1:
        return "Sem dados para compor o relatório"
    else:
        return jsonify(JSON)

#RELATORIO FUNÇÃO
@blueprint.route('/relatoriofuncao/<string:NomeDaFuncao>', methods = ['GET'])
def get_relatoriofuncao(NomeDaFuncao):
    JSON, err = relatorioatividades('funcao',NomeDaFuncao)
    if err == -1:
        return "Sem dados para compor o relatório"
    else:
        return jsonify(JSON)

#RELATORIO SUPERINTENDENCIA
@blueprint.route('/relatoriosuperintendencia/<string:NomeDaSuperintendencia>', methods = ['GET'])
def get_relatoriosuperentendencia(NomeDaSuperintendencia):
    JSON, err = relatorioatividades("superintendencia",NomeDaSuperintendencia)
    if err == -1:
        return "Sem dados para compor o relatório"
    else:
        return jsonify(JSON)

#RELATORIO UNIDADE
@blueprint.route('/relatoriounidade/<string:NomeDaUnidade>', methods = ['GET'])
def get_relatoriounidade(NomeDaUnidade):
    JSON, err = relatorioatividades("unidade",NomeDaUnidade)
    if err == -1:
        return "Sem dados para compor o relatório"
    else:
        return jsonify(JSON)


#Concluintes: relatório de cursos finalizados para emissão de certificados pelo propositor.
@blueprint.route('/relatorioconcluintes', methods = ['GET'])
def get_concluintes():
    session = get_session()
    data = session.query(Turma).filter_by(IsConcluido=1).all()
    JSON = [concluintes(i) for i in data]
    for (i,j) in zip(data,JSON):
        for k in i.Alunos:
            j['cursistas'].append(atividade_aluno(k)) 
    session.close()
    return jsonify(JSON)


@blueprint.route('/testdata', methods=['GET'])
def data():
    try:
        session = get_session()
        User1 = User(usuario="aaaaa", email="aaaa@exemplo.br", senha="aaaasenha",
                     cpf="aaaaaaaacpf", telefone="987654tel", tipo="cursista")
        User2 = User(usuario="bbbbb", email="bbbb@exemplo.br", senha="bbbbsenha",
                     cpf="bbbbbbbbcpf", telefone="187654tel", tipo="propositor")
        User3 = User(usuario="ddddd", email="dddd@exemplo.br", senha="ddddsenha",
                     cpf="ddddddddcpf", telefone="287654tel", tipo="cursista")
        User4 = User(usuario="eeeeee", email="eeeeee@exemplo.br", senha="eeeeeasdasfa",
                     cpf="ddddddddcpf", telefone="287654tel", tipo="cursista")
        User5 = User(usuario="eeeeee", email="eeeeee@exemplo.br", senha="eeeeeasdasfa",
                     cpf="ddddddddcpf", telefone="287654tel", tipo="cursista")
        session.add_all([User1, User2, User3, User4,User5])
        session.commit()
        Turma1 = Turma(id_responsavel=User2.Id,nome_do_curso="calculo",IsConcluido=0,carga_horaria_total=60,tolerancia=30,modalidade="n sei",turma_tag="tbm n sei")
        Turma2 = Turma(id_responsavel=User2.Id,nome_do_curso="iot",IsConcluido=1,carga_horaria_total=60,tolerancia=30,modalidade="n sei",turma_tag="tbm n sei")
        UserComplemento1 = UserComplemento(user=User1,tag="naosei1",profissao="coach",funcao="direcao",superintendenciaDaSUBPAV="ZAP",CAP="1.0",unidadeBasicaDeSaude="1")
        UserComplemento2 = UserComplemento(user=User2,tag="naosei1",profissao="bundao",funcao="direcao",superintendenciaDaSUBPAV="SAP",CAP="1.0",unidadeBasicaDeSaude="1")
        UserComplemento3 = UserComplemento(user=User3,tag="naosei1",profissao="coach",funcao="gerencia",superintendenciaDaSUBPAV="SAP",CAP="1.0",unidadeBasicaDeSaude="1")
        UserComplemento4 = UserComplemento(user=User4,tag="naosei1",profissao="coach",funcao="gerencia",superintendenciaDaSUBPAV="SAP",CAP="1.0",unidadeBasicaDeSaude="1")
        Aluno1 = Aluno(alunoUser=User1, complementoUser=UserComplemento1)
        Aluno2 = Aluno(alunoUser=User3, complementoUser=UserComplemento3)
        Aluno3 = Aluno(alunoUser=User2, complementoUser=UserComplemento2)
        Aluno4 = Aluno(alunoUser=User4, complementoUser=UserComplemento4)
        session.add_all([Aluno1,Aluno2,Aluno3,Aluno4,UserComplemento1,UserComplemento2,UserComplemento3, UserComplemento4,Turma1,Turma2])
        session.commit()
        Turma1.Alunos.append(Aluno1)
        Turma1.Alunos.append(Aluno2)
        Turma2.Alunos.append(Aluno1)
        aba = session.query(User).filter_by(usuario = "eeeeee").first()
        Turma1.Alunos.append(aba.Aluno)
        session.commit()
        if (User5.Aluno != None):
            print("aaa")
        if (User4.Aluno != None):
            print("fasfasga")
        for x in Turma1.Alunos:
            a = session.query(User).filter_by(Id = x.alunos_id_user).first()
            print(a.usuario)
        logger.info("informações de teste inseridas no banco de dados")
        return "200OK"
    except InternalError:
        logger.error("Banco de dados (EdPermanente) desconhecido")
        return "502ERROR"
