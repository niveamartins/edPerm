import React, { Fragment, useState, useEffect } from "react"
import {useHistory} from 'react-router-dom'
import api from "../../../services/api"
import "./criarAula.css"

import { NavBar } from "../../navbar"

const CriarAula = (props) => {
	const [nome_da_aula, setNomeAula] = useState("")
	const [dataInicio, setDataInicio] = useState("")
	const [dataTermino, setDataTermino] = useState("")
	const [horaInicio, setHoraInicio] = useState("")
	const [horaTermino, setHoraTermino] = useState("")

	const [hInicio, setInicio] = useState("")
	const [hTermino, setTermino] = useState("")

	// corrigindo formato de data
	const updateDateFormat = (date) => {
		const year = date.substring(0,4)
		const month = date.substring(5,7)
		const day = date.substring(8,10)
		const updatedDate = `${day}/${month}/${year}`
		return updatedDate
	}

	// montando o formato data-hora aceito pelo backend
	useEffect(() => {
		const formatedInitialDate = updateDateFormat(dataInicio)
		const formatedFinishDate = updateDateFormat(dataTermino)

		const horarioInicial = `${formatedInitialDate}-${horaInicio}:00`
		const horarioTermino = `${formatedFinishDate}-${horaTermino}:00`

		setInicio(horarioInicial)
		setTermino(horarioTermino)
	}, [dataInicio, dataTermino, horaInicio, horaTermino])

	const history = useHistory()

	const info = props.location.state
	const nome_do_curso = info[0].nome_do_curso

	async function handleCreate(e) {
		e.preventDefault()

		const data = {
			nome_do_curso,
			nome_da_aula,
			hInicio,
			hTermino,
		}

		console.log(data)

		try {
			const token = localStorage.getItem("token")
			const AuthStr = "Bearer ".concat(token)
			api
				.post("/cadastraraula", data, {
					headers: { Authorization: AuthStr },
				})
				.then((response) => {
					if (response.data.hasOwnProperty("error") === true) {
						alert("Não foi possível cadastrar aula")
					} else {
						alert("A aula foi cadastrada com sucesso!")
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
							<tr className="content">
								<td className="name">Tag</td>
								<td className="value">{info[0].modalidade}</td>
							</tr>
						</table>
					</div>
				</div>
				<div className="info-turmas">
					<div class="form-page-container cadAulaContainer">
						<div class="form-container">
							<form onSubmit={handleCreate} className="cadAula">
								<h1>Cadastre sua aula!</h1>
								<input
									type="name"
									placeholder="Nome da aula"
									value={nome_da_aula}
									onChange={(e) => setNomeAula(e.target.value)}
									required
								/>
								<label for="data-inicio">
									Data de início (formato mês/dia/ano)
								</label>
								<input
									type="date"
									id="data-inicio"
									value={dataInicio}
									onChange={(e) => setDataInicio(e.target.value)}
									required
								/>
								<label for="data-termino">
									Data de término (formato mês/dia/ano)
								</label>
								<input
									type="date"
									id="data-termino"
									value={dataTermino}
									onChange={(e) => setDataTermino(e.target.value)}
									required
								/>
								<label for="horario-inicio">
									Horário de início (formato AM/PM)
								</label>
								<input
									type="time"
									id="horario-inicio"
									class="form-input"
									placeholder="Hora de Início"
									value={horaInicio}
									onChange={(e) => setHoraInicio(e.target.value)}
									required
								/>
								<label for="horario-termino">
									Horário de término (formato AM/PM)
								</label>
								<input
									type="time"
									id="horario-termino"
									class="form-input"
									placeholder="Hora de Término"
									value={horaTermino}
									onChange={(e) => setHoraTermino(e.target.value)}
									required
								/>
								<input type="submit" class="button" value="cadastrar aula" />
							</form>
						</div>
					</div>
				</div>
			</main>
		</Fragment>
	)
}

export default CriarAula
