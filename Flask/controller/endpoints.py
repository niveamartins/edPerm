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
from services.DeleteApoiadorService import DeleteApoiadorService
from services.DeleteAlunoService import DeleteAlunoService
from services.TransformarEmAdmService import TransformarEmAdmService
from services.TransformarEmApoiadorService import TransformarEmApoiadorService
from services.TransformarEmCoordenadorService import TransformarEmCoordenadorService
from services.TransformarEmGestorService import TransformarEmGestorService
from services.TransformarEmPropositorService import TransformarEmPropositorService
from services.AtualizarUserService import AtualizarUserService
from services.CreateTurmaService import CreateTurmaService
from services.CreateApoiadorService import CreateApoiadorService
from services.CreateAulaService import CreateAulaService
from services.AdicionarPublicoService import AdicionarPublicoService
from services.CreateHorarioService import CreateHorarioService
from services.AutheticateUserService import AutheticateUserService
from services.CadastrarAlunoService import CadastrarAlunoService
from services.ListTurmaService import ListTurmaService
from services.ListPresencaTotalService import ListPresencaTotalService
from services.ListAulaService import ListAulaService
from services.ListUserService import ListUserService
from services.ListTurmaApoiadorService import ListTurmaApoiadorService
from services.ListTurmaAlunoService import ListTurmaAlunoService
from services.ListTurmaPropositorService import ListTurmaPropositorService
from services.CreatePresencaService import CreatePresencaService
from services.makeValidacaoService import makeValidacaoService

blueprint = Blueprint('endpoints', __name__) 
CORS(blueprint)
logger = get_logger(sys.argv[0])

@blueprint.route("/transformaremadm", methods=['POST'])
@jwt_required
def transformaremadm():
    Token = get_jwt_identity()
    if not(Token['adm']):
        return jsonify({"Error": "Você não tem permissão de acessar essa função"}), 400
    userData = request.get_json()
    userDataFields = ["id"]

    if not all(field in userData for field in userDataFields):
        return {"Error":"Missing information."}, 400

    transformarEmAdm = TransformarEmAdmService()

    user = transformarEmAdm.execute(userData)

    return jsonify(user)

@blueprint.route("/transformaremcoordenador", methods=['POST'])
@jwt_required
def transformaremcoordenador():
    Token = get_jwt_identity()
    if not(Token['adm']):
        return jsonify({"Error": "Você não tem permissão de acessar essa função"}), 400
    userData = request.get_json()
    userDataFields = ["id"]

    if not all(field in userData for field in userDataFields):
        return {"Error":"Missing information."}, 400

    transformaremcoordenador = TransformarEmCoordenadorService()

    user = transformaremcoordenador.execute(userData)

    return jsonify(user)

@blueprint.route("/transformaremgestor", methods=['POST'])
@jwt_required
def transformaremgestor():
    Token = get_jwt_identity()
    if not(Token['adm']):
        return jsonify({"Error": "Você não tem permissão de acessar essa função"}), 400
    userData = request.get_json()
    userDataFields = ["id"]

    if not all(field in userData for field in userDataFields):
        return {"Error":"Missing information."}, 400

    transformaremgestor = TransformarEmGestorService()

    user = transformaremgestor.execute(userData)

    return jsonify(user)

@blueprint.route("/transformarempropositor", methods=['POST'])
@jwt_required
def transformarempropositor():
    Token = get_jwt_identity()
    if not(Token['adm']):
        return jsonify({"Error": "Você não tem permissão de acessar essa função"}), 400
    userData = request.get_json()
    userDataFields = ["id"]

    if not all(field in userData for field in userDataFields):
        return {"Error":"Missing information."}, 400

    transformarempropositor = TransformarEmPropositorService()

    user = transformarempropositor.execute(userData)

    return jsonify(user)

@blueprint.route("/transformaremapoiador", methods=['POST'])
@jwt_required
def transformaremapoiador():
    Token = get_jwt_identity()
    if not(Token['adm'] or Token['coordenador'] or Token['propositor'] or Token['gestor']):
        return jsonify({"Error": "Você não tem permissão de acessar essa função"}), 400
    userData = request.get_json()
    userDataFields = ["id"]

    if not all(field in userData for field in userDataFields):
        return {"Error":"Missing information."}, 400

    transformaremapoiador = TransformarEmApoiadorService()

    user = transformaremapoiador.execute(userData)

    return jsonify(user)


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
        return jsonify({"Error": "Missing JSON in request"}), 400

    usuario = request.json.get('usuario', None)
    senha = request.json.get('senha', None)
    if not usuario:
        return jsonify({"Error": "Missing usuario parameter"}), 400
    if not senha:
        return jsonify({"Error": "Missing senha parameter"}), 400
    authenticateUser = AutheticateUserService()
    response = authenticateUser.execute(usuario, senha)
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

    userDataFields = ["usuario", "nome", "email", "senha", "cpf", "telefone", "funcao", "profissao", "UnidadeBasicadeSaude", "CAP"]

    if not all(field in userData for field in userDataFields):
        return {"Error":"Missing information."}, 400

    createUser = CreateUserService()

    user = createUser.execute(userData)

    return jsonify(user)

@blueprint.route("/atualizarusuario", methods=['POST'])
@jwt_required
def atualizarusuario():

    #Não testado a parte dos Json
    userDataID = get_jwt_identity()
    userData = request.get_json()
    userDataFields = ["usuario", "nome", "email", "senha", "cpf", "telefone", "funcao", "profissao", "UnidadeBasicadeSaude", "CAP"]
    
    if not all(field in userData for field in userDataFields):
        return {"Error":"Missing information."}, 400

    userData['id'] = userDataID['id']

    atualizaruser = AtualizarUserService()

    User = atualizaruser.execute(userData)

    return jsonify(User)


#TODO: estruturar como será a segunda parte do cadastramento de informações
@blueprint.route("/cadastrardadoscomplementares", methods=['POST'])
@jwt_required
def cadastrarDadosComplementares():
    pass


@blueprint.route("/cadastrarturma", methods=['POST'])
@jwt_required
def cadastrarturma(): 

    Token = get_jwt_identity()
    if not(Token['adm'] or Token['coordenador'] or Token['propositor'] or Token['gestor']):
        return jsonify({"Error": "Você não tem permissão de acessar essa função"}), 400

    turmaData = request.get_json()
    turmaDataFields = ["responsavel", "nome_do_curso",
                       "carga_horaria_total", "tolerancia", "modalidade"]


    if not all(field in turmaData for field in turmaDataFields):
        return {"Error":"Missing information."}, 400

    createTurma = CreateTurmaService()

    turma = createTurma.execute(turmaData)

    return jsonify(turma)


@blueprint.route("/adicionarpublico", methods=['POST'])
@jwt_required
def adicionarpublico(): 

    Token = get_jwt_identity()
    if not(Token['adm'] or Token['coordenador'] or Token['propositor'] or Token['gestor']):
        return jsonify({"Error": "Você não tem permissão de acessar essa função"}), 400

    turmaData = request.get_json()
    turmaDataFields = ["nome_do_curso", "publico_alvo"]


    if not all(field in turmaData for field in turmaDataFields):
        return {"Error":"Missing information."}, 400

    turmaData['responsavel'] = Token['id']	

    adicionarpublico = AdicionarPublicoService()

    publico = adicionarpublico.execute(turmaData)

    return jsonify(publico)



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


@blueprint.route("/listausuario", methods=['GET'])
@jwt_required
def listarusuarios():
    Token = get_jwt_identity()
    if not(Token['adm'] or Token['coordenador'] or Token['propositor'] or Token['gestor']):
        return jsonify({"Error": "Você não tem permissão de acessar essa função"}), 400
    ListUser = ListUserService()
    usuarios = ListUser.execute()
    return jsonify(usuarios)


@blueprint.route("/listaturmaapoiador", methods=['Post'])
@jwt_required
def listarturmaapoiador():
    apoiadorData = request.get_json()
    apoiadorDataFields = ["usuario"]

    if not all(field in apoiadorData for field in apoiadorDataFields):
        return {"Error":"Missing information."}, 400

    ListTurma = ListTurmaApoiadorService()
    Turma = ListTurma.execute(apoiadorData)
    return jsonify(Turma)

@blueprint.route("/listaraulas", methods=['Post'])
@jwt_required
def listaraulas():
    turmaData = request.get_json()
    turmaDataFields = ["nome_do_curso"]

    if not all(field in turmaData for field in turmaDataFields):
        return {"Error":"Missing information."}, 400

    ListAula = ListAulaService()
    Aulas = ListAula.execute(turmaData)
    return jsonify(Aulas)



@blueprint.route("/listarPresencaTotal", methods=['Post'])
@jwt_required
def listarPresencaTotal():
    turmaData = request.get_json()
    turmaDataFields = ["nome_do_curso"]

    if not all(field in turmaData for field in turmaDataFields):
        return {"Error":"Missing information."}, 400

    ListPresencas = ListPresencaTotalService()
    Presencas = ListPresencas.execute(turmaData)
    return jsonify(Presencas)

@blueprint.route("/listaturmaaluno", methods=['Post'])
@jwt_required
def listaturmaaluno():
    alunoData = request.get_json()
    alunoDataFields = ["usuario"]

    if not all(field in alunoData for field in alunoDataFields):
        return {"Error":"Missing information."}, 400

    ListTurma = ListTurmaAlunoService()
    Turma = ListTurma.execute(alunoData)
    return jsonify(Turma)

@blueprint.route("/listaturmapropositor", methods=['Post'])
@jwt_required
def listaturmapropositor():
    propositorData = request.get_json()
    propositorDataFields = ["usuario"]

    if not all(field in propositorData for field in propositorDataFields):
        return {"Error":"Missing information."}, 400

    ListTurma = ListTurmaPropositorService()
    Turma = ListTurma.execute(propositorData)
    return jsonify(Turma)


@blueprint.route("/marcarpresenca", methods=['POST'])
@jwt_required
def atualizarpresenca():
    presencaData = request.get_json()
    presencaDataFields = ["emailAluno","id_aula"]

    if not all(field in presencaData for field in presencaDataFields):
        return {"Error":"Bad Request"}, 400

    marcarPresenca = CreatePresencaService()
    presenca = marcarPresenca.execute(presencaData)
    return jsonify(presenca)


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
        return {"Error":"Missing information."}, 400

    cadastroData['id'] = userData['id']

    cadastrarAlunoNaTurma = CadastrarAlunoService()

    msg = cadastrarAlunoNaTurma.execute(cadastroData)

    return jsonify(msg)

# Issue 36

@blueprint.route("/cadastrarapoiador", methods=['POST'])
@jwt_required
def cadastrarapoiador():

    Token = get_jwt_identity()
    if not(Token['adm'] or Token['coordenador'] or Token['propositor'] or Token['gestor']):
        return jsonify({"Error": "Você não tem permissão de acessar essa função"}), 400

    apoiadorData = request.get_json()
    apoiadorDataFields = ["email_apoiador", "id_turma"]
  
    if not all(field in apoiadorData for field in apoiadorDataFields):
        return {"Error":"Missing information."}, 400

    apoiadorData['idDoPropositor'] = Token['id']
  
    cadastrarApoiador = CreateApoiadorService()

    msg = cadastrarApoiador.execute(apoiadorData)
    return jsonify(msg)

@blueprint.route("/deletarapoiador", methods=['POST'])
@jwt_required
def deletarapoiador():

    Token = get_jwt_identity()
    if not(Token['adm'] or Token['coordenador'] or Token['propositor'] or Token['gestor']):
        return jsonify({"Error": "Você não tem permissão de acessar essa função"}), 400

    deleteData = request.get_json()
    deleteDataFields = ["cpfApoiador", "idTurma"]


    if not all(field in deleteData for field in deleteDataFields):
        return {"Error":"Missing information."}, 400

    deleteData['idDoPropositor'] = Token['id']

    deleteApoiador = DeleteApoiadorService()

    msg = deleteApoiador.execute(deleteData)

    return jsonify(msg)


@blueprint.route("/deletaraluno", methods=['POST'])
@jwt_required
def deletaraluno():

    Token = get_jwt_identity()
    if not(Token['adm'] or Token['coordenador'] or Token['propositor'] or Token['gestor']):
        return jsonify({"Error": "Você não tem permissão de acessar essa função"}), 400

    deleteData = request.get_json()
    deleteDataFields = ["cpfAluno", "idTurma"]


    if not all(field in deleteData for field in deleteDataFields):
        return {"Error":"Missing information."}, 400

    deleteData['idDoPropositor'] = Token['id']

    deleteAluno = DeleteAlunoService()

    msg = deleteAluno.execute(deleteData)

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
        return {"Error":"Missing information."}, 400

    horarioData['idPropositor'] = user['id']

    cadastrarHorario = CreateHorarioService()
    response = cadastrarHorario.execute(horarioData)
    
    return jsonify(response)

@blueprint.route("/cadastraraula", methods=['POST'])
@jwt_required
def cadastraraula():
    # Não testado a parte dos Json

    AulaData = request.get_json()
    AulaDataFields = ["nome_do_curso", "nome_da_aula", "hInicio", "hTermino"]

    user = get_jwt_identity()
    
    if not all(field in AulaData for field in AulaDataFields):
        return {"Error":"Missing information."}, 400

    #horarioData['idPropositor'] = user['id']

    cadastrarAula = CreateAulaService()
    response = cadastrarAula.execute(AulaData)
    
    return jsonify(response)

@blueprint.route("/autocadastro",methods=['POST'])
@jwt_required
def autocadastro():
    cadastroData=request.get_json()
    cadastroDataFields = ["cpf","tokenTurma"]

    if not all(field in cadastroData for field in cadastroDataFields):
        return {"Error":"Missing information."}, 400

    cadastraraluno=CadastrarAlunoService().executeAluno(cadastroData)
    return cadastraraluno

@blueprint.route('/getHorarios', methods=['GET'])
@jwt_required
def get_horarios():
    if not request.is_json:
        return jsonify({"Error": "Missing JSON in request"}), 400
    
    session = get_session()
    turma_id = request.get_json()
    Horarios = session.query(Horario).filter_by(HorarioIdTurma=turma_id["TurmaID"]).all()
    if not Horarios:
        return jsonify({"Error":"Não há nenhum horario cadastrado para esta turma"}), 400

    response = [horario.as_dict() for horario in Horarios]
    return jsonify(response)


#AINDA NÃO TERMINADA
@blueprint.route("/chamadavalidar", methods=['GET','POST'])
@jwt_required
def chamadavalidar():
    if request.method == 'POST':
        if not request.is_json:
           return jsonify({"Error": "Missing JSON in request"}), 400
        
        user = get_jwt_identity()
        session = get_session()
        checkCargo = session.query(User).filter_by(Id=user["id"],usuario=user["usuario"]).one().as_dict()
        if checkCargo["tipo"]=='cursista' or checkCargo["tipo"]=='apoiador':
            return jsonify({"Error": "Cargo não autorizado"})
        
        validacao = makeValidacao().execute(request.get_json())
    
        return jsonify(validacao)

    elif request.method == 'GET':
        if not request.is_json:
           return jsonify({"Error": "Missing JSON in request"}), 400
        user = get_jwt_identity()
        session = get_session()
        dadosTurma = request.get_json()

        getChamada = session.query(Presenca).filter_by(presencaValidade=0,presenca_id_turma=dadosTurma['idTurma']).all()

        response = [i.as_dict() for i in getChamada]
        return jsonify(response)    

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
    Turmas = session.query(Turma,Aluno).filter(Aluno.id_aluno == PresencaTot.presencatot_id_aluno, PresencaTot.presencatot_id_turma == Turma.id_turma).all()
    if not Turma:
        return jsonify({"Error":"Ocorreu um erro na base de dados"})

    response = [frequenciaTurma(i) for i in Turmas]

    for (i,j) in zip(Turmas,response):
        for z in i.Alunos:
            j['Alunos'].append(frequencia(z))

    session.close()
    return jsonify(response)

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
