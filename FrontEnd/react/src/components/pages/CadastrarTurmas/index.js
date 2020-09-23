import React, { Fragment, useState, useEffect } from "react"
import { useHistory } from "react-router-dom"
import { Redirect } from "react-router-dom"

import { withStyles } from "@material-ui/core/styles"
import InputLabel from "@material-ui/core/InputLabel"
import FormControl from "@material-ui/core/FormControl"
import NativeSelect from "@material-ui/core/NativeSelect"
import Select from "@material-ui/core/Select"
import Checkbox from "@material-ui/core/Checkbox"
import InputBase from "@material-ui/core/InputBase"

import "./cadastroTurma.css"
import api from "../../../services/api"
import { profissaoCargo } from "../CadastroUsuario/data/profissaoData"

// import { Link } from './node_modules/react-router-dom';
import { NavBar } from "../../navbar"
import { HomeButton } from "../../HomeButton"

function CadastrarTurma() {
	const responsavel = localStorage.getItem("user_id")

	let redirectIfNotAuth = null
	const adm = localStorage.getItem("adm")
	const gestor = localStorage.getItem("gestor")
	const coordenador = localStorage.getItem("coordenador")
	const propositor = localStorage.getItem("propositor")

	const allowedToCreateTurma =
		adm === "true" ||
		coordenador === "true" ||
		gestor === "true" ||
		propositor === "true"

	if (!allowedToCreateTurma) {
		redirectIfNotAuth = <Redirect to="/opcoesTurmas" />
	}

	const [nome_do_curso, setTurma] = useState("")
	const [carga_horaria_total, setCarga] = useState("")
	// campos iniciais no select (tolerancia e modalidade)
	const [tolerancia, setTolerancia] = useState("75")
	const [modalidade, setModalidade] = useState("presencial")
	const [turma_tag, setTag] = useState([])

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

	const profissaoAdapted = profissaoCargo.filter((profissao) => profissao.value)
	profissaoAdapted.push({ label: "Selecione seu público alvo", value: "" })

	useEffect(() => {
		console.log(turma_tag)
	}, [turma_tag])

	const BootstrapInput = withStyles((theme) => ({
		root: {
			"label + &": {
				marginTop: theme.spacing(3),
				marginBottom: "10px",
			},
		},
		input: {
			borderRadius: 4,
			position: "relative",
			backgroundColor: "hsl(0, 0%, 95%)",
			width: "100%",
			border: "1px solid #ced4da",
			fontSize: 16,
			padding: "10px 26px 10px 12px",
			transition: theme.transitions.create(["border-color", "box-shadow"]),
			// Use the system font instead of the default Roboto font.
			fontFamily: [
				"-apple-system",
				"BlinkMacSystemFont",
				'"Segoe UI"',
				"Roboto",
				'"Helvetica Neue"',
				"Arial",
				"sans-serif",
				'"Apple Color Emoji"',
				'"Segoe UI Emoji"',
				'"Segoe UI Symbol"',
			].join(","),
			"&:focus": {
				borderRadius: 4,
				borderColor: "#80bdff",
				boxShadow: "0 0 0 0.2rem rgba(0,123,255,.25)",
			},
		},
	}))(InputBase)

	return (
		<Fragment>
			{redirectIfNotAuth}
			<NavBar />
			<main className="main">
				<main className="main-content-forms">
					<div className="form-page-container cad-turma">
						<div className="form-container">
							<h1 className="bold">Cadastre sua turma!</h1>
							<p>Cadastre aqui sua turma de Educação Permanente.</p>
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

								<label for="select-tolerancia" className="select-input__label">
									Selecione a tolerância
								</label>
								<FormControl>
									<NativeSelect
										id="select-tolerancia"
										value={tolerancia}
										onChange={(e) => setTolerancia(e.target.value)}
										input={<BootstrapInput />}
										required
									>
										{toleranciaOptions.map((option) => {
											return (
												<option value={option.value}>{option.label}</option>
											)
										})}
									</NativeSelect>
								</FormControl>
								<label for="select-modalidade" className="select-input__label">
									Selecione a modalidade
								</label>
								<FormControl>
									<NativeSelect
										id="select-modalidade"
										value={modalidade}
										onChange={(e) => setModalidade(e.target.value)}
										input={<BootstrapInput />}
										required
									>
										{modalidadeOptions.map((option) => {
											return (
												<option value={option.value}>{option.label}</option>
											)
										})}
									</NativeSelect>
								</FormControl>

								<label for="select-publico" className="select-input__label">
									Selecione o público alvo
								</label>

								{/* multiple */}
								<FormControl>
									<NativeSelect
										id="select-publico"
										value={turma_tag}
										onChange={(e) => setTag(e.target.value)}
										input={<BootstrapInput />}
										required
									>
										{profissaoAdapted.map((option) => {
											return (
												<option value={option.value}>{option.label}</option>
											)
										})}
									</NativeSelect>
								</FormControl>
								{/* <div className="selected-tags__container">
									{turma_tag && turma_tag.map((tag) => (
										<p className="selected-tags">{tag}; </p>
									))}
								</div> */}
								<input
									type="submit"
									className="button bold"
									id="cad__class-button"
									value="cadastrar Turma"
								/>
							</form>
						</div>
					</div>
				</main>
			</main>
			<HomeButton />
		</Fragment>
	)
}

export default CadastrarTurma
