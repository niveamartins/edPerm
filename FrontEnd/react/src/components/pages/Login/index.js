//página de login
import React, { useState } from "react"
import { Link, useHistory } from "react-router-dom"

import api from "../../../services/api"

import "./login.css"
import NavBar from '../../navbar'

import jwt from "jwt-decode"

function Inicio() {
	const [usuario, setUsuario] = useState("")
	const [senha, setSenha] = useState("")
	const history = useHistory()

	localStorage.removeItem("token")
	localStorage.removeItem("user_id")
	localStorage.removeItem("user_username")
	localStorage.removeItem('user.type')

	async function handleCreate(e) {
		e.preventDefault()

		const data = {
			senha,
			usuario,
		}

		try {
			await api.post("/logar", data).then((response) => {
				localStorage.setItem("token", response.data.access_token)
			})

			let user = jwt(localStorage.getItem("token"))
			console.log( user.identity)
			let user_id = user.identity.id
			localStorage.setItem("user_id", user_id)

			let user_username = user.identity.usuario
			localStorage.setItem("user_username", user_username)

			let user_type = user.identity.tipo
			localStorage.setItem('user_type',user_type)

			history.push("/")
		} catch (err) {
			console.log(err)
			alert("Erro no cadastro, tente novamente")
		}
	}

	//adaptar login para js
	//fazer mudanças para usar useState
	//mudar links esqueci a senha e cadastro
	// <a href="esqueciasenha" class="forgot">Esqueceu a senha?</a>
	return (
		<>
		<NavBar login />
		<div className="login-index">
			<main className="main-content-forms">
				<div className="form-page-container login">
					<div className="form-container">
						<form onSubmit={handleCreate}>
							<h1>Olá!</h1>
							<p>Realize login para ter acesso a funcionalidades exclusivas.</p>
							<input
								type="text"
								name="usuario"
								className="form-input"
								placeholder="Usuário"
								value={usuario}
								onChange={(e) => setUsuario(e.target.value)}
								required
							/>
							<input
								type="password"
								name="senha"
								className="form-input"
								placeholder="Senha"
								value={senha}
								onChange={(e) => setSenha(e.target.value)}
								required
							/>
							<input type="submit" className="button" value="Login" />.{" "}
							<Link to="cadusuario" className="signup">
								Não possui conta?{" "}
								<span className="form-highlight">Se cadastre</span>
							</Link>
						</form>
					</div>
				</div>
			</main>
		</div>
		</>
	)
}

export default Inicio
