//página de login
import React, { useState } from "react"
import { Link } from "react-router-dom"
import api from "../../../services/api"
import { useHistory } from "react-router-dom"

import TextField from "@material-ui/core/TextField"
import Autocomplete from "@material-ui/lab/Autocomplete"

import NavBar from "../../navbar"

// dados pré estabelecidos CAP
import { capData } from "./data/capData"
// dados pré estabelecidos Profissão
import { profissaoCargo, profissaoChefia } from "./data/profissaoData"
// dados pré estabelecidos usuário (tipo)
import { userType } from "./data/userData"

import "./cadUsuario.css"

function Inicio() {
	const [usuario, setUsuario] = useState("")
	const [email, setEmail] = useState("")
	const [senha, setSenha] = useState("")
	const [cpf, setCpf] = useState("")
	const [telefone, setTelefone] = useState("")
	const [tipo, setTipo] = useState("")
	const [confirm_password, setConfPass] = useState("")
	const [cap, setCap] = useState("")
	const [profissao, setProfissao] = useState("")
	const [funcao, setFuncao] = useState("")

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
				history.push("/login")
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
		<>
			<NavBar login />
			<div className="login-index">
				<main className="main-content-forms">
					<div className="form-page-container cad-user">
						<div className="form-container">
							<form onSubmit={handleCreate}>
								<h1 style={title}>Bem vindo(a)!</h1>
								<p>
									Efetue cadastro para utilização de nossas funcionalidades.
								</p>
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
									type="text"
									name="email"
									className="form-input"
									placeholder="Email"
									value={email}
									onChange={(e) => {
										setEmail(e.target.value)
										console.log(email)
									}}
									required
								></input>
								<input
									type="password"
									name="senha"
									className="form-input"
									placeholder="Senha"
									value={senha}
									onChange={(e) => setSenha(e.target.value)}
									required
								/>
								<input
									type="password"
									name="confirme_senha"
									id="confirm_password"
									className="form-input"
									placeholder="Confirme a Senha"
									value={confirm_password}
									onChange={(e) => setConfPass(e.target.value)}
									required
								/>
								<input
									type="text"
									maxLength="11"
									name="cpf"
									className="form-input"
									placeholder="CPF"
									value={cpf}
									onChange={(e) => setCpf(e.target.value)}
									required
								/>
								<input
									type="tel"
									name="tel"
									className="form-input"
									placeholder="Telefone"
									value={telefone}
									onChange={(e) => setTelefone(e.target.value)}
									required
								/>

								<Autocomplete
									inputValue={cap}
									onInputChange={(_, val) => {
										setCap(val)
									}}
									options={capData}
									getOptionLabel={(option) => option.nome}
									getOptionSelected={(option, value) =>
										option.nome === value.nome
									}
									renderInput={(params) => (
										<TextField
											{...params}
											label=""
											required
											placeholder="Selecione sua CAP"
											margin="normal"
											fullWidth
											variant="outlined"
										/>
									)}
								/>

								<Autocomplete
									inputValue={profissao}
									onInputChange={(_, val) => {
										setProfissao(val)
									}}
									options={profissaoCargo}
									getOptionLabel={(option) => option.label}
									getOptionSelected={(option, value) =>
										option.value === value.value
									}
									renderInput={(params) => (
										<TextField
											{...params}
											label=""
											required
											placeholder="Selecione sua profissão"
											margin="normal"
											fullWidth
											variant="outlined"
										/>
									)}
								/>

								<Autocomplete
									inputValue={funcao}
									onInputChange={(_, val) => {
										setFuncao(val)
									}}
									options={profissaoChefia}
									getOptionLabel={(option) => option.label}
									getOptionSelected={(option, value) =>
										option.value === value.value
									}
									renderInput={(params) => (
										<TextField
											{...params}
											label=""
											required
											placeholder="Selecione sua função"
											margin="normal"
											fullWidth
											variant="outlined"
										/>
									)}
								/>

								<Autocomplete
									inputValue={tipo}
									onInputChange={(_, val) => {
										setTipo(val)
									}}
									options={userType}
									getOptionLabel={(option) => option.label}
									getOptionSelected={(option, value) =>
										option.value === value.value
									}
									renderInput={(params) => (
										<TextField
											{...params}
											label=""
											required
											placeholder="Selecione seu tipo de usuário"
											margin="normal"
											fullWidth
											variant="outlined"
										/>
									)}
								/>

								<input type="submit" className="button" value="cadastrar" />
								<Link to="/login">
									Já possui uma conta?{" "}
									<span className="form-highlight">Faça login</span>
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
