//página de login
import React, { useState, useEffect } from "react"
import { Link } from "react-router-dom"
import api from "../../../services/api"
import { useHistory } from "react-router-dom"

import TextField from "@material-ui/core/TextField"
import Autocomplete from "@material-ui/lab/Autocomplete"
import { makeStyles, withStyles } from "@material-ui/core/styles"
import InputLabel from "@material-ui/core/InputLabel"
import FormControl from "@material-ui/core/FormControl"
import NativeSelect from "@material-ui/core/NativeSelect"
import InputBase from "@material-ui/core/InputBase"

import NavBar from "../../navbar"

// dados pré estabelecidos CAP
import { capData, caps } from "./data/capData"
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
	const [CAP, setCAP] = useState("")
	const [UnidadeBasicadeSaude, setUnidadeBasicadeSaude] = useState("")
	const [listaUnidades, setListaUnidades] = useState([])
	const [profissao, setProfissao] = useState("")
	const [funcao, setFuncao] = useState("")

	const [erroNome, setErroNome] = useState("")
	const [erroEmail, setErroEmail] = useState("")
	const [erroSenha, setErroSenha] = useState("")
	const [erroCpf, setErroCpf] = useState("")
	const [erroTelefone, setErroTelefone] = useState("")

	const history = useHistory()

	// quando cap mudar mudam as unidades
	useEffect(() => {
		const unidadesFiltradas = capData.filter((unidade) => unidade.cap == CAP)
		// apenas unidades de certa CAP
		setListaUnidades(unidadesFiltradas)
		// para não enviar "" caso usuário não mude o select da primeira opção
		const unidadeInicial = unidadesFiltradas[0] ? unidadesFiltradas[0].label : ''
		setUnidadeBasicadeSaude(unidadeInicial)
	}, [CAP])

	async function handleCreate(e) {
		e.preventDefault()

		const data = {
			usuario,
			email,
			senha,
			cpf,
			telefone,
			tipo,
			CAP,
			UnidadeBasicadeSaude,
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

	const BootstrapInput = withStyles((theme) => ({
		root: {
			"label + &": {
				marginTop: theme.spacing(3),
				marginBottom: "10px",
			},
		},
		input: {
			borderRadius: 4,
			position: "relative",
			backgroundColor: "hsl(0, 0%, 95%)",
			width: "100%",
			border: "1px solid #ced4da",
			fontSize: 16,
			padding: "10px 26px 10px 12px",
			transition: theme.transitions.create(["border-color", "box-shadow"]),
			// Use the system font instead of the default Roboto font.
			fontFamily: [
				"-apple-system",
				"BlinkMacSystemFont",
				'"Segoe UI"',
				"Roboto",
				'"Helvetica Neue"',
				"Arial",
				"sans-serif",
				'"Apple Color Emoji"',
				'"Segoe UI Emoji"',
				'"Segoe UI Symbol"',
			].join(","),
			"&:focus": {
				borderRadius: 4,
				borderColor: "#80bdff",
				boxShadow: "0 0 0 0.2rem rgba(0,123,255,.25)",
			},
		},
	}))(InputBase)

	const useStyles = makeStyles((theme) => ({
		margin: {
			margin: theme.spacing(1),
		},
	}))

	return (
		<>
			<NavBar login />
			<main className="main">
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
									required
									onChange={(e) => {
										setUsuario(e.target.value)
										const regex = new RegExp("^[a-zA-Z0-9]+$")
										let regexTestNome = !regex.test(e.target.value)
										setErroNome(regexTestNome)
									}}
								/>

								{erroNome && (
									<p className="error">
										Digite um valor alfanumérico sem espaços
									</p>
								)}

								<input
									type="text"
									name="email"
									className="form-input"
									placeholder="Email"
									value={email}
									required
									onChange={(e) => {
										setEmail(e.target.value)
										const regex = /^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i
										let regexTestEmail = !regex.test(e.target.value)
										setErroEmail(regexTestEmail)
									}}
								></input>

								{erroEmail && <p className="error">Digite um e-mail válido</p>}

								<input
									type="password"
									name="senha"
									className="form-input"
									placeholder="Senha"
									value={senha}
									required
									onChange={(e) => {
										setSenha(e.target.value)
										const regex = new RegExp("^.{4,15}$")
										let regexTestSenha = !regex.test(e.target.value)
										setErroSenha(regexTestSenha)
									}}
								/>

								{erroSenha && (
									<p className="error">Senha deve ter de 4 a 15 caracteres</p>
								)}

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
									required
									onChange={(e) => {
										setCpf(e.target.value)
										const regex = new RegExp("^([0-9]{11})$")
										let regexTestCpf = !regex.test(e.target.value)
										setErroCpf(regexTestCpf)
									}}
								/>

								{erroCpf && (
									<p className="error">
										Digite um valor numérico de 11 dígitos para o CPF
									</p>
								)}

								<input
									type="tel"
									name="tel"
									maxLength="9"
									className="form-input"
									placeholder="Telefone"
									value={telefone}
									required
									onChange={(e) => {
										setTelefone(e.target.value)
										const regex = new RegExp("^([0-9]{8,9})$")
										let regexTestTelefone = !regex.test(e.target.value)
										setErroTelefone(regexTestTelefone)
									}}
								/>

								{erroTelefone && (
									<p className="error">
										Digite um valor numérico de 8 a 9 dígitos para o telefone
									</p>
								)}

								<FormControl>
									<InputLabel htmlFor="demo-customized-select-native">
										CAP
									</InputLabel>
									<NativeSelect
										id="demo-customized-select-native"
										value={CAP}
										onChange={(e) => setCAP(e.target.value)}
										input={<BootstrapInput />}
										required
									>
										{caps.map((option) => {
											return (
												<option value={option.value}>{option.label}</option>
											)
										})}
									</NativeSelect>
								</FormControl>

								<FormControl>
									<InputLabel htmlFor="demo-customized-select-native">
										Unidade
									</InputLabel>
									<NativeSelect
										id="demo-customized-select-native"
										value={UnidadeBasicadeSaude}
										onChange={(e) => setUnidadeBasicadeSaude(e.target.value)}
										input={<BootstrapInput />}
										required
									>
										{listaUnidades.map((option) => {
											return (
												<option value={option.label}>{option.label}</option>
											)
										})}
									</NativeSelect>
								</FormControl>

								<FormControl>
									<InputLabel htmlFor="demo-customized-select-native">
										Profissão
									</InputLabel>
									<NativeSelect
										id="demo-customized-select-native"
										value={profissao}
										onChange={(e) => setProfissao(e.target.value)}
										input={<BootstrapInput />}
										required
									>
										{profissaoCargo.map((option) => {
											return (
												<option value={option.value}>{option.label}</option>
											)
										})}
									</NativeSelect>
								</FormControl>

								<FormControl>
									<InputLabel htmlFor="demo-customized-select-native">
										Função
									</InputLabel>
									<NativeSelect
										id="demo-customized-select-native"
										value={funcao}
										onChange={(e) => setFuncao(e.target.value)}
										input={<BootstrapInput />}
									>
										{profissaoChefia.map((option) => {
											return (
												<option value={option.value}>{option.label}</option>
											)
										})}
									</NativeSelect>
								</FormControl>

								<FormControl>
									<InputLabel htmlFor="demo-customized-select-native">
										Tipo de usuário
									</InputLabel>
									<NativeSelect
										id="demo-customized-select-native"
										value={tipo}
										onChange={(e) => setTipo(e.target.value)}
										input={<BootstrapInput />}
										required
									>
										{userType.map((option) => {
											return (
												<option value={option.value}>{option.label}</option>
											)
										})}
									</NativeSelect>
								</FormControl>

								<input type="submit" className="button" value="cadastrar" />
								<Link to="/login">
									Já possui uma conta?{" "}
									<span className="form-highlight cad-user">Faça login</span>
								</Link>
							</form>
						</div>
					</div>
				</main>
			</main>
		</>
	)
}

export default Inicio
