import React, { Fragment, useState } from "react"
import { Redirect } from 'react-router-dom'

import api from "../../../services/api"

import { NavBar } from "../../navbar"
import './cadAdm.css'

function CadastrarAdm(props) {
	// const [email_apoiador, setAluno] = useState("")

	// let info = props.location.state

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
   
   const user_type = localStorage.getItem("user_type")
   let redirectIfNotAuth = null
   if (user_type !== "adm") redirectIfNotAuth = <Redirect to="/" />

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
								<p>Insira abaixo o código do usuário a ser promovido para admnistrador.</p>
                        <br/>
								<input
									name="usuario"
									class="form-input"
									placeholder="E-mail do Usuário"
									// value={email_apoiador}
									// onChange={(e) => setAluno(e.target.value)}
									required
								/>
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
