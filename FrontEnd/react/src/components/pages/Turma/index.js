import React, { Fragment, useState, useEffect } from "react"
// import AddIcon from '@material-ui/icons/Add';
import { Link } from "../../../../node_modules/react-router-dom"

import api from "../../../services/api"
import { NavBar } from "../../navbar"
import { HomeButton } from '../../HomeButton'

import "./Turma.css"

//colocar com o link da turma
import LinkIcon from "@material-ui/icons/Link"
import { capitalize } from "@material-ui/core"

function Turma(props) {
	const [turma, setTurmas] = useState([])

	let cadastrarApoiador = null
	let darPresenca = null

	const user_username = localStorage.getItem("user_username")

	const adm = localStorage.getItem("adm")
	const gestor = localStorage.getItem("gestor")
	const coordenador = localStorage.getItem("coordenador")
	const propositor = localStorage.getItem("propositor")
	const apoiador = localStorage.getItem("apoiador")

	// usuários que poderiam ter cadastrado a turma
	const allowedAllUser =
		adm === "true" ||
		coordenador === "true" ||
		gestor === "true" ||
		propositor === "true"

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
							<tr className="title">
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
								<td className="value">{item.carga_horaria_total}h</td>
							</tr>
							<tr className="content">
								<td className="name">Tolerância</td>
								<td className="value">{item.tolerancia}%</td>
							</tr>
							<tr className="content">
								<td className="name">Modalidade</td>
								<td className="value">{capitalize(item.modalidade)}</td>
							</tr>
						</table>
					</div>
				</div>
			)
		}

		return content
	}

	// checando se nome do usuário é o mesmo que o nome do propositor que está na turma
	const propositorTurma = turma[0] ? turma[0].NomeDoPropositor : ''
	const isPropositor = user_username == propositorTurma

	if (allowedAllUser &&  isPropositor) {
		cadastrarApoiador = (
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
		)

		darPresenca = (
			<Link to={"/leitor/" + id} className="link">
						<button className="button bold">
							<label>Dar Presença</label>
						</button>
					</Link>
		)
	}
	
	// se for usuário apoiador o leitor de presença também é exibido
	// se não for apoiador da turma o back irá proibir
	if (apoiador === "true") {
		darPresenca = (
			<Link to={"/leitor/" + id} className="link">
						<button className="button bold">
							<label>Dar Presença</label>
						</button>
					</Link>
		)
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
						<button className="button bold">
							<label>Criar Aula</label>
						</button>
					</Link>
						{cadastrarApoiador}
					<Link to="/aulas" className="link">
						<button className="button bold" disabled>
							<label>Aulas</label>
						</button>
					</Link>
					{darPresenca}
				</div>
			</main>
			<HomeButton />
		</Fragment>
	)
}

export default Turma
