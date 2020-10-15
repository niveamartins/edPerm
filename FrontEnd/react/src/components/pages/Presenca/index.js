import React, { Fragment } from "react"
import { capitalize } from "@material-ui/core"

import { NavBar } from "../../navbar"
import "./presenca.css"

function Presenca(props) {
	const info = props.location.state
	console.log(info[0])

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

								<tr class="header">
									<th class="header__first-presence">Alunos</th>
									<th>Presenças</th>
								</tr>

								<tr class="students">
									<td class="presence__name">Feitosa</td>
									<td class="value">2</td>
								</tr>
							</table>
						</div>
					</div>
				</div>
			</main>
		</Fragment>
	)
}

export default Presenca
