import React, { Fragment, useState, useEffect } from "react"
import { Redirect, useHistory } from "react-router-dom"

import './cadastrarPublico.css'

import api from "../../../services/api"
import { withStyles } from "@material-ui/core/styles"
import InputLabel from "@material-ui/core/InputLabel"
import FormControl from "@material-ui/core/FormControl"
import NativeSelect from "@material-ui/core/NativeSelect"
import InputBase from "@material-ui/core/InputBase"

import { NavBar } from "../../navbar"
import { HomeButton } from "../../HomeButton"

import { profissaoCargo } from '../CadastroUsuario/data/profissaoData'

function CadastrarPublico(props) {
   const [nome_do_curso, setNomeCurso] = useState("")
   const [publico_alvo, setPublico] = useState("")
	
   const adm = localStorage.getItem("adm")
   const gestor = localStorage.getItem("gestor")
   const coordenador = localStorage.getItem("coordenador")
   const propositor = localStorage.getItem("propositor")

	const allowedUsers = adm === "true" || gestor === "true" || coordenador === "true" || propositor === "true"
	let redirectIfNotAuth = null
	if (!allowedUsers) redirectIfNotAuth = <Redirect to="/" />

	const history = useHistory()

	async function handleCreate(e) {
		e.preventDefault()
		const data = {
         nome_do_curso,
         publico_alvo
		}
		console.log(data)
		try {
			const token = localStorage.getItem("token")
			const AuthStr = "Bearer ".concat(token)
			api
				.post("/adicionarpublico", data, {
					headers: { Authorization: AuthStr },
				})
				.then((response) => {
					if (response.data.hasOwnProperty("error") === true) {
						alert("Não foi possível cadastrar o público-alvo")
					} else {
						alert("O público-alvo foi cadastrado com sucesso!")
						history.go(0)
					}
				})
		} catch (err) {
			console.log(err)
			alert("Erro no cadastro, tente novamente")
		}
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

	return (
		<Fragment>
			{redirectIfNotAuth}
			<NavBar />
			<main className="main">
				<div className="info-turmas apoiador">
					<div className="form-page-container publico-alvo">
						<div className="form-container publico-alvo">
							<form onSubmit={handleCreate}>
								<h1>Cadastre o público alvo de sua turma!</h1>
								<p>
									Selecione, um por vez, os públicos alvos desejados para sua turma!
								</p>
								<br />
                        <input 
                           type="text"
                           placeholder="Nome do curso"
                           value={nome_do_curso}
                           onChange={(e) => setNomeCurso(e.target.value)}
                           required
                        />
								<FormControl>
									<InputLabel htmlFor="demo-customized-select-native">
										Público Alvo
									</InputLabel>
									<NativeSelect
										id="demo-customized-select-native"
										value={publico_alvo}
										onChange={(e) => setPublico(e.target.value)}
										input={<BootstrapInput />}
										required
									>
										{profissaoCargo.map((option) => {
											return (
												<option value={option.value} key={option.value}>
													{option.label}
												</option>
											)
										})}
									</NativeSelect>
								</FormControl>
								<input type="submit" className="button" value="cadastrar público-alvo" />
							</form>
						</div>
					</div>
				</div>
			</main>
			<HomeButton />
		</Fragment>
	)
}

export default CadastrarPublico
