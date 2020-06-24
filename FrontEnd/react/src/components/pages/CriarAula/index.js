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

    const [dia, setDia] = useState("")
    const [horaInicio, setInicio] = useState("")
    const [horaTermino, setTermino] = useState("")
    // const [propositor, setPropositor] = useState("")
    
    
	const info = props.location.state
	const turma = info[0].id_turma
	const propositor = "Wilton"

	// setPropositor("aaaaa") // Mudar aqui quando tiver o login setado.

	async function handleCreate(e) {
		e.preventDefault()

		const data = {
			turma,
			dia,
			horaInicio,
			horaTermino,
			propositor,
		}

		console.log(data)

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
				{/* <Link to="/turma">
					<ArrowBackIcon id="return-icon" />
				</Link> */}
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
					<div class="form-page-container">
						<div class="form-container">
							<form onSubmit={handleCreate}>
								<h1>Cadastre sua aula!</h1>
								<select 
									class="form-input"
									name="data" 
									onChange={(e) => setDia(e.target.value)}
									required>
									<option value="Segunda">Segunda</option> 
									<option value="Terça" selected>Terça</option>
									<option value="Quarta">Quarta</option>
									<option value="Quinta">Quinta</option>
									<option value="Sexta">Sexta</option>	
								</select>
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
