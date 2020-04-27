from flask import session

class Pessoa:
    def __init__(self):
        self.iniciar(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    def iniciar(self, id, nome, senha, email, adm, gestor, coordenador, propositor, cursista, apoiador):
        self._id = id
        self._nome = nome
        self._email = email
        self._senha=senha
        self._adm=adm
        self._gestor=gestor
        self._coordenador=coordenador
        self._propositor=propositor
        self._cursista=cursista
        self._apoiador=apoiador
        self.valido = self.validar()
    
    def validar(self):
        session['logged_in'] = True
        session['user'] = self._nome
        session['user_id'] = int(self._id)
        session['adm'] = int(self._adm)
        session['gestor'] = int(self._gestor)
        session['coordenador'] = int(self._coordenador)
        session['propositor'] = int(self._propositor)
        session['cursista'] = int(self._cursista)
        session['apoiador'] = int(self._apoiador)
        #Para (futuramente) verificar se a pessoa é valida
        valido = True
        return valido

    def get_nome(self):
        return self._nome

    def alterar_senha(self):
        return "Ainda nao e possivel alterar a senha"
