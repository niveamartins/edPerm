import React, { Fragment, useState, useEffect } from "react"
import { Redirect, useHistory } from "react-router-dom"

import api from "../../../services/api"
import { withStyles } from "@material-ui/core/styles"
import InputLabel from "@material-ui/core/InputLabel"
import FormControl from "@material-ui/core/FormControl"
import NativeSelect from "@material-ui/core/NativeSelect"
import InputBase from "@material-ui/core/InputBase"

import { NavBar } from "../../navbar"
import { HomeButton } from "../../HomeButton"

function CadastrarGestor(props) {
	const [listaUsers, setListaUsers] = useState([])
	const [id, setGestorId] = useState("")

	const adm = localStorage.getItem("adm")
	const gestor = localStorage.getItem("gestor")
	let redirectIfNotAuth = null
	const allowedUsers = adm === "true" || gestor === "true"
	if (!allowedUsers) redirectIfNotAuth = <Redirect to="/" />

	const history = useHistory()

	// loading users on page load
	useEffect(() => {
		try {
			const token = localStorage.getItem("token")
			const AuthStr = "Bearer ".concat(token)
	
			api
				.get("/listausuario", { headers: { Authorization: AuthStr } })
				.then((response) => {
					const notGestores = response.data.filter((user) => user.Adm == "Não").filter((user) => user.Gestor == "Não")
					setListaUsers(notGestores)
					setGestorId(notGestores[0].Id)
				})
		} catch (err) {
			console.log(err)
			alert("Não foi possível listar usuários")
		}
	}, [])

	async function handleCreate(e) {
		e.preventDefault()
		const data = {
			id,
		}
		console.log(data)
		try {
			const token = localStorage.getItem("token")
			const AuthStr = "Bearer ".concat(token)
			api
				.post("/transformaremgestor", data, {
					headers: { Authorization: AuthStr },
				})
				.then((response) => {
					if (response.data.hasOwnProperty("error") === true) {
						alert("Não foi possível promover usuário a gestor")
					} else {
						alert("O usuário foi promovido a gestor com sucesso!")
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
					<div className="form-page-container adm">
						<div className="form-container adm">
							<form onSubmit={handleCreate}>
								<h1>Cadastre o Gestor!</h1>
								<p>
									Selecione abaixo o usuário a ser promovido para gestor
								</p>
								<br />
								<FormControl>
									<InputLabel htmlFor="demo-customized-select-native">
										Usuário
									</InputLabel>
									<NativeSelect
										id="demo-customized-select-native"
										value={id}
										onChange={(e) => setGestorId(e.target.value)}
										input={<BootstrapInput />}
										required
									>
										{listaUsers.map((option) => {
											return (
												<option value={option.Id} key={option.Id}>
													{option.Usuario}
												</option>
											)
										})}
									</NativeSelect>
								</FormControl>
								<input type="submit" className="button" value="cadastrar gestor" />
							</form>
						</div>
					</div>
				</div>
			</main>
			<HomeButton />
		</Fragment>
	)
}

export default CadastrarGestor
