import React, { Fragment } from "react"

import { NavBar } from "../../navbar"
import Button from "../../Button"

import "./Inicio.css"

function Inicio() {
	// para o caso de alguém voltar pro início sem cancelar auto cadastro
	localStorage.removeItem("urlAutoSignup")

	const user_type = localStorage.getItem("user_type")

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

	if (user_type === "cursista" || user_type === "apoiador") {
		turmasButton = (
			<Button link="/opcoesTurmas" title="Turmas" description="Liste Turmas" />
		)
	}
	
	
	if (user_type === "cursita" || user_type === "propositor") {
		mudarTipoUsuarioButton = null
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
