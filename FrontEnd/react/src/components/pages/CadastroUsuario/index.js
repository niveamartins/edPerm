//página de login
import React, { useState } from "react"
import api from "../../../services/api"

function Inicio() {
	const [user, setUser] = useState("")
	const [email, setEmail] = useState("")
	const [password, setPassword] = useState("")
	const [cpf, setCpf] = useState("")
	const [telephone, setTelephone] = useState("")
	const [type, setType] = useState("")
	const [confirm_password, setConfPass] = useState("")

	async function handleCreate(e) {
		e.preventDefault()

		const data = {
			user,
			email,
			password,
			cpf,
			telephone,
			type,
		}

		if (password == confirm_password) {
			try {
				api.post("/cadastrar", data)

				alert(`O usuário foi cadastrado com sucesso!`)
			} catch (err) {
				console.log(err)
				alert("Erro no cadastro, tente novamente")
			}
		} else {
			alert("As senhas não coincidem.")
		}
	}

	const title = {
		marginTop: "4.5em",
    }
    
	return (
		<div className="login-index">
			<div className="index-header">
				<a href="/">Educação Permanente</a>
			</div>

			<main className="main-content-forms">
				<div className="form-page-container">
					<div className="form-container">
						<form onSubmit={handleCreate}>
							<h1 style={title}>Bem vindo(a)!</h1>
							<p>Efetue cadastro para utilização de nossas funcionalidades.</p>
							<input
								type="text"
								name="usuario"
								class="form-input"
								placeholder="Usuário"
								value={user}
								onChange={(e) => setUser(e.target.value)}
								required
							/>
							<input
								type="text"
								name="email"
								class="form-input"
								placeholder="Email"
								value={email}
								onChange={(e) => setEmail(e.target.value)}
								required
							></input>
							<input
								type="password"
								name="senha"
								class="form-input"
								placeholder="Senha"
								value={password}
								onChange={(e) => setPassword(e.target.value)}
								required
							/>
							<input
								type="password"
								name="confirme_senha"
								id="confirm_password"
								class="form-input"
								placeholder="Confirme a Senha"
								value={confirm_password}
								onChange={(e) => setConfPass(e.target.value)}
								required
							/>
							<input
								type="text"
								maxLength="11"
								name="cpf"
								class="form-input"
								placeholder="CPF"
								value={cpf}
								onChange={(e) => setCpf(e.target.value)}
								required
							/>
							<input
								type="tel"
								name="tel"
								class="form-input"
								placeholder="Telefone"
								value={telephone}
								onChange={(e) => setTelephone(e.target.value)}
								required
							/>
							<input type="submit" class="button" value="cadastrar" />
							<a href="/">
								Já possui uma conta?{" "}
								<span class="form-highlight">Faça login</span>
							</a>
						</form>
					</div>
				</div>
			</main>
		</div>
	)
}

export default Inicio
