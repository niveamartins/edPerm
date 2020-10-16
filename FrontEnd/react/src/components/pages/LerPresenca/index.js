import React, { Component, useState, useEffect } from "react"
//npm install --save react-qr-reader
import QrReader from "react-qr-reader"

import { withStyles } from "@material-ui/core/styles"
import InputLabel from "@material-ui/core/InputLabel"
import FormControl from "@material-ui/core/FormControl"
import NativeSelect from "@material-ui/core/NativeSelect"
import InputBase from "@material-ui/core/InputBase"

import { NavBar } from "../../navbar"
import { HomeButton } from "../../HomeButton"

import api from "../../../services/api"

import "./lerpresenca.css"

function LerPresenca(props) {
	const [dadosAluno, setAluno] = useState("")
	const [id_aula, setIdAula] = useState("")

	const [aulas, setAulas] = useState("")

	let info = props.location.state
	let nome_do_curso = null
	if (info) {
		nome_do_curso = info[0].nome_do_curso
	}

	// carregando aulas para essa turma
	useEffect(() => {
		const data = {
			nome_do_curso,
		}
		try {
			const token = localStorage.getItem("token")
			const AuthStr = "Bearer ".concat(token)
			api
				.post("/listaraulasparapresenca", data, {
					headers: { Authorization: AuthStr },
				})
				.then((response) => {
					setAulas(response.data)
					// valor inicial caso usuário não mude a aula
					setIdAula(response.data[0].id_aula)
				})
		} catch (err) {
			alert("Não foi possível encontrar as turmas, tente novamente")
		}
	}, [])

	const handleScan = (data) => {
		if (data) {
			data = JSON.parse(data)
			setAluno(data)
			alert("O QR Code foi lido!")
		}
	}

	const handleError = (err) => {
		console.error(err)
	}

	// enviando dados presença
	const handlePresenca = (e) => {
		let data = {
			emailAluno: dadosAluno.email,
			id_aula: props.match.params.id_turma,
		}

		try {
			const token = localStorage.getItem("token")
			const AuthStr = "Bearer ".concat(token)
			api
				.post("/marcarpresenca", data, { headers: { Authorization: AuthStr } })
				.then((response) => {
					alert("Presença marcada com sucesso")
				})

			// alert(`A turma foi cadastrada com sucesso!`)
		} catch (err) {
			console.log(err)
			alert("Erro na marcação de presença, tente novamente")
		}
	}

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

	function getDadosQR(dadosQR) {
		let content = []
		content.push(
			<div className="card qr-reader">
				<table className="card-list">
					<tr className="content">
						<td className="name">CPF: </td>
						<td className="value">{dadosQR.cpf}</td>
					</tr>
					<tr className="content">
						<td className="name">E-mail: </td>
						<td className="value">{dadosQR.email}</td>
					</tr>
				</table>
			</div>
		)
		return content
	}

	const formAulas = aulas ? (
		<FormControl>
			<InputLabel htmlFor="demo-customized-select-native">Aula</InputLabel>
			<NativeSelect
				id="demo-customized-select-native"
				value={id_aula}
				onChange={(e) => setIdAula(e.target.value)}
				input={<BootstrapInput />}
				required
			>
				{aulas.map((option) => {
					return (
						<option value={option.id_aula} key={option.id_aula}>
							{option.nome_da_aula}
						</option>
					)
				})}
			</NativeSelect>
		</FormControl>
	) : (
		<p>Não há aulas cadastradas</p>
	)

	return (
		<div>
			<NavBar />
			<main className="qr-reader">
				<h2 className="qr-reader__title">Leitor de QrCode</h2>
				<div className="qr-reader__element">
					<QrReader
						delay={300}
						onError={handleError}
						onScan={handleScan}
						facingMode="enviroment"
						style={{ height: "90%" }}
					/>
				</div>
				<div>{getDadosQR(dadosAluno)}</div>

				<div className="qr-reader__card">
					{formAulas}
					<button onClick={handlePresenca} className="button">
						Confirmar
					</button>
				</div>
			</main>
			<HomeButton />
		</div>
	)
}

export default LerPresenca
