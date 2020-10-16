import React, { Fragment, useState } from "react"
import { useHistory } from "react-router-dom"

import api from "../../../services/api"

import { NavBar } from "../../navbar"
import { HomeButton } from "../../HomeButton"
import "./cadApoiador.css"

function CadastrarApoiador(props) {
	const [email_apoiador, setAluno] = useState("")

	const user_username = localStorage.getItem("user_username")

	let info = props.location.state
	// console.log(info)

	const id_turma = info[0].id_turma

	const history = useHistory()

	async function handleCreate(e) {
		e.preventDefault()

		const data = {
			email_apoiador,
			id_turma,
		}

		console.log(data)
		try {
			const token = localStorage.getItem("token")
			const AuthStr = "Bearer ".concat(token)
			api
				.post("/cadastrarapoiador", data, {
					headers: { Authorization: AuthStr },
				})
				.then((response) => {
					if (response.data.hasOwnProperty("error") === true) {
						alert("O e-mail cadastrado não existe no banco de dados")
					} else {
						alert(`O aluno foi cadastrado como apoiador da turma com sucesso!`)
						history.go(0)
					}
				})
		} catch (err) {
			console.log(err)
			alert("Erro no cadastro, tente novamente")
		}
	}

	return (
		<Fragment>
			<NavBar />
			<main className="main">
				<div className="card-container">
					<div className="card">
						<table className="card-list">
							<tr className="title">
								<td>{info[0].nome_do_curso}</td>
							</tr>
							<tr className="tutor">
								<td>Responsável:</td>
								<td>
									<span className="tutor__highlight">
										{info[0].NomeDoPropositor}
									</span>
								</td>
							</tr>
							<tr className="header">
								<th>Turma</th>
								<th>Informações</th>
							</tr>
							<tr className="content">
								<td className="name">Carga horária total</td>
								<td className="value">{info[0].carga_horaria_total}</td>
							</tr>
							<tr className="content">
								<td className="name">Tolerância</td>
								<td className="value">{info[0].tolerancia}</td>
							</tr>
							<tr className="content">
								<td className="name">Modalidade</td>
								<td className="value">{info[0].modalidade}</td>
							</tr>
						</table>
					</div>
				</div>
				<div className="info-turmas apoiador">
					<div class="form-page-container apoiador">
						<div class="form-container apoiador">
							<form onSubmit={handleCreate}>
								<h1>Cadastre o apoiador!</h1>
								<p>Insira abaixo o código do aluno escolhido</p>
								<br />
								<input
									name="aluno"
									class="form-input"
									placeholder="E-mail do Aluno"
									value={email_apoiador}
									onChange={(e) => setAluno(e.target.value)}
									required
								/>
								<input
									type="submit"
									class="button"
									value="cadastrar apoiador"
								/>
							</form>
						</div>
					</div>
				</div>
			</main>
			<HomeButton />
		</Fragment>
	)
}

export default CadastrarApoiador
