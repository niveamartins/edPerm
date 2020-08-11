import sys
from os import path
from datetime import datetime, timezone
import qrcode


from flask import Blueprint, request, jsonify, render_template, redirect, url_for, session, jsonify, send_file
from sqlalchemy.exc import InternalError
from flask_jwt_extended import (jwt_required, get_jwt_identity)
from sqlalchemy import func
from flask_cors import CORS, cross_origin

from database.session import get_session
from database.model.Model import *
from utilities.montaRelatorio import *
from utilities.loggers import get_logger
from utilities.DateTimes import tradutor
from services.CreateUserService import CreateUserService
from services.CreateTurmaService import CreateTurmaService
from services.CreateAlunoService import CreateAlunoService
from services.CreateApoiadorService import CreateApoiadorService
from services.CreateHorarioService import CreateHorarioService
from services.AutheticateUserService import AutheticateUserService
from services.CadastrarAlunoService import CadastrarAlunoService
from services.ListTurmaService import ListTurmaService
from services.CreatePresencaService import CreatePresencaService
from services.makeValidacaoService import makeValidacaoService

blueprint = Blueprint('endpoints', __name__) 
CORS(blueprint)
logger = get_logger(sys.argv[0])

#AINDA NÃO SERÁ IMPLEMENTADA
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
    response = authenticateUser.execute(usuario, senha)
    print(response)
    return jsonify(response), 200


@blueprint.route('/authTest', methods=['GET'])
@jwt_required  # unico requerimento para criar rotas protegidas é adicionar esse decorator
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@blueprint.route('/dadosPessoais', methods=['GET'])
@jwt_required
def dados_pessoais():
    user = get_jwt_identity()
    session = get_session()
    data = session.query(User).filter_by(Id=user['id']).one().as_dict()
    session.close()
    del data["senha"]
    return jsonify(data)


@blueprint.route("/cadastrar", methods=['POST'])
def cadastrar():

    userData = request.get_json()
    userDataFields = ["usuario", "email", "senha", "cpf", "telefone", "tipo"]

    if not all(field in userData for field in userDataFields):
        return "Missing information", 400

    createUser = CreateUserService()

    user = createUser.execute(userData)

    return jsonify(user)


#TODO: estruturar como será a segunda parte do cadastramento de informações
@blueprint.route("/cadastrardadoscomplementares", methods=['POST'])
@jwt_required
def cadastrarDadosComplementares():
    pass


@blueprint.route("/cadastrarturma", methods=['POST'])
def cadastrarturma(): 

    # Não testado a parte dos Json

    turmaData = request.get_json()
    turmaDataFields = ["responsavel", "nome_do_curso",
                       "carga_horaria_total", "tolerancia", "modalidade"]

    if not all(field in turmaData for field in turmaDataFields):
        return "Missing information", 400

    createTurma = CreateTurmaService()

    turma = createTurma.execute(turmaData)

    return jsonify(turma)



@blueprint.route('/listaturma/<int:codigo_turma>')
@jwt_required
def turma(codigo_turma):
    session=get_session()
    data = session.query(Turma).filter_by(id_turma=codigo_turma).one()
    JSON = [data.as_dict()]
    JSON[0]['NomeDoPropositor'] = data.propositor.usuario

    session.close()

    return jsonify(JSON)



@blueprint.route("/listaturma", methods=['GET'])
def listarturma():
    #user_id = request.json.get('user_id', None)

    listTurma = ListTurmaService()
    turmas = listTurma.execute()
    print(turmas)
    return jsonify(turmas)






@blueprint.route("/marcarpresenca", methods=['POST'])
@jwt_required
def atualizarpresenca():
    presencaData = request.get_json()
    presencaDataFields = ["emailAluno","idAluno","idTurma"]

    if not all(field in presencaData for field in presencaDataFields):
        return {"Error":"Bad Request"}

    marcarPresenca = CreatePresencaService()
    presenca = marcarPresenca.execute(presencaData)
    return jsonify(presenca)

@blueprint.route("/cadastraraluno", methods=['POST'])
@jwt_required
def cadastraraluno():

    #Não testado a parte dos Json

    cadastroData = request.get_json()
    cadastroDataFields = ["usuario", "nome_do_curso"]

    if not all(field in cadastroData for field in cadastroDataFields):
         return "Missing information", 400

    cadastrarAluno = CreateAlunoService()

    Aluno = cadastrarAluno.execute(cadastroData)

    return jsonify(Aluno)

# Issue 36
@blueprint.route("/cadastraralunonaturma", methods=['POST'])
@jwt_required
def cadastraralunonaturma():

    #Não testado a parte dos Json
    #Perguntar se
    #cpf == do token
    #preciso testar se o usuario e aluno
    userData = get_jwt_identity()
    cadastroData = request.get_json()
    cadastroDataFields = ["cpfAluno", "idTurma"]




    if not all(field in cadastroData for field in cadastroDataFields):
         return "Missing information", 400

    cadastroData['id'] = userData['id']

    cadastrarAlunoNaTurma = CadastrarAlunoService()

    msg = cadastrarAlunoNaTurma.execute(cadastroData)

    return jsonify(msg)

# Issue 36

@blueprint.route("/cadastrarapoiador", methods=['POST'])
@jwt_required
def cadastrarapoiador():

    apoiadorData = request.get_json()
    apoiadorDataFields = ["email_apoiador", "id_turma"]

    if not all(field in apoiadorData for field in apoiadorDataFields):
        return "Missing information", 400

    cadastrarApoiador = CreateApoiadorService()

    msg = cadastrarApoiador.execute(apoiadorData)
    return jsonify(msg)


@blueprint.route("/cadastrarhorario", methods=['POST'])
@jwt_required
def cadastrarhorario():
    # Não testado a parte dos Json

    horarioData = request.get_json()
    horarioDataFields = ["idTurma", "DiaDaSemana",
                         "hInicio", "hTermino"]
    user = get_jwt_identity()
    
    if not all(field in horarioData for field in horarioDataFields):
        return "Missing information"

    horarioData['idPropositor'] = user['id']

    cadastrarHorario = CreateHorarioService()
    response = cadastrarHorario.execute(horarioData)
    
    return jsonify(response)

@blueprint.route("/autocadastro",methods=['POST'])
@jwt_required
def autocadastro():
    cadastroData=request.get_json()
    cadastroDataFields = ["cpf","tokenTurma"]

    if not all(field in cadastroData for field in cadastroDataFields):
        return {"Error":"Missing information"}

    cadastraraluno=CadastrarAlunoService().executeAluno(cadastroData)
    return cadastraraluno


#AINDA NÃO TERMINADA
@blueprint.route("/chamadavalidar", methods=['POST'])
@jwt_required
def chamadavalidar():
    if not request.is_json:
       return jsonify({"Error": "Missing JSON in request"}), 400
    
    user = get_jwt_identity()
    session = get_session()
    checkCargo = session.query(User).filter_by(Id=user["id"],usuario=user["usuario"]).one().as_dict()
    if checkCargo["tipo"]=='cursista' or checkCargo["tipo"]=='apoiador':
        return jsonify({"Error": "Cargo não autorizado"})
    
    validacao = makeValidacao().execute(request.get_json())

    return jsonify(validacao)

### RELATORIOS ###

# RELATORIO CONTATO
@blueprint.route('/relatoriocontato', methods=['GET'])
@jwt_required
def get_relatoriocontato():
    session = get_session()
    data = session.query(User).all()
    data = [relatoriocontato(i) for i in data]
    session.close()
    return jsonify(data)

# RELATORIO CPF/NOME


@blueprint.route('/relatoriocpfnome', methods=['GET'])
@jwt_required
def get_relatoriocpfnome():
    session = get_session()
    data = session.query(Turma).all()
    JSON = [Rcpfnome(i) for i in data]
    for (i, j) in zip(data, JSON):
        for z in i.Alunos:
            j["alunos"].append(RcpfnomeAlunos(z))
    session.close()
    return jsonify(JSON)

# RELATORIO FREQUENCIA
# AINDA NÃO SERÁ IMPLEMENTADO, PRECISA DA FUNÇÃO DE CHECKIN


@blueprint.route('/relatoriofrequencia', methods=['GET'])
@jwt_required
def get_relatoriofrequencia():
    
    session = get_session()
    TuplaAlunoPresencaTotTurma = session.query(Aluno,PresencaTot,Turma).filter(Aluno.id_aluno == PresencaTot.presencatot_id_aluno, PresencaTot.presencatot_id_turma == Turma.id_turma).all()
    print(TuplaAlunoPresencaTotTurma)
    if not TuplaAlunoPresencaTotTurma:
        return jsonify({"Error":"Ocorreu um erro na base de dados"})

    #TODO: POPULAR O PRESENCATOT
    Alunos = [frequencia(i) for i in TuplaAlunoPresencaTotTurma[0]]
    
    for (aluno, infoAlunos) in zip(TuplaAlunoPresencaTotTurma[0],Alunos):
        for turma in aluno.MinhasTurmas:
            for presencatot in TuplaAlunoPresencaTotTurma[1]:
                if presencatot.presencatot_id_turma == turma.id_turma:
                    infoAlunos["Turmas"].append(frequenciaTurma(presencatot,turma))
    


    session.close()
    return jsonify(infoAlunos)

# RELATORIO PROFISSAO


@blueprint.route('/relatorioprofissao/<string:NomeDaProfissao>', methods=['GET', 'POST'])
@jwt_required
def get_relatorioprofissao(NomeDaProfissao):
    JSON, err = relatorioatividades('profissao', NomeDaProfissao)
    if err == -1:
        return "Sem dados para compor o relatório"
    else:
        return jsonify(JSON)

# RELATORIO CAP


@blueprint.route('/relatorioCAP/<string:NomeDoCAP>', methods=['GET'])
@jwt_required
def get_relatorioCAP(NomeDoCAP):
    JSON, err = relatorioatividades('CAP', NomeDoCAP)
    if err == -1:
        return "Sem dados para compor o relatório"
    else:
        return jsonify(JSON)

# RELATORIO FUNÇÃO


@blueprint.route('/relatoriofuncao/<string:NomeDaFuncao>', methods=['GET'])
@jwt_required
def get_relatoriofuncao(NomeDaFuncao):
    JSON, err = relatorioatividades('funcao', NomeDaFuncao)
    if err == -1:
        return "Sem dados para compor o relatório"
    else:
        return jsonify(JSON)

# RELATORIO SUPERINTENDENCIA


@blueprint.route('/relatoriosuperintendencia/<string:NomeDaSuperintendencia>', methods=['GET'])
@jwt_required
def get_relatoriosuperentendencia(NomeDaSuperintendencia):
    JSON, err = relatorioatividades("superintendencia", NomeDaSuperintendencia)
    if err == -1:
        return "Sem dados para compor o relatório"
    else:
        return jsonify(JSON)

# RELATORIO UNIDADE


@blueprint.route('/relatoriounidade/<string:NomeDaUnidade>', methods=['GET'])
@jwt_required
def get_relatoriounidade(NomeDaUnidade):
    JSON, err = relatorioatividades("unidade", NomeDaUnidade)
    if err == -1:
        return "Sem dados para compor o relatório"
    else:
        return jsonify(JSON)


# Concluintes: relatório de cursos finalizados para emissão de certificados pelo propositor.
@blueprint.route('/relatorioconcluintes', methods=['GET'])
@jwt_required
def get_concluintes():
    session = get_session()
    data = session.query(Turma).filter_by(IsConcluido=1).all()
    JSON = [concluintes(i) for i in data]
    for (i, j) in zip(data, JSON):
        for k in i.Alunos:
            j['cursistas'].append(atividade_aluno(k))
    session.close()
    return jsonify(JSON)


@blueprint.route('/testdata', methods=['GET'])
def data():
    try:
        session = get_session()
        User1 = User(usuario="Tiffany", email="aufderhar.elwin@example.com", senha="aaaasenha",
                     cpf="5586424623", telefone="987654653", tipo="cursista")
        User2 = User(usuario="Wilton", email="zulauf.bertha@example.com", senha="bbbbsenha",
                     cpf="9887048243", telefone="187654635", tipo="propositor")
        User3 = User(usuario="Gino", email="meaghan.zieme@example.org", senha="ddddsenha",
                     cpf="9843298432", telefone="287654432", tipo="cursista")
        User4 = User(usuario="Domenica", email="irice@example.org", senha="eeeeeasdasfa",
                     cpf="9874321121", telefone="187439298", tipo="cursista")
        User5 = User(usuario="Beau", email="horace.beer@example.org", senha="eeeeeasdasfa",
                     cpf="0987432187", telefone="098743119", tipo="cursista")
        session.add_all([User1, User2, User3, User4, User5])
        session.commit()
        Turma1 = Turma(id_responsavel=User2.Id, nome_do_curso="calculo", IsConcluido=0,
                       carga_horaria_total=60, tolerancia=30, modalidade="n sei", turma_tag="tbm n sei")
        Turma2 = Turma(id_responsavel=User2.Id, nome_do_curso="iot", IsConcluido=1,
                       carga_horaria_total=60, tolerancia=30, modalidade="n sei", turma_tag="tbm n sei")

        Aluno1 = Aluno(alunoUser=User1)
        Aluno2 = Aluno(alunoUser=User3)
        Aluno3 = Aluno(alunoUser=User2) 
        Aluno4 = Aluno(alunoUser=User4) 
        session.add_all([Aluno1, Aluno2, Aluno3, Aluno4, Turma1, Turma2])
        session.commit()
        Turma1.Alunos.append(User1.Aluno)
        Turma1.Alunos.append(Aluno2)
        Turma1.Alunos.append(Aluno3)

        for alunos in Turma1.Alunos:
                if(alunos.id_aluno == User1.Aluno.id_aluno):
                    print("Testando")

        if not(User5.Aluno):
            print('Oi')
        session.commit()
        logger.info("informações de teste inseridas no banco de dados")
        session.close()
        return "200OK"
    except InternalError:
        logger.error("Banco de dados (EdPermanente) desconhecido")
        return "502ERROR"
