from flask import Flask, request, render_template, redirect, url_for, session
import os, smtplib
from db_create import Banco
from pessoas import Pessoa
from geradordeqrcode import Gerador

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
            return redirect('/')
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


@app.route("/cadastroturma")
def cadastroturma():
    return render_template('CadastroTurma.html')

@app.route("/cadastrarturma", methods = ['POST'])
def cadastrarturma():
    variavelProfessor = str(request.form["professor"])
    variavelCodigo = str(request.form["codigo"])
    variavelCurso =  str(request.form["curso"])
    
    banco = Banco()
    if (banco.buscarProfessor(variavelProfessor) != []):
        variavelProfessor = banco.buscarProfessor(variavelProfessor)
        cadastrado = banco.cadastrarTurma(variavelProfessor[0], variavelCodigo, variavelCurso)
    else:
        return 'Usuario não existe'
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
            if(banco.buscarAluno(variavelAluno)):
                 variavelAluno = banco.buscarAluno(variavelAluno)
                 cadastrado = banco.cadastrarAlunos(variavelTurma[0], variavelAluno[0])
            else:
                return 'Aluno não existe'
    else:
        return 'Turma não existe'
    if cadastrado:
        print("3")
        return render_template('cadastroalunonaturma.html', erro_cad = False)
    else:
        print("4")
        return render_template('cadastroalunonaturma.html', erro_cad = True)

@app.route("/listaturma")
def listarturma():
    banco = Banco()
    return render_template('listaturma.html', eventos = banco.listarTurma())

@app.route('/listaturma/<string:codigo_turma>')
def turma(codigo_turma):
    banco = Banco()
    eventos = banco.buscarTurma(codigo_turma)
    variavel = eventos[0][0]
    alunodaturma = banco.listarAlunos(variavel)
    evento = banco.buscarTurma(codigo_turma)
    print(eventos)
    print(alunodaturma)
    print(variavel)
    return render_template('listaralunosdaturma.html', eventos = evento, alunosdaturma = alunodaturma )


@app.route("/listadepresenca")
def listadepresenca():
    return render_template('atualizarpresencaaluno.html')

@app.route("/atualizarpresenca", methods = ['POST'])
def atualizarpresenca():
    variavelAluno = str(request.form["alunopre"])
    variavelTurma = str(request.form["codigopre"])
    
    banco = Banco()
    if (banco.buscarTurma(variavelTurma) != []):
            if(banco.buscarAlunoPorUsuarioECodigo(variavelAluno, variavelTurma) != []):
                 variavelAluno = banco.buscarAlunoPorUsuarioECodigo(variavelAluno, variavelTurma)
                 variavelTurma = banco.buscarTurma(variavelTurma)
                 presenca = int(variavelAluno[0][3]) + 1
                 cadastrado = banco.atualizarAlunos(variavelAluno[0][0], presenca)
            else:
                return 'Aluno não existe'
    else:
        return 'Turma não existe'
    if cadastrado:
        print("3")
        return render_template('atualizarpresencaaluno.html', erro_cad = False)
    else:
        print("4")
        return render_template('atualizarpresencaaluno.html', erro_cad = True)


app.secret_key = os.urandom(12)
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, threaded=True, debug=True)
