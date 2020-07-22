//página de login
import React, { useState } from "react"
import { Link } from "react-router-dom"
import api from "../../../services/api"
import { useHistory } from "react-router-dom"

//dados pré estabelecidos CAP
import { capData, renderCapTitle } from "./capData"
//autocomplete pra exibir dados cap
import Autocomplete from "react-autocomplete"

import './cadUsuario.css'

function Inicio() {
	const [usuario, setUsuario] = useState("")
	const [email, setEmail] = useState("")
	const [senha, setSenha] = useState("")
	const [cpf, setCpf] = useState("")
	const [telefone, setTelefone] = useState("")
	const tipo = "adm"
	const [confirm_password, setConfPass] = useState("")
	const [cap, setCap] = useState("")
	const [funcao, setFuncao] = useState("")
	const [profissao, setProfissao] = useState("")

	const history = useHistory()

	async function handleCreate(e) {
		e.preventDefault()

		const data = {
			usuario,
			email,
			senha,
			cpf,
			telefone,
			tipo,
			cap,
			funcao,
			profissao,
		}

		if (senha == confirm_password) {
			try {
				api.post("/cadastrar", data)

				alert(`O usuário foi cadastrado com sucesso!`)
				history.push('/login')
			} catch (err) {
				console.log(err)
				alert("Erro no cadastro, tente novamente")
			}
		} else {
			alert("As senhas não coincidem.")
		}
	}

	const title = {
		marginTop: "300px",
	}

	return (
		<div className="login-index">
			<div className="index-header">
				<Link to="/login">Educação Permanente</Link>
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
								value={usuario}
								onChange={(e) => setUsuario(e.target.value)}
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
								value={senha}
								onChange={(e) => setSenha(e.target.value)}
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
								value={telefone}
								onChange={(e) => setTelefone(e.target.value)}
								required
							/>
							{/* <input
								type="text"
								name="cap"
								class="form-input"
								placeholder="CAP"
								value={cap}
								onChange={(e) => setCap(e.target.value)}
								required
							/> */}
							<div className="autocomplete-wrapper">
								<Autocomplete
									inputProps={{ placeholder: 'Selecione o Cap', required: true, type: 'select' }}
									value={cap}
									items={capData()}
									getItemValue={(item) => item.nome}
									shouldItemRender={renderCapTitle}
									renderMenu={(item) => <div className="dropdown">{item}</div>}
									renderItem={(item, isHighlighted) => (
										<div
											className={`item ${isHighlighted ? "selected-item" : ""}`}
										>
											{item.nome}
										</div>
									)}
									onChange={(e) => setCap(e.target.value)}
									onSelect={(val) => setCap(val)}
								/>
							</div>

							<input
								type="text"
								name="funcao"
								class="form-input"
								placeholder="Função"
								value={funcao}
								onChange={(e) => setFuncao(e.target.value)}
								required
							/>
							<input
								type="text"
								name="profissao"
								class="form-input"
								placeholder="Profissão"
								value={profissao}
								onChange={(e) => setProfissao(e.target.value)}
								required
							/>
							<input type="submit" class="button" value="cadastrar" />
							<Link to="/login">
								Já possui uma conta?{" "}
								<span class="form-highlight">Faça login</span>
							</Link>
						</form>
					</div>
				</div>
			</main>
		</div>
	)
}

export default Inicio
