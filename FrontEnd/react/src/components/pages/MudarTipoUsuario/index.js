import React, { Fragment } from "react"
import { Redirect } from 'react-router-dom'

import { NavBar } from "../../navbar"
import Button from "../../Button"


function Inicio() {

	const adm = localStorage.getItem("adm")
	const gestor = localStorage.getItem("gestor")
	const coordenador = localStorage.getItem("coordenador")

	let cadastrarAdmsButton = null
	let cadastrarGestorButton = null
	let cadastrarCoordenadorButton = null
	let cadastrarPropositorButton = null

	let redirectIfNotAuth = null

	const allowedToChangeUser =
		adm === "true" || coordenador === "true" || gestor === "true"
	if (!allowedToChangeUser) {
		redirectIfNotAuth = <Redirect to="/"/>
	}

	if (adm === "true") {
		cadastrarAdmsButton = (
			<Button
				link="/cadAdm"
				title="Tornar Adm"
				description="Torne usuários administradores"
			/>
		)
	}
	const allowedToChangeGestor = (adm === "true") || ("gestor" === "true")
	if (allowedToChangeGestor) {
		cadastrarGestorButton = (
			<Button
				link="/cadGestor"
				title="Tornar Gestor"
				description="Torne usuários gestores"
			/>
		)
	}

	const allowedToChangeCoordenador = (adm === "true") || (coordenador === "true")
	if (allowedToChangeCoordenador) {
		cadastrarCoordenadorButton = (
			<Button
				link="/cadCoordenador"
				title="Tornar Coordenador"
				description="Torne usuários coordenadores"
			/>
		)
	}

	if (allowedToChangeUser) {
		cadastrarPropositorButton = (
			<Button
				link="/cadPropositor"
				title="Tornar Propositor"
				description="Torne usuários propositores"
			/>
		)
	}

	return (
		<Fragment>
			{redirectIfNotAuth}
			<NavBar />
			<main className="main-inicio">
				<h1 bold>Mude os tipos dos usuários desejados</h1>
				<div className="button__link-container">
					{cadastrarAdmsButton}
               {cadastrarGestorButton}
               {cadastrarCoordenadorButton}
               {cadastrarPropositorButton}
				</div>
			</main>
		</Fragment>
	)
}

export default Inicio
