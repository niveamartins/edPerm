//FALTA EXIBIR DADOS DE AULAS QUANDO BACK FOR CORRIGIDO


import React, { Fragment, useEffect, useState } from "react"
import { Link } from "../../../../node_modules/react-router-dom"
import api from "../../../services/api"

import "./aulas.css"
import { NavBar } from "../../navbar"
import { HomeButton } from "../../HomeButton"

// preencher dados turma tipo o que acontece com as outras páginas da turma

function Aulas(props) {
	const [aulas, setAulas] = useState("")

    let info = props.location.state
    const nome_do_curso = info[0].nome_do_curso

	useEffect(() => {
		try {
			const token = localStorage.getItem("token")
			const AuthStr = "Bearer ".concat(token)
			api
				.post("/listaraulas", nome_do_curso, { headers: { Authorization: AuthStr } })
				.then((response) => {
                    setAulas(response.data)
                    console.log(response.data)
				})
		} catch (err) {
			alert("Não foi possível encontrar as turmas, tente novamente")
		}
	}, [])

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
				<div className="card-container aulas">
					<div className="card">
						<table className="card-list">
							<tr className="title">
								<td>Aulas</td>
							</tr>
							<tr className="header">
								<th>Aula 1</th>
							</tr>
							<tr className="content">
								<td className="name">Inicio</td>
								<td className="value">2020-10-12 13:00:00</td>
							</tr>
							<tr className="content">
								<td className="name">Fim</td>
								<td className="value">2020-10-16 15:00:00</td>
							</tr>
						</table>
					</div>
				</div>
			</main>
			<HomeButton />
		</Fragment>
	)
}

export default Aulas
