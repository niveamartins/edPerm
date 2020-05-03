from flask import Flask, request, render_template, redirect, url_for, session, jsonify
import os, smtplib
from db_create import Banco
from pessoas import Pessoa
from BD.session import get_session 
from BD.model.User import User
#from geradordeqrcode import Gerador

app = Flask(__name__)


@app.route("/")
def login():
    return render_template('login.html')

@app.route("/esqueci_a_senha")
def esqueci_a_senha():
    return render_template('esqueci_a_senha.html')

@app.route("/esqueci", methods = ['POST'])
def esqueci_():
    email = request.form['email']
    banco = Banco()

    banco.recuperarSenha(email)
    return redirect('/esqueci_a_senha')

@app.route("/logar", methods = ['POST'])
def logar():
    
    usr = str(request.form["usuario"]).title()
    senha = str(request.form["senha"])

    banco = Banco()
    busca =  banco.buscar_pessoa(usr, senha)
    visitante = Pessoa()
    if len(busca) > 0:    
        x = busca[0]
        id = x[0]
        usuario = x[1]
        email = x[2]
        adm = x[4]
        gestor = x[5]
        coordenador = x[6]
        propositor = x[7]
        cursista = x[8]
        apoiador = x[9]
        visitante.iniciar(id, usuario, senha, email, adm, gestor, coordenador, propositor, cursista, apoiador)

        busca2 =  banco.buscarDadosComplementares(session['user_id'])
        if len(busca2) > 0:
            y = busca2[0]
            tag = y[2]
            profissao = y[3]
            funcao = y[4]
            superentendencia = y[5]
            cap = y[6]
            unidade = y[7]
            session['tag'] = tag
            session['profissao'] = profissao
            session['profissao'] = funcao
            session['superentendencia'] = superentendencia
            session['cap'] = cap
            session['unidade'] = unidade


        session['logged_in'] = True
        visitante.validar()
    else:
        session['logged_in'] = False
    
    try:
        if session['logged_in']:
            return redirect('/listaturma')
        else:
            return render_template('login.html', erro_log = True)
    except:
        return "Concerte isso"

@app.route("/sair")
def sair():
    session['logged_in'] = False
    session['user'] = ""
    session['user_id'] = ""
    return redirect('/')

@app.route("/cadastro")
def cadastro():
    return render_template('cadastro.html')

@app.route("/cadastrar", methods = ['POST'])
def cadastrar():
    variavel_turma_id_user = str(request.form["usuario"]).title()
    email = str(request.form["email"]).title()
    senha = str(request.form["senha"])
    
    banco = Banco()
    if (banco.buscar_pessoa(variavel_turma_id_user, senha) == []):
        cadastrado =  banco.cadastrar_pessoa(variavel_turma_id_user, senha, email)
    else:
        return 'usuário já existente'
    if cadastrado:
        busca =  banco.buscar_pessoa(variavel_turma_id_user, senha)
        if len(busca) > 0:  
            x = busca[0]  
            id = x[0]
            usuario = x[1]
        print(id)
        print(usuario)
        qr = Gerador()
        qr.gerarQrcode(id,usuario)
        return redirect('/')
    else:
        return render_template('cadastro.html', erro_cad = True)

@app.route("/cadastrodadoscomplementares")
def cadastroDadosComplementares():
    return render_template('CadastroDadosComplementares.html')

@app.route("/cadastrardadoscomplementares", methods = ['POST'])
def cadastrarDadosComplementares():
    tag = str(request.form["tag"]).title()
    profissao = str(request.form["profissao"]).title()
    funcao = str(request.form["funcao"])
    superentendencia = str(request.form["superentendencia"]).title()
    cap = str(request.form["cap"]).title()
    unidade = str(request.form["unidade"])
    
    banco = Banco()
    print(session['user_id'])
    if (banco.buscarDadosComplementares(session['user_id']) == []):
        cadastrado =  banco.cadastrar_complemento(session['user_id'], tag, profissao, funcao, superentendencia, cap, unidade)
    else:
        banco.atualizarTag(session['user_id'], tag)
        banco.atualizarProfissao(session['user_id'], profissao)
        banco.atualizarFuncao(session['user_id'], funcao)
        banco.atualizarSuperentendencia(session['user_id'], superentendencia)
        banco.atualizarCap(session['user_id'], cap)
        banco.atualizarUnidade(session['user_id'], unidade)
        return 'Complemento atualizado'
    if cadastrado:
        session['tag'] = tag
        session['profissao'] = profissao
        session['profissao'] = funcao
        session['superentendencia'] = superentendencia
        session['cap'] = cap
        session['unidade'] = unidade
        return redirect('/')
    else:
        return render_template('cadastro.html', erro_cad = True)

@app.route("/cadastrodadospessoais")
def cadastroDadosPessoais():
    return render_template('cadastrodadospessoais.html')

@app.route("/cadastrardadospessoais", methods = ['POST'])
def cadastrarDadosPessoais():
    nome = str(request.form["nome"]).title()
    cpf = str(request.form["cpf"]).title()
    telefone = str(request.form["telefone"])
    
    banco = Banco()

    if (banco.buscarDadosPessoais(session['user_id']) == []):
        cadastrado =  banco.cadastrar_dados_pessoais(session['user_id'], nome, cpf, telefone)
    else:
        banco.atualizarNome(session['user_id'], tag)
        banco.atualizarCpf(session['user_id'], profissao)
        banco.atualizarTelefone(session['user_id'], funcao)
        return 'Dados Pessoais atualizado'
    if cadastrado:
        return redirect('/')
    else:
        return render_template('cadastro.html', erro_cad = True)


@app.route("/cadastroturma")
def cadastroturma():
    return render_template('CadastroTurma.html')

@app.route("/cadastrarturma", methods = ['POST'])
def cadastrarturma():
    variavelResponsavel = str(request.form["responsavel"])
    variavelNome = str(request.form["nome"])
    variavelDia =  str(request.form["dia"])
    variavelHora = str(request.form["hora"])
    variavelCarga = str(request.form["carga"])
    variavelTolerancia =  str(request.form["tolerancia"])
    variavelModalidade = str(request.form["modalidade"])
    variavelTag =  str(request.form["tag"])
    
    banco = Banco()
    if (banco.buscarProfessor(variavelResponsavel) != []):
        variavelResponsavel = banco.buscarProfessor(variavelResponsavel)
        cadastrado = banco.cadastrarTurma(variavelResponsavel[0], variavelNome, variavelDia, variavelHora, variavelCarga, variavelTolerancia, variavelModalidade, variavelTag)
    else:
        return 'Responsavel não cadastrado'
    if cadastrado:
        return render_template('CadastroTurma.html', erro_cad = False)
    else:
        return render_template('CadastroTurma.html', erro_cad = True)

@app.route("/cadastroalunonaturma")
def cadastroalunonaturma():
    return render_template('cadastroalunonaturma.html')

@app.route("/cadastraralunonaturma", methods = ['POST'])
def cadastraralunonaturma():
    variavelAluno = str(request.form["aluno"])
    variavelTurma = str(request.form["codigo"])
    
    banco = Banco()
    if (banco.buscarTurma(variavelTurma) != []):
            variavelTurma = banco.buscarTurma(variavelTurma)
            if(banco.buscarAluno(variavelAluno) !=[]):
                 variavelAluno = banco.buscarAluno(variavelAluno)
                 if(banco.buscarAlunoPorUsuarioECodigo(str(request.form["aluno"]), str(request.form["codigo"])) == []):
                     cadastrado = banco.cadastrarAlunos(variavelTurma[0], variavelAluno[0])
                 else:
                     return 'Aluno ja cadastrado na turma'
            else:
                return 'Aluno não existe'
    else:
        return 'Turma não existe'
    if cadastrado:
        return render_template('cadastroalunonaturma.html', erro_cad = False)
    else:
        return render_template('cadastroalunonaturma.html', erro_cad = True)


@app.route("/listaturma")
def listarturma():
    banco = Banco()
    return render_template('listaturma.html', eventos = banco.listarTurma())

@app.route('/listaturma/<string:codigo_turma>')
def turma(codigo_turma):
    session['nome_da_turma'] = codigo_turma
    banco = Banco()
    soualuno = banco.buscarAlunoPorUsuarioECodigo(session['user'], session['nome_da_turma'])
    if(soualuno != []):
        session['inscrito'] = True
    else:
        session['inscrito'] = False
    eventos = banco.buscarTurmaComProfessor(codigo_turma)
    variavel = eventos[0][0]
    alunodaturma = banco.listarAlunos(variavel)
    evento = banco.buscarTurmaComProfessor(codigo_turma)
    return render_template('listaralunosdaturma.html', eventos = evento, alunosdaturma = alunodaturma )


@app.route("/listadepresenca")
def listadepresenca():
    return render_template('atualizarpresencaaluno.html')

@app.route("/atualizarpresenca", methods = ['POST'])
def atualizarpresenca():
    variavelAluno = str(request.form["alunopre"])
    
    banco = Banco()

    if (banco.buscarTurma(session['nome_da_turma']) != []):
            if(banco.buscarApoiadorPorUsuarioECodigo(session['user'], session['nome_da_turma']) != []):
                if(banco.buscarAulaPorTurmaENome(session['nome_da_turma'], session['aula']) != []):
                    if(banco.buscarAlunoPorUsuarioECodigo(variavelAluno, session['nome_da_turma']) != []):
                        if(banco.buscarPresencaPorUsuarioEAula(variavelAluno, session['aula']) == []):
                            variavelAluno = banco.buscarAlunoPorUsuarioECodigo(variavelAluno, session['nome_da_turma'])
                            variavelUsuario = banco.buscarAluno(str(request.form["alunopre"]))
                            variavelAula = banco.buscarAulaPorTurmaENome(session['nome_da_turma'], session['aula'])
                            inicio = int(variavelAula[0][2])
                            fim = int(variavelAula[0][3])
                            horarioDaPresenca = banco.retornaHorarioNow()
                            horarioDaPresenca = int(horarioDaPresenca[0][0])
                            cadastrado = banco.cadastrarPresenca(variavelUsuario[0], variavelAula[0], horarioDaPresenca)
                            if cadastrado:
                                if(horarioDaPresenca<inicio):
                                    presenca = int(variavelAluno[0][3]) + fim - inicio
                                else:
                                    if(horarioDaPresenca>fim):
                                        presenca = int(variavelAluno[0][3])
                                    else:
                                        presenca = int(variavelAluno[0][3]) + fim - horarioDaPresenca
                                cadastrado = banco.atualizarAlunos(variavelAluno[0][0], presenca)
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
        return render_template('atualizarpresencaaluno.html', erro_cad = False)
    else:
        banco.apagarPresenca(variavelUsuario[0], variavelAula[0])
        return render_template('atualizarpresencaaluno.html', erro_cad = True)

@app.route("/cadastraraluno", methods = ['POST'])
def cadastraraluno():
    variavelAluno = session['user']
    variavelTurma = session['nome_da_turma']
    
    banco = Banco()
    if (banco.buscarTurma(variavelTurma) != []):
            variavelTurma = banco.buscarTurma(variavelTurma)
            if(banco.buscarAluno(variavelAluno) !=[]):
                 variavelAluno = banco.buscarAluno(variavelAluno)
                 if(banco.buscarAlunoPorUsuarioECodigo(session['user'], session['nome_da_turma']) == []):
                     cadastrado = banco.cadastrarAlunos(variavelTurma[0], variavelAluno[0])
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
        return render_template('inicio.html', erro_cad = False)
    else:
        session['nome_da_turma'] = ''
        return render_template('inicio.html', erro_cad = True)


@app.route("/cadastroapoiador")
def cadastroapoiador():
    return render_template('cadastroapoiador.html')

@app.route("/cadastrarapoiador", methods = ['POST'])
def cadastrarapoiador():
    variavelAluno = str(request.form["aluno"])
    variavelTurma = str(request.form["turma"])
    
    banco = Banco()
    if (banco.buscarTurma(variavelTurma) != []):
            variavelTurma = banco.buscarTurma(variavelTurma)
            if(banco.buscarAluno(variavelAluno) !=[]):
                 variavelAluno = banco.buscarAluno(variavelAluno)
                 if(banco.buscarApoiadorPorUsuarioECodigo(str(request.form["aluno"]), str(request.form["turma"])) == []):
                     cadastrado = banco.cadastrarAlunoApoiador(variavelTurma[0], variavelAluno[0])
                 else:
                     return 'Aluno ja cadastrado como apoiador da turma'
            else:
                return 'Aluno não existe'
    else:
        return 'Turma não existe'
    if cadastrado:
        return render_template('cadastroapoiador.html', erro_cad = False)
    else:
        return render_template('cadastroapoiador.html', erro_cad = True)

@app.route("/cadastroaula")
def cadastroaula():
    return render_template('horario.html')

@app.route("/cadastraraula", methods = ['POST'])
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
            if(banco.buscarAulaPorTurmaENome(variavelturma, variavelaula) ==[]):
                 cadastrado = banco.cadastrarAula(variavelTurma[0], teste1, teste2, variavelaula)
            else:
                return 'Aula Ja cadastrada'
    else:
        return 'Turma não existe'
    if cadastrado:
        return render_template('cadastroapoiador.html', erro_cad = False)
    else:
        return render_template('cadastroapoiador.html', erro_cad = True)

@app.route("/chamada")
def chamada():
    return render_template('chamada.html')

@app.route("/chamadapesquisar", methods = ['POST'])
def chamadapesquisar():
    variavelTurma = str(request.form["turma"])
    variavelAula = str(request.form["aula"])
    
    banco = Banco()
    if (banco.buscarTurma(variavelTurma) != []):
            if(banco.buscarApoiadorPorUsuarioECodigo(session['user'], variavelTurma) != []):
                if(banco.buscarAulaPorTurmaENome(variavelTurma, variavelAula) != []):
                     session['aula'] = variavelAula
                     session['nome_da_turma'] = variavelTurma
                     return render_template('atualizarpresencaaluno.html', erro_cad = False)
                else:
                    return 'Aula não existe'
            else:
                return 'Você não é apoiador dessa turma'
    else:
        return 'Turma não existe'


@app.route('/testerelatoriocontato', methods = ['GET'])
def get_relatorio(): 
    session = get_session()
    data = session.query(User).all()
    dic = {}
    for i in data:
        dic = i.format(dic)
    session.close()
    return jsonify(dic)

app.secret_key = os.urandom(12)
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, threaded=True, debug=True)
