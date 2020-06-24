import React, { Fragment } from "react"

import { NavBar } from "../../navbar"
import { Footer } from "../../footer"
import { Accessibility } from "../../accessibility"
import Button from "../../Button"

import "./Inicio.css"

function Inicio() {
	return (
		<Fragment>
			<Accessibility />
			<NavBar />
			<main className="main-inicio">
				<h1>Bem vindo, usuário!</h1>
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
			<Footer />
		</Fragment>
	)
}

export default Inicio
