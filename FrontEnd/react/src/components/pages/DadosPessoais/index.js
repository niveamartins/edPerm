import React, { Fragment, useState, useEffect } from "react"
// import AddIcon from '@material-ui/icons/Add';
import { NavBar } from "../../navbar"
import { HomeButton } from '../../HomeButton'

import api from "../../../services/api"

import Download from '../../../assets/img/IconeDownload.png'
import "./dadosPessoais.css"

const QRCode = require("qrcode.react")

function DadosPessoais() {
	const [dados, setDados] = useState([])

	useEffect(() => {
		try {
			const token = localStorage.getItem("token")
			const AuthStr = "Bearer ".concat(token)
			api
				.get("/dadosPessoais", { headers: { Authorization: AuthStr } })
				.then((response) => {
					console.log(response.data)
					setDados(response.data)
				})
		} catch (err) {
			alert("Não foi possível encontrar o usuário desejada, tente novamente")
		}
	}, [])

	function createQR(dadosQR) {
		let a = {}
		for (var key in dadosQR) {
			var attrName = key
			if (attrName != "email" && attrName != "cpf") {
				continue
			}
			a[attrName] = dadosQR[attrName]
		}

		a = JSON.stringify(a)
		const sizeQR = 300

		let content = []
		content.push(
			<div className="QR-container">
				<QRCode
					value={a}
					size={sizeQR}
					id="qr-code"
					value="qr-code"
				/>
				<a className="download-QR__button" onClick={downloadQR}>
				<img src={Download} alt="Icone download" className="download-icon"></img>Faça download do QR Code
				</a>
			</div>
		)
		return content
	}

	const downloadQR = () => {
        const canvas = document.getElementById("qr-code")
		const pngUrl = canvas
			.toDataURL("image/png")
			.replace("image/png", "image/octet-stream")
		let downloadLink = document.createElement("a")
		downloadLink.href = pngUrl
		downloadLink.download = "qrcodeEducaSEGS.png"
		document.body.appendChild(downloadLink)
		downloadLink.click()
		document.body.removeChild(downloadLink)
	}

	const getDadosContent = (dado) => {
		let content = []

		const item = dado
		content.push(
			<table className="card-list">
				<tbody>
					<tr className="title">
						<td>{item.nome}</td>
					</tr>
					<tr className="content">
						<td>Nome de Usuário</td>
						<td>
							<span className="tutor__highlight">{item.usuario}</span>
						</td>
					</tr>
					<tr className="content">
						<td className="name">CPF</td>
						<td className="value">{item.cpf}</td>
					</tr>
					<tr className="content">
						<td className="name">E-mail</td>
						<td className="value">{item.email}</td>
					</tr>
					<tr className="content">
						<td className="name">Telefone</td>
						<td className="value">{item.telefone}</td>
					</tr>
					<tr className="content">
						<td className="name">Função</td>
						<td className="value">{item.funcao}</td>
					</tr>
					<tr className="content">
						<td className="name">Profissão</td>
						<td className="value">{item.profissao}</td>
					</tr>
					<tr className="content">
						<td className="name">CAP</td>
						<td className="value">{item.CAP}</td>
					</tr>
					<tr className="content">
						<td className="name">Unidade</td>
						<td className="value">{item.UnidadeBasicadeSaude}</td>
					</tr>
				</tbody>
			</table>
		)

		return content
	}

	return (
		<Fragment>
			<NavBar />
			<main className="main">
				<div className="card-container dados-pessoais">
					<div className="card">{createQR(dados)}</div>
					<div className="card dados-pessoais">{getDadosContent(dados)}</div>
				</div>
			</main>
			<HomeButton />
		</Fragment>
	)
}

export default DadosPessoais
