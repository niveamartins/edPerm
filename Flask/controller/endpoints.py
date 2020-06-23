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
from services.CreateComplementoService import CreateComplementoService
from services.CreateAlunoService import CreateAlunoService
from services.CreateApoiadorService import CreateApoiadorService
from services.CreateHorarioService import CreateHorarioService
from services.AutheticateUserService import AutheticateUserService
from services.ListTurmaService import ListTurmaService

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
    access_token = authenticateUser.execute(usuario, senha)

    return jsonify(access_token=access_token), 200


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

@blueprint.route('/qrcode/<int:codigo_aluno>', methods=['GET'])
@jwt_required
def gerarqrcode(codigo_aluno):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    session = get_session()
    data = session.query(Aluno).filter_by(id_aluno=codigo_aluno).one()
    JSON = data.alunoUser.as_dict()
    qr.add_data(JSON)
    qr.make(fit=True)
    img = qr.make_image()
    url = path.abspath(__file__).split('controller')[0]
    img.save(url+f'{codigo_aluno}.png')

    return send_file(url+f'{codigo_aluno}.png', mimetype='image/png')

@blueprint.route("/cadastrar", methods=['POST'])
@jwt_required
def cadastrar():

    userData = request.get_json()
    userDataFields = ["usuario", "email", "senha", "cpf", "telefone", "tipo", "cap", "funcao", "profissao"]

    if not all(field in userData for field in userDataFields):
        return "Missing information", 400

    createUser = CreateUserService()

    user = createUser.execute(userData)

    return jsonify(user)

# refatorado


@blueprint.route("/cadastrardadoscomplementares", methods=['POST'])
@jwt_required
def cadastrarDadosComplementares():

    # Não testado a parte dos Json

    complementoData = request.get_json()

    complementoDataFields = ["usuario", "tag", "profissao", "funcao",
                             "superintendenciaDaSUBPAV", "CAP", "unidadeBasicaDeSaude"]

    if not all(field in complementoData for field in complementoDataFields):
        return "Missing information", 400

    createComplemento = CreateComplementoService()

    Complemento = createComplemento.execute(complementoData)

    return jsonify(Complemento)


# refatorado
@blueprint.route("/cadastrarturma", methods=['POST'])
@jwt_required
def cadastrarturma():

    # Não testado a parte dos Json

    turmaData = request.get_json()
    turmaDataFields = ["responsavel", "nome_do_curso",
                       "carga_horaria_total", "tolerancia", "modalidade", "turma_tag"]

    # if not all(field in turmaData for field in turmaDataFields):
    #     return "Missing information", 400

    createTurma = CreateTurmaService()
    print(turmaData)
    turma = createTurma.execute(turmaData)
    print(turma)
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
@jwt_required
def listarturma():
    #user_id = request.json.get('user_id', None)

    listTurma = ListTurmaService()
    turmas = listTurma.execute()
    print(turmas)
    return jsonify(turmas)





@blueprint.route("/atualizarpresenca", methods=['POST'])
@jwt_required
def atualizarpresenca():
    pass

@blueprint.route("/cadastraraluno", methods=['POST'])
@jwt_required
def cadastraraluno(): 

    #Não testado a parte dos Json

    cadastroData = request.get_json()
    cadastroDataFields = ["usuario", "nome_do_curso"]

    # if not all(field in cadastroData for field in cadastroDataFields):
    #     return "Missing information", 400

    cadastrarAluno = CreateAlunoService()

    Aluno = cadastrarAluno.execute(cadastroData)

    return jsonify(Aluno)


@blueprint.route("/cadastrarapoiador", methods=['POST'])
@jwt_required
def cadastrarapoiador():

    # Não testado a parte dos Json

    apoiadorData = request.get_json()
    apoiadorDataFields = ["usuario", "nome_do_curso"]

    if not all(field in apoiadorData for field in apoiadorDataFields):
        return "Missing information", 400

    cadastrarApoiador = CreateApoiadorService()

    Apoiador = cadastrarApoiador.execute(apoiadorData)
    return jsonify(Apoiador)


@blueprint.route("/cadastrarhorario", methods=['POST'])
@jwt_required
def cadastrarhorario():
    # Não testado a parte dos Json

    horarioData = request.get_json()
    horarioDataFields = ["Turma", "DiaDaSemana",
                         "Inicio", "Termino", "Propositor"]
    user = get_jwt_identity()
    if(user['tipo']!='propositor'):
        return "Usuario não tem permissão", 400

    horarioData['Propositor'] = user['usuario']

    if not all(field in horarioData for field in horarioDataFields):
        return "Missing information"

    cadastrarHorario = CreateHorarioService()
    Horario = cadastrarHorario.execute(horarioData)
    erros = ["Turma não cadastrada", "Horario ja cadastrado"]
    for er in erros:
        if(Horario == er):
            return Horario

    return jsonify(Horario)

#AINDA NÃO TERMINADA
@blueprint.route("/chamadavalidar", methods=['POST'])
@jwt_required
def chamadapesquisar():
    pass
    #if not request.is_json:
    #   return jsonify({"msg": "Missing JSON in request"}), 400
     

### RELATORIOS ###

# RELATORIO CONTATO
@blueprint.route('/relatoriocontato', methods=['GET'])
@jwt_required
@cross_origin(origin="localhost")
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
    '''
    Frequência: frequência computada em dias, horas e minutos com base no horário de check-in do cursista.
    Ele poderá acompanhar a própria carga-horária com base na tolerância informada pelo propositor da atividade.
    '''
    session = get_session()
    data = session.query(Aluno).all()
    JSON = [frequencia(i) for i in data]

    session.close()
    return jsonify()

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
        UserComplemento1 = UserComplemento(user=User1, tag="naosei1", profissao="advogado",
                                           funcao="direcao", superintendenciaDaSUBPAV="SIAP", CAP="1.0", unidadeBasicaDeSaude="1")
        UserComplemento2 = UserComplemento(user=User2, tag="naosei2", profissao="medico",
                                           funcao="direcao", superintendenciaDaSUBPAV="SAP", CAP="1.0", unidadeBasicaDeSaude="1")
        UserComplemento3 = UserComplemento(user=User3, tag="naosei3", profissao="engenheiro",
                                           funcao="gerencia", superintendenciaDaSUBPAV="SVS", CAP="1.0", unidadeBasicaDeSaude="1")
        UserComplemento4 = UserComplemento(user=User4, tag="naosei4", profissao="pedreiro",
                                           funcao="gerencia", superintendenciaDaSUBPAV="SPS", CAP="1.0", unidadeBasicaDeSaude="1")
        Aluno1 = Aluno(alunoUser=User1, complementoUser=UserComplemento1)
        Aluno2 = Aluno(alunoUser=User3, complementoUser=UserComplemento3)
        Aluno3 = Aluno(alunoUser=User2, complementoUser=UserComplemento2)
        Aluno4 = Aluno(alunoUser=User4, complementoUser=UserComplemento4)
        session.add_all([Aluno1, Aluno2, Aluno3, Aluno4, UserComplemento1,
                         UserComplemento2, UserComplemento3, UserComplemento4, Turma1, Turma2])
        session.commit()
        Turma1.Alunos.append(Aluno1)
        Turma1.Alunos.append(Aluno2)
        Turma2.Alunos.append(Aluno1)
        session.commit()
        if (User5.Aluno != None):
            print("aaa")
        if (User4.Aluno != None):
            print("fasfasga")
        for x in Turma1.Alunos:
            a = session.query(User).filter_by(Id=x.alunos_id_user).first()
            print(a.usuario)
        logger.info("informações de teste inseridas no banco de dados")
        return "200OK"
    except InternalError:
        logger.error("Banco de dados (EdPermanente) desconhecido")
        return "502ERROR"
