import React, { Fragment } from "react"
import { Link } from 'react-router-dom'

import { NavBar } from "../../navbar"
import Perfil from '../../../assets/img/IconePessoa.png'
import Turmas from '../../../assets/img/IconeTurmas.png'

import './autocadastroEfetuado.css'
import DoneIcon from "@material-ui/icons/Done"

function Inicio(props) {
	
	// cadastro concluído:  não precisa mais de redirecionamento
	localStorage.removeItem("urlAutoSignup")

	return (
		<Fragment>
			<NavBar />
			<main className="main">
				<div className="card-concluido auto-cad">
					<div className="card-concluido__header">
						<h3>Auto Cadastro efetuado com sucesso!</h3>
						<DoneIcon />
					</div>
					<h4 className="subtitle">Sua inscrição na turma foi efetuada!</h4>
					<h4>
						Para confirmar sua presença nas aulas apresente o QR Code que se encontra em sua página de perfil no momento de sua chegada
					</h4>
               <div className="profile__container-buttons auto-cad">
							<Link to="/perfil">
								<button size="large" class="personal-buttons bold">
									<img src={Perfil} alt="Icone pessoa"></img>
									<label>Ir para Perfil</label>
								</button>
							</Link>
                     <Link to="/">
								<button size="large" class="personal-buttons bold">
									<img src={Turmas} alt="Icone turma"></img>
									<label>Ir para turmas</label>
								</button>
							</Link>
						</div>
				</div>
			</main>
		</Fragment>
	)
}

export default Inicio
