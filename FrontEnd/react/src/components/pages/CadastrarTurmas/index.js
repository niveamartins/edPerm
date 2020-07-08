import React, { Fragment, useState } from "react"
import { useHistory } from 'react-router-dom'

import "./cadastroTurma.css"
import api from "../../../services/api"

// import { Link } from './node_modules/react-router-dom';
import { NavBar } from "../../navbar"
import { Footer } from "../../footer"
import { Accessibility } from "../../accessibility"

function CadastrarTurma() {
	const responsavel = localStorage.getItem("user_id")

	const [nome_do_curso, setTurma] = useState("")
	const [carga_horaria_total, setCarga] = useState("")
	const [tolerancia, setTolerancia] = useState("")
	const [modalidade, setModalidade] = useState("")
  const [turma_tag, setTag] = useState("")
  
  const history = useHistory()

	async function handleCreate(e) {
		e.preventDefault()

		const data = {
			responsavel,
			nome_do_curso,
			carga_horaria_total,
			tolerancia,
			modalidade,
			turma_tag,
		}

		try {
			api.post("/cadastrarturma", data)

      // alert(`A turma foi cadastrada com sucesso!`)
      history.push("/cadastroTurmaEfetuado")
      
		} catch (err) {
			console.log(err)
			alert("Erro no cadastro, tente novamente")
		}
	}

	return (
		<Fragment>
			<Accessibility />
			<NavBar />
			<main className="main">
				<main className="main-content-forms">
					<div class="form-page-container">
						<div class="form-container">
							<h1>Cadastre sua turma!</h1>
							<p>Cadastre aqui sua turma Educação Permanente.</p>
							<form onSubmit={handleCreate}>
								<input
									name="nome"
									class="form-input"
									placeholder="Nome do Curso"
									value={nome_do_curso}
									onChange={(e) => setTurma(e.target.value)}
									required
								/>
								{/* <div class="form-line"> */}
								{/* </div> */}
								{/* <div class="form-line"> */}
								<input
									name="carga"
									class="form-input"
									placeholder="Carga Horária"
									value={carga_horaria_total}
									onChange={(e) => setCarga(e.target.value)}
									required
								/>
								<input
									name="tolerancia"
									class="form-input-second"
									placeholder="Tolerância"
									value={tolerancia}
									onChange={(e) => setTolerancia(e.target.value)}
									required
								/>
								{/* </div> */}
								<input
									name="modalidade"
									class="form-input"
									placeholder="Modalidade"
									value={modalidade}
									onChange={(e) => setModalidade(e.target.value)}
									required
								/>
								<input
									name="tag"
									class="form-input"
									placeholder="Tag"
									value={turma_tag}
									onChange={(e) => setTag(e.target.value)}
									required
								/>
								<input
									type="submit"
									className="button"
									id="cad__class-button"
									value="cadastrar Turma"
								/>
							</form>
						</div>
					</div>
				</main>
			</main>
			<Footer />
		</Fragment>
	)
}

export default CadastrarTurma
