import React, { Fragment, useState, useEffect } from "react"
// import AddIcon from '@material-ui/icons/Add';
import { Link } from "../../../../node_modules/react-router-dom"
import ArrowBackIcon from "@material-ui/icons/ArrowBack"
import api from "../../../services/api"
import "./criarAula.css"

import { NavBar } from "../../navbar"
import { Footer } from "../../footer"
import { Accessibility } from "../../accessibility"

const CriarAula = props => {

    const [turma, setTurma] = useState("")
    const [dia, setDia] = useState("")
    const [horaInicio, setInicio] = useState("")
    const [horaTermino, setTermino] = useState("")
    const [propositor, setPropositor] = useState("")
    
    
    const info = props.location.state[0][0]
    setTurma(info.id_turma)

	setPropositor("aaaaa") // Mudar aqui quando tiver o login setado.

	async function handleCreate(e) {
		e.preventDefault()

		const data = {
			turma,
			dia,
			horaInicio,
			horaTermino,
			propositor,
		}

		// try {
		//   api.post("/cadastrarhorario", data);

		//   alert(`A aula foi cadastrada com sucesso!`);

		// } catch (err) {
		//   console.log(err);
		//   alert("Erro no cadastro, tente novamente");
		// }
	}

	return (
		<Fragment>
			<Accessibility />
			<NavBar />
			<main className="main">
				<a href="/turma">
					<ArrowBackIcon id="return-icon" />
				</a>
				<div className="card-container">
					<div className="card">
						<table className="card-list">
							<tr className="title">
								<td>{info.nome_do_curso}</td>
							</tr>
							<tr className="tutor">
								<td>Responsável:</td>
								<td>
									<span className="tutor__highlight">
										{info.NomeDoPropositor}
									</span>
								</td>
							</tr>
							<tr className="header">
								<th>Turma</th>
								<th>Informações</th>
							</tr>
							<tr className="content">
								<td className="name">Carga horária total</td>
								<td className="value">{info.carga_horaria_total}</td>
							</tr>
							<tr className="content">
								<td className="name">Tolerância</td>
								<td className="value">{info.tolerancia}</td>
							</tr>
							<tr className="content">
								<td className="name">Modalidade</td>
								<td className="value">{info.modalidade}</td>
							</tr>
							<tr className="content">
								<td className="name">Tag</td>
								<td className="value">{info.modalidade}</td>
							</tr>
						</table>
					</div>
				</div>
				<div className="info-turmas">
					<div class="form-page-container">
						<div class="form-container">
							<form onSubmit={handleCreate}>
								<h1>Cadastre sua aula!</h1>
								<input
									type="date"
									name="data"
									class="form-input"
									placeholder="Dia da Semana"
									value={dia}
									onChange={(e) => setDia(e.target.value)}
									required
								/>
								<input
									type="time"
									name="inicio"
									class="form-input"
									placeholder="Hora de Início"
									value={horaInicio}
									onChange={(e) => setInicio(e.target.value)}
									required
								/>
								<input
									type="time"
									name="inicio"
									class="form-input"
									placeholder="Hora de Término"
									value={horaTermino}
									onChange={(e) => setTermino(e.target.value)}
									required
								/>
								<input type="submit" class="button" value="cadastrar aula" />
							</form>
						</div>
					</div>
				</div> 
			</main>
			<Footer />
		</Fragment>
	)
}

export default CriarAula
