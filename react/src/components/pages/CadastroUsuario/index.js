//página de login 
import React from 'react'

import './cadastroUsuario.css'

function Inicio() {

    //Integrar cadastro com js

    // mudar quando for integrar:
    // <input placeholder="Nome do Aluno" value={name} onChange={e => setName(e.target.value)}></input>
    // onSubmit={handleCreate}
    // <input placeholder="Código da Turma" value={turma} onChange={e => setTurma(e.target.value)}></input>

    return (
        <div className="login-index">
            <div className="index-header">
                <a href="/">Educação Permanente</a>
            </div>

            <main className="main-content-forms">
                <div className="form-page-container">
                    <div className="form-container">
                        <form>
                            <h1>Bem vindo(a)!</h1>
                            <p>Efetue cadastro para utilização de nossas funcionalidades.</p>
                            <input type="text" name="usuario" class="form-input" placeholder="Usuário" required />
                            <input type="text" name="email" class="form-input" placeholder="Email" required></input>
                            <input type="password" name="senha" class="form-input" placeholder="Senha" required />
                            <input type="password" name="confirme_senha" id="confirm_password" class="form-input"
                                placeholder="Confirme a Senha" required />
                            <input type="submit" class="button login" value="cadastrar" />
                            <a href="/">Já possui uma conta? <span class="form-highlight">Faça login</span></a>
                        </form>
                    </div>
                </div>
            </main>
        </div>
    )
}

export default Inicio