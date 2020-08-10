import React, { Fragment } from "react"

import { NavBar } from "../../navbar"
import Button from "../../Button"

import "./Inicio.css"

function Inicio() {
	return (
		<Fragment>
			<NavBar />
			<main className="main-inicio">
				<h1 bold>Bem vindo, usuário!</h1>
				<div className="button__link-container">
					<Button
						link="/opcoesTurmas"
						title="Turmas"
						description="Crie, Edite e Liste Turmas"
					/>
					<Button
						link="/perfil"
						title="Perfil"
						description="Acesse seu perfil"
					/>
					<Button
						link="/relatorios"
						title="Relatórios"
						description="Visualize os relatórios gerados"
					/>
				</div>
			</main>
		</Fragment>
	)
}

export default Inicio
