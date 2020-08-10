import React, { Fragment, useState, useEffect } from 'react'
import { Link } from "../../../../node_modules/react-router-dom"

// icons
import Create from "@material-ui/icons/Create"
import Class from "@material-ui/icons/Class"
import Done from "@material-ui/icons/Done"
import AccountCircle from "@material-ui/icons/AccountCircle"

// icons
import Checkmark from '../../../assets/img/IconeCheckmark.png'
import Lapis from '../../../assets/img/IconeLapis.png'
import Pessoa from '../../../assets/img/IconePessoa.png'
import Turmas from '../../../assets/img/IconeTurmas.png'

import api from "../../../services/api"
import { NavBar } from "../../navbar"

import "./perfil.css"

var QRCode = require('qrcode.react');

function Perfil() {
	const [dados, setDados] = useState([])

	//alterar rota.
	useEffect(() => {
		try {
            const token = localStorage.getItem("token")
            const AuthStr = 'Bearer '.concat(token); 
			api.get("/dadosPessoais", { headers: { Authorization: AuthStr }}).then((response) => {
                setDados(response.data)
			})
		} catch (err) {
			alert("Não foi possível encontrar o usuário desejada, tente novamente")
		}
	}, [])

	function createQR(dadosQR){
		for (var key in dadosQR){
			var attrName = key;
			if (attrName != "email" && attrName != "cpf") {
				delete dadosQR [ attrName ]
			}

		}

		dadosQR = JSON.stringify(dadosQR)
		
		let content = []
		content.push(
		
			<QRCode value={dadosQR} renderAs='svg' size='300' />
		
		)
		return content

	}
	


	return (
		<Fragment>
			<NavBar />
			<main className="main">
				<div className="profile__container">
					<div className="profile__container-info">
						<h1 className="bold">Olá, usuário!</h1>
						<p className="subtitle">
							Visualize suas informações pessoais nesta página.
						</p>
						<p className="subtitle-qr bold">Seu QR Code de acesso:</p>
						<div className="card">
							{createQR(dados)}
						</div>
						<div className="profile__container-buttons">
							<Link to="/editarDados">
								<button size="large" class="personal-buttons bold" disabled>
									<img src={Lapis} alt="Icone editar"></img>
									<label>Editar Dados</label>
								</button>
							</Link>
							<Link to="/dadosPessoais">
								<button size="large" class="personal-buttons bold">
								<img src={Pessoa} alt="Icone pessoa"></img>
									<label>Dados Pessoais</label>
								</button>
							</Link>
						</div>
					</div>
					<div className="profile__container-options">
						<Link to="/turmasinscritas" className="link">
							<button size="large" class="button bold" disabled>
							<img src={Turmas} alt="Icone turmas"></img>
								<label>Turmas Inscritas</label>
							</button>
						</Link>
						<Link to="/presencaspessoais" className="link">
							<button size="large" class="button bold" disabled>
							<img src={Checkmark} alt="Icone checkmarck"></img>
								<label>Presenças</label>
							</button>
						</Link>
					</div>
				</div>
			</main>
		</Fragment>
	)
}

export default Perfil

