import React, { Fragment, useState, useEffect } from "react"
import AddIcon from "@material-ui/icons/Add"
import { Link } from "../../../../node_modules/react-router-dom"

import api from "../../../services/api"
import { NavBar } from "../../navbar"
import { Footer } from "../../footer"
import { Accessibility } from "../../accessibility"

import "./listarTurmas.css"

function ListarTurmas() {
	const [turmas, setTurmas] = useState([])

	useEffect(() => {
		try {
			api.get("listaturma").then((response) => {
				setTurmas(response.data)
			})
		} catch (err) {
			alert("Não foi possível encontrar as turmas, tente novamente")
		}
	}, [])

	const getTurmasContent = (turma) => {
		let content = []
		for (let idx in turma) {
			const item = turma[idx]
			content.push(
				<div className="card">
					<table className="card-list">
						<thead>
							<tr className="title">
								<td>{item.nome_do_curso}</td>
							</tr>
						</thead>
						<tbody>
							<tr className="tutor">
								<td>Responsável:</td>
								<td>
									<span className="tutor__highlight">
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
							<tr className="header">
								<th>Turma</th>
								<th>Informações</th>
							</tr>
						</thead>

						<tbody>
							<tr className="content">
								<td className="name">Carga horária total</td>
								<td className="value">{item.Carga_Horaria_Total}</td>
							</tr>
						</tbody>
					</table>
				</div>
			)

			/*<tr className="content">
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
                            </tr>*/
			// Aqui dentro do push devemos colocar o html da parte de cada um dos contatos
		}

		return content
	}

	return (
		<Fragment>
			<Accessibility />
			<NavBar />
			<main>
				<div className="card-container">
                    {getTurmasContent(turmas)}
                </div>
			</main>
			<Footer />
		</Fragment>
	)
}

export default ListarTurmas
