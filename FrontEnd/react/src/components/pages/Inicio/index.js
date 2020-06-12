//página de login 
import React, { useState } from 'react'
import { Link } from 'react-router-dom'

import api from "../../../services/api"

import './inicio.css'

function Inicio() {
    const [usuario, setUsuario] = useState("")
    const [senha, setSenha] = useState("")

	async function handleCreate(e) {
		e.preventDefault()

		const data = {
            senha,
            usuario
		}

		console.log(data)

		try {
		    api.post("/logar", data).then((response) => {
                localStorage.setItem("token", response.data.access_token)
                console.log(localStorage.getItem("token"))
			})


		} catch (err) {
		    console.log(err);
		    alert("Erro no cadastro, tente novamente");
		 }
	}

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
                        <form onSubmit={handleCreate}>
                            <h1>Olá!</h1>
                            <p>Realize login para ter acesso a funcionalidades exclusivas.</p>
                            <input type="text" name="usuario" class="form-input" placeholder="Usuário" value={usuario} onChange={e => setUsuario(e.target.value)} required/>
                            <input type="password" name="senha" class="form-input" placeholder="Senha" value={senha} onChange={e => setSenha(e.target.value)} required/>
                            <input type="submit" class="button" value="Login" />
.                           <Link to="cadusuario" class="signup">Não possui conta? <span class="form-highlight">Se cadastre</span></Link>
                        </form>
                    </div>
                </div>
            </main>
        </div>
    )
}

export default Inicio