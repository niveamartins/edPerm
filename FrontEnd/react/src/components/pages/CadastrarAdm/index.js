import React, { Fragment, useState } from "react"
import { Redirect } from 'react-router-dom'

import api from "../../../services/api"
import { makeStyles, withStyles } from "@material-ui/core/styles"
import InputLabel from "@material-ui/core/InputLabel"
import FormControl from "@material-ui/core/FormControl"
import NativeSelect from "@material-ui/core/NativeSelect"
import InputBase from "@material-ui/core/InputBase"

import { NavBar } from "../../navbar"
import './cadAdm.css'

function CadastrarAdm(props) {
	const [user, setAdm] = useState("")

	// let info = props.location.state

	const user_type = localStorage.getItem("user_type")
	let redirectIfNotAuth = null
	if (user_type !== "adm") redirectIfNotAuth = <Redirect to="/" />

	async function handleCreate(e) {
		// e.preventDefault()

		// const data = {
		// 	email_apoiador,
		// 	id_turma,
		// }

		// console.log(data)
		// try {
		// 	const token = localStorage.getItem("token")
		// 	const AuthStr = "Bearer ".concat(token)
		// 	api
		// 		.post("/cadastrarapoiador", data, {
		// 			headers: { Authorization: AuthStr },
		// 		})
		// 		.then((response) => {
		// 			if (response.data.hasOwnProperty("error") === true) {
		// 				alert("O e-mail cadastrado não existe no banco de dados")
		// 			} else {
		// 				alert(`O aluno foi cadastrado como apoiador da turma com sucesso!`)
		// 			}
		// 		})
		// } catch (err) {
		// 	console.log(err)
		// 	alert("Erro no cadastro, tente novamente")
		// }
   }
   
	const userOptions = [
		{ value: "", label: "Selecione o usuário" },
		{ value: "1", label: "user1" },
		{ value: "2", label: "user2" },
		{ value: "3", label: "user3" },
		{ value: "4", label: "user4" },
	]

	const BootstrapInput = withStyles((theme) => ({
		root: {
			"label + &": {
				marginTop: theme.spacing(3),
				marginBottom: "10px"
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
					<div class="form-page-container adm">
						<div class="form-container adm">
							<form onSubmit={handleCreate}>
								<h1>Cadastre o Admistrador!</h1>
								<p>Selecione abaixo o usuário a ser promovido para administrador!</p>
								<FormControl>
									<InputLabel htmlFor="demo-customized-select-native">
										Usuário
									</InputLabel>
									<NativeSelect
										id="demo-customized-select-native"
										value={user}
										onChange={(e) => setAdm(e.target.value)}
										input={<BootstrapInput />}
										required
									>
										{userOptions.map((option) => {
											return (
												<option value={option.value}>{option.label}</option>
											)
										})}
									</NativeSelect>
								</FormControl>
								<input
									type="submit"
									class="button"
									value="cadastrar adm"
								/>
							</form>
						</div>
					</div>
				</div>
			</main>
		</Fragment>
	)
}

export default CadastrarAdm
