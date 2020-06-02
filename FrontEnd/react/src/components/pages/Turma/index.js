import React, { Fragment } from "react"
// import AddIcon from '@material-ui/icons/Add';
import { Link } from "../../../../node_modules/react-router-dom"

import { NavBar } from "../../navbar"
import { Footer } from "../../footer"
import { Accessibility } from "../../accessibility"

import "./Turma.css"

function Turma() {
	//preencher dados da turma com db

	return (
		<Fragment>
			<Accessibility />
			<NavBar />
			<main className="main">
				<div className="card-container">
					<div className="card">
						<table className="card-list">
							<tr className="title">
								<td>Natação</td>
							</tr>
							<tr className="tutor">
								<td>Responsável:</td>
								<td>
									<span className="tutor__highlight">Fulaninho</span>
								</td>
							</tr>
							<tr className="header">
								<th>Turma</th>
								<th>Informações</th>
							</tr>
							<tr className="content">
								<td className="name">Dia</td>
								<td className="value">Terça</td>
							</tr>
							<tr className="content">
								<td className="name">Hora</td>
								<td className="value">13:00</td>
							</tr>
							<tr className="content">
								<td className="name">Carga horária total</td>
								<td className="value">15min</td>
							</tr>
							<tr className="content">
								<td className="name">Tolerância</td>
								<td className="value">120h</td>
							</tr>
							<tr className="content">
								<td className="name">Tolerância</td>
								<td className="value">15min</td>
							</tr>
							<tr className="content">
								<td className="name">Modalidade</td>
								<td className="value">Esportes</td>
							</tr>
							<tr className="content">
								<td className="name">Tag</td>
								<td className="value">Atividade Física</td>
							</tr>
						</table>
					</div>

					<div className="nav-info-turmas">
						<Link to="/presenca" className="link">
							<button size="large" class="button" disabled>
								<label>Lista de Presença</label>
							</button>
						</Link>
						<Link to="/relatorios" className="link">
							<button size="large" class="button">
								<label>Relatórios</label>
							</button>
						</Link>
						<Link to="/cadaula" className="link">
							<button size="large" class="button">
								<label>Criar Aula</label>
							</button>
						</Link>
						<Link to="/cadapoiador" className="link">
							<button size="large" class="button">
								<label>Cadastrar Aluno Apoiador</label>
							</button>
						</Link>
						<Link to="/aulas" className="link">
							<button size="large" class="button" disabled>
								<label>Aulas</label>
							</button>
						</Link>
					</div>
				</div>
			</main>
			<Footer />
		</Fragment>
	)
}

export default Turma
