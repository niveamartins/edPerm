import React, { Fragment, useState, useEffect } from "react"

import { NavBar } from "../../navbar"
import { Footer } from "../../footer"
import { Accessibility } from "../../accessibility"

import "./relatorio.css"

import api from "../../../services/api"

function Relatorio(props) {
	const [relatorio, setRelatorio] = useState([])

	const url = props.location.state

	useEffect(() => {
		try {
			const token = localStorage.getItem("token")
            const AuthStr = 'Bearer '.concat(token); 
			api.get(url, { headers: { Authorization: AuthStr }}).then((response) => {
				setRelatorio(response.data)
			})
		} catch (err) {
			alert("Não foi possível encontrar o relatório, tente novamente")
		}
	}, [])

	switch (props.location.state) {
		case "relatoriocontato":
			const getContatoContent = (contato) => {
				let content = []
				console.log(relatorio)
				for (let idx in contato) {
					const item = contato[idx]
					console.log(item)
					content.push(
						<table className="card-relatorio contato">
							<thead>
								<tr>
									<td className="topo__contato">
									<strong>{item.id}</strong>
									<span className="campo">{item.nome}</span>
									</td>
								</tr>
							</thead>
							<tbody>
								<tr>{item.email}</tr>
								<tr>{item.telefone}</tr>
							</tbody>
						</table>
					)

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
							<ul>{getContatoContent(relatorio)}</ul>
						</div>
					</main>
					<Footer />
				</Fragment>
			)

		case "relatoriocpfnome":
			const getAlunoContent = (alunos) => {
				let content = []
				for (let idx in alunos) {
					const item = alunos[idx]
					content.push(
						<tr className="info-alunos">
							<td>{item.nomeDoAluno}</td>
							<td className="cpf">{item.cpfDoAluno}</td>
						</tr>
					)
				}
				return content
			}

			const getCPFContent = (cpf) => {
				let content = []
				for (let idx in cpf) {
					const item = cpf[idx]
					console.log(item)
					content.push(
						<table className="card-relatorio cpf">
							<thead>
								<tr>
									<td className="campo">Turma: </td>
									<td>
										<strong>{item.id_turma}</strong>{" "}
										<span className="info">{item.nomeDoCurso}</span>
									</td>
								</tr>
								<tr>
									<td className="campo">Propositor: </td>
									<td>
										<strong>{item.idPropositor}</strong>{" "}
										<span className="info">{item.propositor}</span>
									</td>
								</tr>
							</thead>
							<tbody>
								<tr>
									<td className="campo">Alunos: </td>
								</tr>
								{getAlunoContent(item.alunos)}
							</tbody>
						</table>
					)

					// Dentro do push devemos colocar o html da parte de cada um dos cpfs
				}
				return content
			}

			return (
				<Fragment>
					<Accessibility />
					<NavBar />
					<main>
						<div className="card-container">
							<ul>{getCPFContent(relatorio)}</ul>
						</div>
					</main>
					<Footer />
				</Fragment>
			)

		case "relatoriofrequencia":
			const getFrequenciaContent = (frequencia) => {
				let content = []
				for (let idx in frequencia) {
					const item = frequencia[idx]
					content.push(
						<li className="card-relatorio frequencia">
							<div>
								<div>
									<p className="title">{item.Nome}</p>
									<p>{item.id_aluno}</p>
								</div>
								<p>{item.cpf}</p>
								<p>{item.id_user_aluno}</p>
								<p>
									{
										//Um item.Turma é uma lista, tem que percorrer
									}
								</p>
							</div>
						</li>
					)

					// Dentro do push devemos colocar o html da parte de cada um dos cpfs
				}
				return content
			}

			return (
				<Fragment>
					<Accessibility />
					<NavBar />
					<main className="main">
						<div className="container-relatorios">
							<ul>{getFrequenciaContent(relatorio)}</ul>
						</div>
					</main>
					<Footer />
				</Fragment>
			)

		case "profissao":
			const getProfissaoContent = (profissao) => {
				let content = []
				for (let idx in profissao) {
					const item = profissao[idx]
					content.push()

					// Dentro do push devemos colocar o html da parte de cada um dos cpfs
				}
				return content
			}

			return (
				<Fragment>
					<Accessibility />
					<NavBar />
					<main className="main">
						<div className="container-relatorios">
							<ul>{getProfissaoContent(relatorio)}</ul>
						</div>
					</main>
					<Footer />
				</Fragment>
			)

		case "CAP":
			const getCAPContent = (cap) => {
				let content = []
				for (let idx in cap) {
					const item = cap[idx]
					content.push()

					// Dentro do push devemos colocar o html da parte de cada um dos cpfs
				}
				return content
			}

			return (
				<Fragment>
					<Accessibility />
					<NavBar />
					<main className="main">
						<div className="container-relatorios">
							<ul>{getCAPContent(relatorio)}</ul>
						</div>
					</main>
					<Footer />
				</Fragment>
			)

		case "superintendencia":
			const getSIContent = (si) => {
				let content = []
				for (let idx in si) {
					const item = si[idx]
					content.push()

					// Dentro do push devemos colocar o html da parte de cada um dos cpfs
				}
				return content
			}

			return (
				<Fragment>
					<Accessibility />
					<NavBar />
					<main className="main">
						<div className="container-relatorios">
							<ul>{getSIContent(relatorio)}</ul>
						</div>
					</main>
					<Footer />
				</Fragment>
			)

		case "unidade":
			const getUnidadeContent = (unid) => {
				let content = []
				for (let idx in unid) {
					const item = unid[idx]
					content.push()

					// Dentro do push devemos colocar o html da parte de cada um dos cpfs
				}
				return content
			}

			return (
				<Fragment>
					<Accessibility />
					<NavBar />
					<main className="main">
						<div className="container-relatorios">
							<ul>{getUnidadeContent(relatorio)}</ul>
						</div>
					</main>
					<Footer />
				</Fragment>
			)

		case "relatorioconcluintes":
			const getCursistaContent = (cursistas) => {
				let content = []
				for (let idx in cursistas) {
					const item = cursistas[idx]
					console.log(item)
					content.push(
						<li>
							<p>{item.CAP}</p>
							<p>{item.aluno_nome}</p>
							<p>{item.funcao}</p>
							<p>{item.profissao}</p>
							<p>{item.unidade}</p>
							<p>{item.id_aluno}</p>
							<p>{item.id_user}</p>
							<p>{item.superintendenciadaSUBPAV}</p>
						</li>
					)
				}
				return content
			}

			const getConcluintesContent = (concluintes) => {
				let content = []
				for (let idx in concluintes) {
					const item = concluintes[idx]
					content.push(
						<li className="card-relatorio">
							<div>
								<p>{item.id_turma}</p>
								<p>{item.nome_do_curso}</p>
								<p>{item.id_do_responsavel}</p>
								<p>{item.nomeDoPropositor}</p>
								<p>{item.Carga_Horaria_Total}</p>
								<p>{getCursistaContent(item.cursistas)}</p>
							</div>
						</li>
					)

					// Dentro do push devemos colocar o html da parte de cada um dos cpfs
				}
				return content
			}

			return (
				<Fragment>
					<Accessibility />
					<NavBar />
					<main>
						<div className="card-container">
							<ul>{getConcluintesContent(relatorio)}</ul>
						</div>
					</main>
					<Footer />
				</Fragment>
			)
	}
}

export default Relatorio
