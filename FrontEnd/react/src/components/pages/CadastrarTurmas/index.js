import React, { Fragment, useState } from "react"
import { useHistory } from "react-router-dom"
import Select from "react-select"


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
			let resposta

			const token = localStorage.getItem("token")
			const AuthStr = "Bearer ".concat(token)
			await api
				.post("/cadastrarturma", data, { headers: { Authorization: AuthStr } })
				.then((response) => {
					resposta = response.data
				})
			history.push({
				pathname: "/cadastroTurmaEfetuado",
				state: { detail: resposta },
			})

			// alert(`A turma foi cadastrada com sucesso!`)
		} catch (err) {
			console.log(err)
			alert("Erro no cadastro, tente novamente")
		}
	}

	const toleranciaOptions = [
		{ value: "75", label: "75%" },
		{ value: "80", label: "80%" },
		{ value: "90", label: "90%" },
		{ value: "95", label: "95%" },
	]

	const modalidadeOptions = [
		{ value: "presencial", label: "Presencial" },
		{ value: "semipresencial", label: "Semipresencial" },
		{ value: "distancia", label: "A distância" },
	]

	//const publicoAlvo = []

	//Select styles
	const customSelectStyles = {
		option: (base, state) => ({
			...base,
			backgroundColor: state.isSelected ? "hsl(0, 0%, 95%)" : "ccc",
			color: "000",
			outline: "none",
			// This line disable the blue border
			boxShadow: state.isFocused ? 0 : 0,
			"&:hover": {
				border: state.isFocused ? 1 : 1,
			},
		}),
	}
	const theme = (theme) => ({
		...theme,
		colors: {
			...theme.colors,
			primary25: "#eee",
			primary: "#eee",
		},
		borderRadius: 0,
	})

	return (
		<Fragment>
			<Accessibility />
			<NavBar />
			<main className="main">
				<main className="main-content-forms">
					<div className="form-page-container">
						<div className="form-container">
							<h1>Cadastre sua turma!</h1>
							<p>Cadastre aqui sua turma Educação Permanente.</p>
							<form onSubmit={handleCreate}>
								<input
									name="nome"
									className="form-input"
									placeholder="Nome do Curso"
									value={nome_do_curso}
									onChange={(e) => setTurma(e.target.value)}
									required
								/>
								<input
									name="carga"
									className="form-input"
									placeholder="Carga Horária"
									maxLength="3"
									value={carga_horaria_total}
									onChange={(e) => setCarga(e.target.value)}
									required
								/>
								{/* <input
									name="tolerancia"
									className="form-input-second"
									placeholder="Tolerância"
									value={tolerancia}
									onChange={(e) => setTolerancia(e.target.value)}
									required
								/> */}
								<Select
									styles={customSelectStyles}
									theme={theme}
									className="select"
									placeholder="Tolerância"
									options={toleranciaOptions}
									onChange={(value) => setTolerancia(value.value)}
								/>
								{/* <input
									name="modalidade"
									className="form-input"
									placeholder="Modalidade"
									value={modalidade}
									onChange={(e) => setModalidade(e.target.value)}
									required
								/> */}
								<Select
									styles={customSelectStyles}
									theme={theme}
									className="select"
									placeholder="Modalidade"
									options={modalidadeOptions}
									onChange={(value) => setModalidade(value.value)}
								/>
								<input
									name="tag"
									className="form-input"
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
