import React, { Fragment, useState, useEffect } from "react"
import AddIcon from "@material-ui/icons/Add"
import { Link } from "../../../../node_modules/react-router-dom"

import api from "../../../services/api"
import { NavBar } from "../../navbar"

import "../ListarTurmas/listarTurmas.css"

function ListarTurmas() {
	const [turmasAluno, setTurmasAluno] = useState([])

	// aviso inicial para quando ainda não tiver turmas
	let empty = null
	if (turmasAluno.length === 0) empty = <p className="empty">Não há turmas</p>

	const usuario = localStorage.getItem("user_username")

	const data = {
		usuario,
	}

	useEffect(() => {
		try {
			const token = localStorage.getItem("token")
			const AuthStr = "Bearer ".concat(token)
			api
				.post("listaturmaaluno", data, { headers: { Authorization: AuthStr } })
				.then((response) => {
					if (response.data[0].Error && response.data[1] == "502") {
						return
					} else {
						setTurmasAluno(response.data)
					}
				})
		} catch (err) {
			alert("Não foi possível encontrar as turmas, tente novamente")
		}
	}, [])

	const getTurmasContent = (turma) => {
		let content = []
		for (let idx in turma) {
			const item = turma[idx]
			// Aqui dentro do push devemos colocar o html da parte de cada um dos contatos
			content.push(
				<div className="card">
					<table className="card-list">
						<thead>
							<tr className="title bold">
								<td>{item.nome_do_curso}</td>
							</tr>
						</thead>
						<tbody>
							<tr className="tutor">
								<td>Responsável:</td>
								<td>
									<span className="tutor__highlight bold">
										{item.nomeDoPropositor}
									</span>
								</td>

								<Link
									to={{
										pathname: "/turma",
										state: [item.id_turma],
									}}
									className="link-info"
								>
									<AddIcon id="more-details"></AddIcon>info.
								</Link>
							</tr>
						</tbody>

						<thead>
							<tr className="header bold">
								<th>Turma</th>
								<th>Informações</th>
							</tr>
						</thead>

						<tbody>
							<tr className="content">
								<td className="name">Carga horária total</td>
								<td className="value">{item.Carga_Horaria_Total}h</td>
							</tr>
						</tbody>
					</table>
				</div>
			)
		}

		return content
	}

	return (
		<Fragment>
			<NavBar />
			<main>
				<div className="card-container">
					{empty}
					{getTurmasContent(turmasAluno)}
				</div>
			</main>
		</Fragment>
	)
}

export default ListarTurmas
