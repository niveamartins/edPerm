import React, { Fragment, useState, useEffect } from "react"
import api from "../../../services/api"
import { capitalize } from "@material-ui/core"

import { NavBar } from "../../navbar"
import "./presenca.css"

function Presenca(props) {
	const [presenca, setPresenca] = useState("")

	const info = props.location.state
	const nome_do_curso = info[0].nome_do_curso
	const data = {
		nome_do_curso,
	}

	useEffect(() => {
		try {
			const token = localStorage.getItem("token")
			const AuthStr = "Bearer ".concat(token)
			api
				.post("/listarPresencaTotal", data, {
					headers: { Authorization: AuthStr },
				})
				.then((response) => {
					setPresenca(response.data)
				})
		} catch (err) {
			alert("Não foi possível encontrar as turmas, tente novamente")
		}
	}, [])

	let displayedPresenca = null
	if (presenca) {
		displayedPresenca = presenca.map((dadosPresenca) => (
			<>
				<tr class="students">
					<td class="presence__name">{dadosPresenca.nome}</td>
					<td class="value"></td>
				</tr>
				<tr class="students__data">
					<td>Número de presenças</td>
					<td class="value">{dadosPresenca.numero_de_presencas}</td>
				</tr>
				<tr class="students__data">
					<td>Horas</td>
					<td class="value">{dadosPresenca.horas}</td>
				</tr>
				<tr class="students__data">
					<td>Minutos</td>
					<td class="value">{dadosPresenca.minutos}</td>
				</tr>
				<tr class="students__data">
					<td>Segundos</td>
					<td class="value">{dadosPresenca.segundos}</td>
				</tr>
			</>
		))
	} 
	if (presenca.length === 0) {
		displayedPresenca = <p>Não há dados de presença</p>
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
									<span className="tutor__highlight bold">
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
								<td className="value">{info[0].carga_horaria_total}h</td>
							</tr>
							<tr className="content">
								<td className="name">Tolerância</td>
								<td className="value">{info[0].tolerancia}%</td>
							</tr>
							<tr className="content">
								<td className="name">Modalidade</td>
								<td className="value">{capitalize(info[0].modalidade)}</td>
							</tr>
						</table>
					</div>
					<div className="info-turmas">
						<div class="card presenca">
							<table class="presence-list">
								<tr class="title">
									<td>Lista de presença</td>
								</tr>
								{displayedPresenca}
							</table>
						</div>
					</div>
				</div>
			</main>
		</Fragment>
	)
}

export default Presenca
