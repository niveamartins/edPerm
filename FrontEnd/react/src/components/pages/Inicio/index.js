//página de login 
import React, { useState } from 'react'
import { Link, useHistory } from 'react-router-dom'

import api from "../../../services/api"

import './inicio.css'

import jwt from 'jwt-decode'



function Inicio() {
    const [usuario, setUsuario] = useState("")
    const [senha, setSenha] = useState("")
    const history = useHistory();

    localStorage.removeItem("token");

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
                const token = response.data.access_token; 
                let user = jwt(token)
                user = user.identity

                localStorage.setItem("user", user)

                history.push("/turmas");
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
                            <input type="text" name="usuario" className="form-input" placeholder="Usuário" value={usuario} onChange={e => setUsuario(e.target.value)} required/>
                            <input type="password" name="senha" className="form-input" placeholder="Senha" value={senha} onChange={e => setSenha(e.target.value)} required/>
                            <input type="submit" className="button" value="Login" />
.                           <Link to="cadusuario" className="signup">Não possui conta? <span className="form-highlight">Se cadastre</span></Link>
                        </form>
                    </div>
                </div>
            </main>
        </div>
    )
}

export default Inicio