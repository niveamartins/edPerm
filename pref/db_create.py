# -*- coding: utf-8 -*-
import sqlite3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from send import Send
import smtplib 

class Banco():

    def ajeitarTabelas(self,):
        with sqlite3.connect('db1.db') as connection:
            cursor = connection.cursor()
            cursor.execute("DROP TABLE IF EXISTS grade")
    def criarTabelas(self):

        connection = sqlite3.connect('db1.db')


        # if connection.is_connected():
        #     db_Info = connection.get_server_info()
        #     print("Connected to MySQL Server version ", db_Info)
        #     cursor = connection.cursor()
        #     cursor.execute("select database();")
        #     record = cursor.fetchone()
        #     print("You're connected to database: ", record)
        cursor = connection.cursor()


        cursor.execute (

        """
            CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY,
            usuario TEXT NOT NULL,
            email TEXT NOT NULL,
            senha TEXT NOT NULL,
            adm INTEGER DEFAULT 0 NOT NULL,
            gestor INTEGER DEFAULT 0 NOT NULL,
            coordenador INTEGER DEFAULT 0 NOT NULL,
            propositor INTEGER DEFAULT 0 NOT NULL,
            cursista INTEGER DEFAULT 0 NOT NULL,
            apoiador INTEGER DEFAULT 0 NOT NULL
            );

        """
        )

        cursor.execute (

        """
            CREATE TABLE IF NOT EXISTS turma(
            id_turma INTEGER PRIMARY KEY AUTOINCREMENT,
            id_responsavel INTEGER NOT NULL,
            nome_do_curso VARCHAR(50) NOT NULL,
            dia VARCHAR(50) NOT NULL,
            hora VARCHAR(50) NOT NULL,
            carga_horaria_total VARCHAR(50) NOT NULL,
            tolerancia VARCHAR(50) NOT NULL,
            modalidade VARCHAR(50) NOT NULL,
            turma_tag VARCHAR(50) NOT NULL,
            FOREIGN KEY (id_responsavel) REFERENCES user(id)
            );

        """
        )

        cursor.execute (

        """
            CREATE TABLE IF NOT EXISTS horario(
            id_horario INTEGER PRIMARY KEY AUTOINCREMENT,
            horario_id_turma INTEGER NOT NULL,
            dia_da_semana VARCHAR(20) NOT NULL,
            horario_inicio TIME NOT NULL,
            horario_termino TIME NOT NULL,
            FOREIGN KEY (horario_id_turma) REFERENCES turma(id_turma)
            );

        """
        )

        cursor.execute (

        """
            CREATE TABLE IF NOT EXISTS alunos(
            id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
            alunos_id_turma INTEGER NOT NULL,
            alunos_id_user INTEGER NOT NULL,
            presenca INTEGER DEFAULT '0' NOT NULL,
            FOREIGN KEY (alunos_id_turma) REFERENCES turma(id_turma),
            FOREIGN KEY (alunos_id_user) REFERENCES user(id)
            );

        """
        )

        connection.commit()
        cursor.close()
        connection.close()



    def cadastrar_pessoa(self,user, senha, email):
        try:
            with sqlite3.connect('db1.db') as connection:
                cursor = connection.cursor()
                cursor.execute('INSERT INTO user(usuario, email, senha) VALUES(?, ?, ?)', (user, email, senha))
                connection.commit()
                return True
        except:
            return False

    def cadastrar_complemento(self,userId, tag, profissao, funcao, superentendencia, cap, unidade):
        try:
            with sqlite3.connect('db1.db') as connection:
                cursor = connection.cursor()
                cursor.execute('INSERT INTO userComplemento(id_do_user, tag, profissao, funcao, superentendenciaDaSUBPAV, CAP, unidadeBasicaDeSaude) VALUES(?, ?, ?, ?, ?, ?, ?)', (userId, tag, profissao, funcao, superentendencia, cap, unidade))
                connection.commit()
                return True
        except:
            return False

    def atualizarTag(self, iddosuser, tag):
        try:
            with sqlite3.connect('db1.db') as connection:
                cursor = connection.cursor()
                cursor.execute('UPDATE userComplemento SET tag = ? WHERE id_do_user = ?', (tag, iddosuser))
                connection.commit()
                return True
        except:
            return False
   
    def atualizarProfissao(self, iddosuser, profissao):
        try:
            with sqlite3.connect('db1.db') as connection:
                cursor = connection.cursor()
                cursor.execute('UPDATE userComplemento SET profissao = ? WHERE id_do_user = ?', (profissao, iddosuser))
                connection.commit()
                return True
        except:
            return False

    def atualizarFuncao(self, iddosuser, funcao):
        try:
            with sqlite3.connect('db1.db') as connection:
                cursor = connection.cursor()
                cursor.execute('UPDATE userComplemento SET funcao = ? WHERE id_do_user = ?', (funcao, iddosuser))
                connection.commit()
                return True
        except:
            return False

    def atualizarSuperentendencia(self, iddosuser, superentendencia):
        try:
            with sqlite3.connect('db1.db') as connection:
                cursor = connection.cursor()
                cursor.execute('UPDATE userComplemento SET superentendenciaDaSUBPAV = ? WHERE id_do_user = ?', (superentendencia, iddosuser))
                connection.commit()
                return True
        except:
            return False

    def atualizarCap(self, iddosuser, cap):
        try:
            with sqlite3.connect('db1.db') as connection:
                cursor = connection.cursor()
                cursor.execute('UPDATE userComplemento SET CAP = ? WHERE id_do_user = ?', (cap, iddosuser))
                connection.commit()
                return True
        except:
            return False

    def atualizarUnidade(self, iddosuser, unidade):
        try:
            with sqlite3.connect('db1.db') as connection:
                cursor = connection.cursor()
                cursor.execute('UPDATE userComplemento SET unidadeBasicaDeSaude = ? WHERE id_do_user = ?', (unidade, iddosuser))
                connection.commit()
                return True
        except:
            return False


    def buscar_pessoa(self, usr, senha):
        with sqlite3.connect('db1.db') as connection:
            cursor = connection.cursor()
            find_user = ("SELECT * FROM user WHERE usuario = ? AND senha = ?")
            results = cursor.execute(find_user, (usr, senha)).fetchall()
        return results

    def ajuste(self, string):
        string = string.strip('[')
        string = string.strip(']')
        string = string.strip('(')
        string = string.strip(')')
        string = " ".join(string.split('"'))
        string = " ".join(string.split('"'))
        string = " ".join(string.split("'"))
        string = " ".join(string.split("'"))
        
        return string



    def recuperarSenha(self,user):
        send = Send()
        user = user.title()
        try: 
            with sqlite3.connect('db1.db') as connection:
                cursor = connection.cursor()
                find_user = "SELECT senha, email FROM user WHERE email = ?"
                
                results = cursor.execute(find_user, (user,)).fetchall()[0]
                
            send.sendMessage(results[0], results[1])
            return "enviado"
        except:
            return 'usuário não existe'

    def cadastrarTurma(self, responsavel, nome, dia, hora, carga, tolerancia, modalidade, tag):
        try:
            with sqlite3.connect('db1.db') as connection:
                cursor = connection.cursor()
                cursor.execute('INSERT INTO turma(id_responsavel, nome_do_curso, dia, hora, carga_horaria_total, tolerancia, modalidade, turma_tag) VALUES(?, ?, ?, ?, ?, ?, ?, ?)', (responsavel[0], nome, dia, hora, carga, tolerancia, modalidade, tag))
                connection.commit()
                return True
        except:
            return False


    def cadastrarHorario(self,variavel_horario_id_turma, variavel_dia_da_semana, variavel_horario_inicio, variavel_horario_termino):
        try:
            with sqlite3.connect('db1.db') as connection:
                cursor = connection.cursor()
                cursor.execute('INSERT INTO horario(horario_id_turma, dia_da_semana, horario_inicio, horario_termino) VALUES(?, ?, ?, ?)', (variavel_horario_id_turma, variavel_dia_da_semana, variavel_horario_inicio, variavel_horario_termino))
                connection.commit()
                return True
        except:
            return False



    def cadastrarAlunos(self,variavel_alunos_id_turma, variavel_alunos_id_user):
        try:
            with sqlite3.connect('db1.db') as connection:
                cursor = connection.cursor()
                cursor.execute('INSERT INTO alunos(alunos_id_turma, alunos_id_user) VALUES(?, ?)', (variavel_alunos_id_turma[0], variavel_alunos_id_user[0]))
                connection.commit()
                return True
        except:
            return False

    def atualizarAlunos(self, variavel_alunos_id, valordapresenca):
        try:
            with sqlite3.connect('db1.db') as connection:
                cursor = connection.cursor()
                cursor.execute('UPDATE alunos SET presenca = ? WHERE id_aluno = ?', (valordapresenca, variavel_alunos_id))
                connection.commit()
                return True
        except:
            return False


    def listarTurma(self):

        with sqlite3.connect('db1.db') as connection:

            cursor = connection.cursor()

            lista = ("SELECT * FROM turma INNER JOIN user ON turma.id_responsavel = user.id")
            result = cursor.execute(lista).fetchall()
            
        return result
      

    def listarHorario(self, variavel_horario_id_turma):

        with sqlite3.connect('db1.db') as connection:

            cursor = connection.cursor()

            lista = ("SELECT * FROM horario WHERE horario_id_turma = ?")
            result = cursor.execute(lista).fetchall()
            
        return result
      

    def listarAlunos(self, variavel_alunos_id_turma):

        with sqlite3.connect('db1.db') as connection:

            cursor = connection.cursor()

            lista = ("SELECT * FROM alunos INNER JOIN user ON alunos.alunos_id_user = user.id WHERE alunos_id_turma = ? AND alunos_id_turma = ?")
            result = cursor.execute(lista, (variavel_alunos_id_turma, variavel_alunos_id_turma)).fetchall()
            
        return result

    def buscarProfessor(self, usuario):
        resultado = []
        with sqlite3.connect('db1.db') as connection:
            
            cursor = connection.cursor()
            find_user = ("SELECT * FROM user WHERE usuario = ? AND usuario = ?")
            resultado = cursor.execute(find_user, (usuario, usuario)).fetchall()
        return resultado

    def buscarDadosComplementares(self, usuario):
        resultado = []
        with sqlite3.connect('db1.db') as connection:
            
            cursor = connection.cursor()
            find_user = ("SELECT * FROM userComplemento WHERE id_do_user = ? AND id_do_user = ?")
            resultado = cursor.execute(find_user, (usuario, usuario)).fetchall()
        return resultado

    def buscarAluno(self, usuario):
        resultado = []
        with sqlite3.connect('db1.db') as connection:
            
            cursor = connection.cursor()
            find_user = ("SELECT * FROM user WHERE usuario = ? AND usuario = ?")
            resultado = cursor.execute(find_user, (usuario, usuario)).fetchall()
        return resultado

    def buscarTurma(self, codigo):
        resultado = []
        with sqlite3.connect('db1.db') as connection:
            
            cursor = connection.cursor()
            find_user = ("SELECT * FROM turma WHERE nome_do_curso = ? AND nome_do_curso = ?")
            resultado = cursor.execute(find_user, (codigo, codigo)).fetchall()
        return resultado

    def buscarTurmaComProfessor(self, codigo):
        resultado = []
        with sqlite3.connect('db1.db') as connection:
            
            cursor = connection.cursor()
            find_user = ("SELECT * FROM turma INNER JOIN user ON turma.id_responsavel = user.id WHERE nome_do_curso = ? AND nome_do_curso = ?")
            resultado = cursor.execute(find_user, (codigo, codigo)).fetchall()
        return resultado

    def buscarAlunoPorUsuarioECodigo(self, usuario, codigo):
        resultado = []
        with sqlite3.connect('db1.db') as connection:

            cursor = connection.cursor()
            find_user = ("SELECT * FROM alunos INNER JOIN user ON alunos.alunos_id_user = user.id INNER JOIN turma ON alunos.alunos_id_turma = turma.id_turma WHERE usuario = ? AND nome_do_curso = ?")
            resultado = cursor.execute(find_user, (usuario, codigo)).fetchall()
            print("Cheguei aqui")
        return resultado

banco = Banco()
x = "Crystian"
send= Send()
'''
send.sendMessage("123", "Crystian.S.F@Gmail.Com")
'''
#print(banco.recuperarSenha(x))
'''
banco.ajeitarTabelas()
banco.criarTabelas()
'''


