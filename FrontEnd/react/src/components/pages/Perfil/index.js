import React, { Fragment } from "react"
import { Link } from "../../../../node_modules/react-router-dom"

// icons
import Create from "@material-ui/icons/Create"
import Class from "@material-ui/icons/Class"
import Done from "@material-ui/icons/Done"
import AccountCircle from "@material-ui/icons/AccountCircle"

import { NavBar } from "../../navbar"
import { Footer } from "../../footer"
import { Accessibility } from "../../accessibility"

import "./perfil.css"

const qrcodeimg = require("../../../assets/qr-code-teste.png")

function Perfil() {
	//preencher dados da turma com db

	return (
		<Fragment>
			<Accessibility />
			<NavBar />
			<main className="main">
				<div className="profile__container">
					<div className="profile__container-info">
						<h1>Olá, usuário!</h1>
						<p className="subtitle">
							Visualize suas informações pessoais nesta página!
						</p>
						<p className="subtitle-qr">Seu QR Code de acesso</p>
						<div className="card">
							<img src={qrcodeimg} alt="QRCode de acesso" />
						</div>
						<div className="profile__container-buttons">
							<Link to="/editarDados">
								<button size="large" class="personal-buttons" disabled>
									<Create id="icons"></Create>
									<label>Editar Dados</label>
								</button>
							</Link>
							<Link to="/dadosPessoais">
								<button size="large" class="personal-buttons" disabled>
									<AccountCircle id="icons"></AccountCircle>
									<label>Dados Pessoais</label>
								</button>
							</Link>
						</div>
					</div>
					<div className="profile__container-options">
						<Link to="/turmasinscritas" className="link">
							<button size="large" class="button" disabled>
								<Class id="icons"></Class>
								<label>Turmas Inscritas</label>
							</button>
						</Link>
						<Link to="/presencaspessoais" className="link">
							<button size="large" class="button" disabled>
								<Done id="icons"></Done>
								<label>Presenças</label>
							</button>
						</Link>
					</div>
				</div>
			</main>
			<Footer />
		</Fragment>
	)
}

export default Perfil

