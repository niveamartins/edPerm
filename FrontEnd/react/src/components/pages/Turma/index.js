import React, { Fragment, useState, useEffect } from "react"
// import AddIcon from '@material-ui/icons/Add';
import { Link } from "../../../../node_modules/react-router-dom"

import api from "../../../services/api"
import { NavBar } from "../../navbar"

import "./Turma.css"

//colocar com o link da turma
import LinkIcon from "@material-ui/icons/Link"
import { capitalize } from "@material-ui/core"

function Turma(props) {
	const [turma, setTurmas] = useState([])

	const id = props.location.state
	const url = "listaturma/" + id
	useEffect(() => {
		try {
			const token = localStorage.getItem("token")
			const AuthStr = "Bearer ".concat(token)
			api.get(url, { headers: { Authorization: AuthStr } }).then((response) => {
				setTurmas(response.data)
			})
		} catch (err) {
			alert("Não foi possível encontrar a turma desejada, tente novamente")
		}
	}, [])

	const getTurmaContent = (turma) => {
		let content = []
		for (let idx in turma) {
			const item = turma[idx]
			content.push(
				<div className="card-container">
					<div className="card">
						<table className="card-list">
							<tr className="title bold">
								<td>{item.nome_do_curso}</td>
							</tr>
							<tr className="tutor">
								<td>Responsável:</td>
								<td>
									<span className="tutor__highlight bold">
										{item.NomeDoPropositor}
									</span>
								</td>
							</tr>
							<tr className="header">
								<th>Turma</th>
								<th>Informações</th>
							</tr>
							<tr className="content">
								<td className="name">Carga horária total</td>
								<td className="value bold">{item.carga_horaria_total}h</td>
							</tr>
							<tr className="content">
								<td className="name">Tolerância</td>
								<td className="value bold">{item.tolerancia}%</td>
							</tr>
							<tr className="content">
								<td className="name">Modalidade</td>
								<td className="value bold">{capitalize(item.modalidade)}</td>
							</tr>
						</table>
					</div>
				</div>
			)
		}

		return content
	}

	return (
		<Fragment>
			<NavBar />
			<main className="main turma">
				{getTurmaContent(turma)}
				<div className="nav-info-turmas">
					<Link to="/presenca" className="link">
						<button className="button bold" disabled>
							<label>Lista de Presença</label>
						</button>
					</Link>
					<Link
						to={{
							pathname: "/cadaula",
							state: turma,
						}}
						className="link"
					>
						<button className="button bold" disabled>
							<label>Criar Aula</label>
						</button>
					</Link>
					<Link
						to={{
							pathname: "/cadapoiador",
							state: turma,
						}}
						className="link"
					>
						<button className="button bold">
							<label>Cadastrar Aluno Apoiador</label>
						</button>
					</Link>
					<Link to="/aulas" className="link">
						<button className="button bold" disabled>
							<label>Aulas</label>
						</button>
					</Link>
					<Link to="/leitor" className="link">
						<button className="button bold">
							<label>Dar Presença</label>
						</button>
					</Link>
				</div>
			</main>
		</Fragment>
	)
}

export default Turma
