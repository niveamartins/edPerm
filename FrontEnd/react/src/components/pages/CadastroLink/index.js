import React, { Fragment, useState, useEffect } from "react"
import { useHistory } from "react-router-dom"

import api from "../../../services/api"

// import { Link } from './node_modules/react-router-dom';
import { NavBar } from "../../navbar"
import "./cadLink.css"

function CadastroLink(props) {
	const tokenTurma = props.match.params.token
	const id_turma = props.match.params.turma

	const [cpf, setCPF] = useState("")
	const [dadosAluno, setDA] = useState([])
	const [dadosTurma, setDT] = useState([])

	const url = "listaturma/" + id_turma

	useEffect(() => {
		try {
			const token = localStorage.getItem("token")
			const AuthStr = "Bearer ".concat(token)
			api
				.get("/dadosPessoais", { headers: { Authorization: AuthStr } })
				.then((response) => {
					setDA(response.data)
				})

			api.get(url, { headers: { Authorization: AuthStr } }).then((response) => {
				console.log(response.data)
				setDT(response.data[0])
			})
		} catch (err) {}
		console.log(dadosTurma)
	}, [])

	// url do autocadastro no localStorage para efetuar redirecionamento em caso de login
	const urlTurmaAutocadastro = `/cadlink/${id_turma}/${tokenTurma}`
	localStorage.setItem("urlAutoSignup", urlTurmaAutocadastro)

	const history = useHistory()

	const cancelarAutocadastro = () => {
		localStorage.removeItem("urlAutoSignup")
		history.push("/")
	}

	async function handleCreate(e) {
		e.preventDefault()

		const data = {
			tokenTurma,
			cpf,
		}

		if (dadosAluno.cpf == data.cpf) {
			try {
				const token = localStorage.getItem("token")
				const AuthStr = "Bearer ".concat(token)

				api.post("/autocadastro", data, { headers: { Authorization: AuthStr } })

				alert(`O aluno foi cadastrado na turma com sucesso!`)
				history.push("/autocadastroTurmaEfetuado")
			} catch (err) {
				console.log(err)
				alert("Erro no cadastro nessa turma, tente novamente")
			}
		} else {
			alert("CPF não consta em nosso banco de dados")
		}
	}

	return (
		<Fragment>
			<NavBar />
			<main className="main">
				<div class="main-content-forms">
					<div class="form-page-container cad-link">
						<div class="form-container">
							<form onSubmit={handleCreate}>
								<h1>Cadastre-se na turma!</h1>
								<p>
									Você está se cadastrando na turma{" "}
									<b>{dadosTurma.nome_do_curso}</b> com o professor(a){" "}
									<b>{dadosTurma.NomeDoPropositor}</b>.
								</p>
								<p>
									Para confirmar, por favor, preencha o campo abaixo com o seu
									CPF:
								</p>
                <br/>
								<input
									name="aluno"
									class="form-input"
									placeholder="CPF"
									value={cpf}
									onChange={(e) => setCPF(e.target.value)}
									required
								/>
								<input type="submit" class="button" value="cadastrar" />
                <div className="signup turma">
									Não deseja se cadastrar?
									<span className="form-highlight" onClick={cancelarAutocadastro}> Cancelar cadastro em turma</span>
								</div>
							</form>
						</div>
					</div>
				</div>
			</main>
		</Fragment>
	)
}

export default CadastroLink
