import React, { Component, useState } from "react"
//npm install --save react-qr-reader
import QrReader from "react-qr-reader"

import { NavBar } from "../../navbar"
import api from "../../../services/api"

import "./lerpresenca.css"

function LerPresenca(props) {
	const [dadosAluno, setAluno] = useState("")
	const [dadoHora, setHora] = useState("")

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

	const handlePresenca = (e) => {
		let data = {
			idTurma: props.match.params.id_turma,
			emailAluno: dadosAluno.email,
			Horas: dadoHora,
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
        <input
					name="carga"
					className="form-input"
					placeholder="Horas Obtidas"
					maxLength="3"
					type="number"
					value={dadoHora}
					onChange={(e) => setHora(e.target.value)}
					required
				/>
				<button onClick={handlePresenca} className="button">
					Confirmar
				</button>
        </div>
			</main>
		</div>
	)
}

export default LerPresenca
