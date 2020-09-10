import React, { Fragment } from "react"

import { NavBar } from "../../navbar"
import Button from "../../Button"

import "./Inicio.css"

function Inicio() {
	// para o caso de alguém voltar pro início sem cancelar auto cadastro
	localStorage.removeItem("urlAutoSignup")

	const adm = localStorage.getItem("adm")
	const gestor = localStorage.getItem("gestor")
	const coordenador = localStorage.getItem("coordenador")
	const propositor = localStorage.getItem("propositor")

	let turmasButton = (
		<Button
			link="/opcoesTurmas"
			title="Turmas"
			description="Crie e Liste Turmas"
		/>
	)
	let mudarTipoUsuarioButton = (
		<Button
			link="/mudarTipoUsuario"
			title="Mudar tipo de usuário"
			description="Mude tipo de usuários (adm, gestão, etc)"
		/>
	)
	let relatoriosButton = (
		<Button
			link="/relatorios"
			title="Relatórios"
			description="Visualize os relatórios gerados"
		/>
	)

	const allowedToChangeTurma =
		adm === "true" ||
		coordenador === "true" ||
		gestor === "true" ||
		propositor === "true"
		
	if (!allowedToChangeTurma) {
		turmasButton = (
			<Button link="/opcoesTurmas" title="Turmas" description="Liste Turmas" />
		)
	}

	const allowedToChangeUser =
		adm === "true" || coordenador === "true" || gestor === "true"
	if (!allowedToChangeUser) {
		mudarTipoUsuarioButton = null
	}

	if (adm === "false") {
		relatoriosButton = null
	}

	return (
		<Fragment>
			<NavBar />
			<main className="main-inicio">
				<h1 bold>Bem vindo, {localStorage.getItem("user_username")}!</h1>
				<div className="button__link-container">
					<Button
						link="/perfil"
						title="Perfil"
						description="Acesse seu perfil"
					/>
					{turmasButton}
					{relatoriosButton}
					{mudarTipoUsuarioButton}
				</div>
			</main>
		</Fragment>
	)
}

export default Inicio
