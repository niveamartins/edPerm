import sys

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

    usuarioDoUser = str(request.form["usuario"]).title()
    emailDoUser = str(request.form["email"]).title()
    senhaDoUser = str(request.form["senha"]).title()
    CpfDoUser = str(request.form["cpf"]).title()
    TelefoneDoUser = str(request.form["telefone"]).title()
    TipoDoUser = str(request.form["tipo"]).title()

    userData = {"usuario":usuarioDoUser, "email":emailDoUser, "senha":senhaDoUser, "cpf":CpfDoUser, "telefone":TelefoneDoUser, "tipo":TipoDoUser}
    
#na versão final descomentar os comentarios abaixo e trocar o return e apagar tudo acima desse comentario
#    userData = request.get_json()
    userDataFields = ["usuario", "email", "senha", "cpf", "telefone", "tipo"]

    if not all(field in userData for field in userDataFields):
        return "Missing information", 400

    createUser = CreateUserService()

    user = createUser.execute(userData)

    return "Cadastrou o usuario"
#    return jsonify(user)


@blueprint.route("/cadastrardadoscomplementares", methods=['POST'])
def cadastrarDadosComplementares():
    usuarioDoUser = str(request.form["usuario"]).title()
    tagDoComplemento = str(request.form["tag"]).title()
    profissaoDoComplemento = str(request.form["profissao"]).title()
    funcaoDoComplemento = str(request.form["funcao"])
    superentendenciaDoComplemento = str(request.form["superentendencia"]).title()
    capDoComplemento = str(request.form["cap"]).title()
    unidadeDoComplemento = str(request.form["unidade"])

    complementoData = {"usuario":usuarioDoUser, "tag":tagDoComplemento, "profissao":profissaoDoComplemento, "funcao":funcaoDoComplemento, "superintendenciaDaSUBPAV":superentendenciaDoComplemento, "CAP":capDoComplemento, "unidadeBasicaDeSaude":unidadeDoComplemento}
    
#na versão final descomentar os comentarios abaixo e trocar o return e apagar tudo acima desse comentario
#    complementoData = request.get_json()

    complementoDataFields = ["usuario", "tag", "profissao", "funcao", "superintendenciaDaSUBPAV", "CAP", "unidadeBasicaDeSaude"]

    if not all(field in complementoData for field in complementoDataFields):
        return "Missing information", 400

    createComplemento = CreateComplementoService()

    Complemento = createComplemento.execute(complementoData)

    return "Atualização dos dados do usuario completa"
#    return jsonify(user)

 

#    if cadastrado:
#        session['tag'] = tag
#        session['profissao'] = profissao
#        session['superentendencia'] = superentendencia
#        session['cap'] = cap
#        session['unidade'] = unidade
#        return redirect('/')
#    else:
#        return render_template('cadastro.html', erro_cad=True)


@blueprint.route("/cadastrardadospessoais", methods=['POST'])
def cadastrarDadosPessoais():
#Vai morrer
    nome = str(request.form["nome"]).title()
    cpf = str(request.form["cpf"]).title()
    telefone = str(request.form["telefone"])

    banco = Banco()

    if (banco.buscarDadosPessoais(session['user_id']) == []):
        cadastrado = banco.cadastrar_dados_pessoais(
            session['user_id'], nome, cpf, telefone)
    else:
        banco.atualizarNome(session['user_id'], tag)
        banco.atualizarCpf(session['user_id'], profissao)
        banco.atualizarTelefone(session['user_id'], funcao)
        return 'Dados Pessoais atualizado'
    if cadastrado:
        return redirect('/')
    else:
        return render_template('cadastro.html', erro_cad=True)


@blueprint.route("/cadastrarturma", methods=['POST'])
def cadastrarturma():
    variavelResponsavel = str(request.form["responsavel"]).title()
    variavelNome = str(request.form["nome"]).title()
    variavelCarga = str(request.form["carga"]).title()
    variavelTolerancia = str(request.form["tolerancia"]).title()
    variavelModalidade = str(request.form["modalidade"]).title()
    variavelTag = str(request.form["tag"]).title()
    
    turmaData = {"responsavel":variavelResponsavel, "nome_do_curso":variavelNome, "carga_horaria_total":variavelCarga, "tolerancia":variavelTolerancia, "modalidade":variavelModalidade, "turma_tag":variavelTag}
    
#na versão final descomentar os comentarios abaixo e trocar o return e apagar tudo acima desse comentario
#    turmaData = request.get_json()
    turmaDataFields = ["responsavel", "nome_do_curso", "carga_horaria_total", "tolerancia", "modalidade", "turma_tag"]

    if not all(field in turmaData for field in turmaDataFields):
        return "Missing information", 400

    createTurma = CreateTurmaService()

    turma = createTurma.execute(turmaData)

    return "Cadastrou a turma"
#    return jsonify(turma)    



@blueprint.route("/cadastraralunonaturma", methods=['POST'])
def cadastraralunonaturma():
    variavelAluno = str(request.form["aluno"])
    variavelTurma = str(request.form["codigo"])

    banco = Banco()
    if (banco.buscarTurma(variavelTurma) != []):
        variavelTurma = banco.buscarTurma(variavelTurma)
        if(banco.buscarAluno(variavelAluno) != []):
            variavelAluno = banco.buscarAluno(variavelAluno)
            if(banco.buscarAlunoPorUsuarioECodigo(str(request.form["aluno"]), str(request.form["codigo"])) == []):
                cadastrado = banco.cadastrarAlunos(
                    variavelTurma[0], variavelAluno[0])
            else:
                return 'Aluno ja cadastrado na turma'
        else:
            return 'Aluno não existe'
    else:
        return 'Turma não existe'
    if cadastrado:
        return render_template('cadastroalunonaturma.html', erro_cad=False)
    else:
        return render_template('cadastroalunonaturma.html', erro_cad=True)


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


@blueprint.route("/atualizarpresenca", methods=['POST'])
def atualizarpresenca():
    variavelAluno = str(request.form["alunopre"])

    banco = Banco()

    if (banco.buscarTurma(session['nome_da_turma']) != []):
        if(banco.buscarApoiadorPorUsuarioECodigo(session['user'], session['nome_da_turma']) != []):
            if(banco.buscarAulaPorTurmaENome(session['nome_da_turma'], session['aula']) != []):
                if(banco.buscarAlunoPorUsuarioECodigo(variavelAluno, session['nome_da_turma']) != []):
                    if(banco.buscarPresencaPorUsuarioEAula(variavelAluno, session['aula']) == []):
                        variavelAluno = banco.buscarAlunoPorUsuarioECodigo(
                            variavelAluno, session['nome_da_turma'])
                        variavelUsuario = banco.buscarAluno(
                            str(request.form["alunopre"]))
                        variavelAula = banco.buscarAulaPorTurmaENome(
                            session['nome_da_turma'], session['aula'])
                        inicio = int(variavelAula[0][2])
                        fim = int(variavelAula[0][3])
                        horarioDaPresenca = banco.retornaHorarioNow()
                        horarioDaPresenca = int(horarioDaPresenca[0][0])
                        cadastrado = banco.cadastrarPresenca(
                            variavelUsuario[0], variavelAula[0], horarioDaPresenca)
                        if cadastrado:
                            if(horarioDaPresenca < inicio):
                                presenca = int(
                                    variavelAluno[0][3]) + fim - inicio
                            else:
                                if(horarioDaPresenca > fim):
                                    presenca = int(variavelAluno[0][3])
                                else:
                                    presenca = int(
                                        variavelAluno[0][3]) + fim - horarioDaPresenca
                            cadastrado = banco.atualizarAlunos(
                                variavelAluno[0][0], presenca)
                    else:
                        return 'Aluno já possui presença nessa aula'
                else:
                    return 'Aluno não existe'
            else:
                return 'Aula não existe'
        else:
            return 'Você não é apoiador dessa turma'
    else:
        return 'Turma não existe'

    if cadastrado:
        return render_template('atualizarpresencaaluno.html', erro_cad=False)
    else:
        banco.apagarPresenca(variavelUsuario[0], variavelAula[0])
        return render_template('atualizarpresencaaluno.html', erro_cad=True)


@blueprint.route("/cadastraraluno", methods=['POST'])
def cadastraraluno():
    variavelAluno = session['user']
    variavelTurma = session['nome_da_turma']

    banco = Banco()
    if (banco.buscarTurma(variavelTurma) != []):
        variavelTurma = banco.buscarTurma(variavelTurma)
        if(banco.buscarAluno(variavelAluno) != []):
            variavelAluno = banco.buscarAluno(variavelAluno)
            if(banco.buscarAlunoPorUsuarioECodigo(session['user'], session['nome_da_turma']) == []):
                cadastrado = banco.cadastrarAlunos(
                    variavelTurma[0], variavelAluno[0])
            else:
                session['nome_da_turma'] = ''
                return 'Aluno ja cadastrado na turma'
        else:
            session['nome_da_turma'] = ''
            return 'Aluno não existe'
    else:
        session['nome_da_turma'] = ''
        return 'Turma não existe'
    if cadastrado:
        session['nome_da_turma'] = ''
        return render_template('inicio.html', erro_cad=False)
    else:
        session['nome_da_turma'] = ''
        return render_template('inicio.html', erro_cad=True)


@blueprint.route("/cadastrarapoiador", methods=['POST'])
def cadastrarapoiador():
    variavelAluno = str(request.form["aluno"])
    variavelTurma = str(request.form["turma"])

    banco = Banco()
    if (banco.buscarTurma(variavelTurma) != []):
        variavelTurma = banco.buscarTurma(variavelTurma)
        if(banco.buscarAluno(variavelAluno) != []):
            variavelAluno = banco.buscarAluno(variavelAluno)
            if(banco.buscarApoiadorPorUsuarioECodigo(str(request.form["aluno"]), str(request.form["turma"])) == []):
                cadastrado = banco.cadastrarAlunoApoiador(
                    variavelTurma[0], variavelAluno[0])
            else:
                return 'Aluno ja cadastrado como apoiador da turma'
        else:
            return 'Aluno não existe'
    else:
        return 'Turma não existe'
    if cadastrado:
        return render_template('cadastroapoiador.html', erro_cad=False)
    else:
        return render_template('cadastroapoiador.html', erro_cad=True)


@blueprint.route("/cadastraraula", methods=['POST'])
def cadastraraula():
    banco = Banco()
    variavelturma = str(request.form["turma"])
    variavelaula = str(request.form["aula"])
    horario = str(request.form["horario"])
    termino = str(request.form["termino"])
    horario = horario[:10] + ' ' + horario[11:] + ':00'
    termino = termino[:10] + ' ' + termino[11:] + ':00'
    teste1 = banco.retornaHorario(horario)
    teste2 = banco.retornaHorario(termino)
    teste3 = banco.retornaHorarioNow()
    teste1 = int(teste1[0][0])
    teste2 = int(teste2[0][0])
    teste3 = int(teste3[0][0])
    if(teste1 >= teste2 or teste3 >= teste2):
        return 'Horario invalido'

    if (banco.buscarTurma(variavelturma) != []):
        variavelTurma = banco.buscarTurma(variavelturma)
        if(banco.buscarAulaPorTurmaENome(variavelturma, variavelaula) == []):
            cadastrado = banco.cadastrarAula(
                variavelTurma[0], teste1, teste2, variavelaula)
        else:
            return 'Aula Ja cadastrada'
    else:
        return 'Turma não existe'
    if cadastrado:
        return render_template('cadastroapoiador.html', erro_cad=False)
    else:
        return render_template('cadastroapoiador.html', erro_cad=True)


@blueprint.route("/chamadapesquisar", methods=['POST'])
def chamadapesquisar():
    variavelTurma = str(request.form["turma"])
    variavelAula = str(request.form["aula"])

    banco = Banco()
    if (banco.buscarTurma(variavelTurma) != []):
        if(banco.buscarApoiadorPorUsuarioECodigo(session['user'], variavelTurma) != []):
            if(banco.buscarAulaPorTurmaENome(variavelTurma, variavelAula) != []):
                session['aula'] = variavelAula
                session['nome_da_turma'] = variavelTurma
                return render_template('atualizarpresencaaluno.html', erro_cad=False)
            else:
                return 'Aula não existe'
        else:
            return 'Você não é apoiador dessa turma'
    else:
        return 'Turma não existe'

### RELATORIOS ###

#RELATORIO CONTATO
@blueprint.route('/relatoriocontato', methods=['GET'])
def get_relatoriocontato():
    session = get_session()
    data = session.query(User).all()
    logger.debug(f'Query: {str(session.query(User))}')
    data = [relatoriocontato(i) for i in data]
    session.close()
    return jsonify(data)

#RELATORIO CPF/NOME
@blueprint.route('/relatoriocpfnome', methods = ['GET'])
def get_relatoriocpfnome():
    session = get_session()
    data = session.query(Turma).all()
    logger.debug(f'Query: {str(session.query(Turma))}')
    JSON = [Rcpfnome(i) for i in data]
    for (i, j) in zip(data, JSON):
        for z in i.Alunos:
            j["alunos"].append(RcpfnomeAlunos(z))
    session.close()
    return jsonify(JSON)

#RELATORIO FREQUENCIA
@blueprint.route('/relatoriofrequencia', methods = ['GET'])
def get_relatoriofrequencia():
    session = get_session()

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
        session.add_all([User1, User2, User3])
        session.commit()
        Turma1 = Turma(id_responsavel=User2.Id,nome_do_curso="calculo",IsConcluido=0,carga_horaria_total=60,tolerancia=30,modalidade="n sei",turma_tag="tbm n sei")
        Turma2 = Turma(id_responsavel=User2.Id,nome_do_curso="iot",IsConcluido=1,carga_horaria_total=60,tolerancia=30,modalidade="n sei",turma_tag="tbm n sei")
        UserComplemento1 = UserComplemento(user=User1,tag="naosei1",profissao="coach",funcao="direcao",superintendenciaDaSUBPAV="ZAP",CAP="1.0",unidadeBasicaDeSaude="1")
        UserComplemento2 = UserComplemento(user=User2,tag="naosei1",profissao="bundao",funcao="direcao",superintendenciaDaSUBPAV="SAP",CAP="1.0",unidadeBasicaDeSaude="1")
        UserComplemento3 = UserComplemento(user=User3,tag="naosei1",profissao="coach",funcao="gerencia",superintendenciaDaSUBPAV="SAP",CAP="1.0",unidadeBasicaDeSaude="1")
        Aluno1 = Aluno(alunoUser=User1, complementoUser=UserComplemento1)
        Aluno2 = Aluno(alunoUser=User3, complementoUser=UserComplemento3)
        session.add_all([Aluno1,Aluno2,UserComplemento1,UserComplemento2,UserComplemento3,Turma1,Turma2])
        session.commit()
        Turma1.Alunos.append(Aluno1)
        Turma1.Alunos.append(Aluno2)
        Turma2.Alunos.append(Aluno1)
        session.commit()
        logger.info("informações de teste inseridas no banco de dados")
        return "200OK"
    except InternalError:
        logger.error("Banco de dados (EdPermanente) desconhecido")
        return "502ERROR"
