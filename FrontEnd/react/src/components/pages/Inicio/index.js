//página de login 
import React from 'react'
import { Link } from 'react-router-dom'

import './inicio.css'

function Inicio() {

    //adaptar login para js
    //fazer mudanças para usar useState
    //mudar links esqueci a senha e cadastro
    // <a href="esqueciasenha" class="forgot">Esqueceu a senha?</a>
    return (
        <div className="login-index">
            <div className="index-header">
                <Link to="/">Educação Permanente</Link>
            </div>

            <main className="main-content-forms">
                <div className="form-page-container">
                    <div className="form-container">
                        <form>
                            <h1>Olá!</h1>
                            <p>Realize login para ter acesso a funcionalidades exclusivas.</p>
                            <input type="text" name="usuario" class="form-input" placeholder="Usuário"/>
                            <input type="password" name="senha" class="form-input" placeholder="Senha"></input>
.                            <Link to="cadusuario" class="signup">Não possui conta? <span class="form-highlight">Se cadastre</span></Link>
                        </form>
                        <Link to="/turmas">
                            <button class="button" value="Login">Login</button>
                        </Link>
                    </div>
                </div>
            </main>
        </div>
    )
}

export default Inicio