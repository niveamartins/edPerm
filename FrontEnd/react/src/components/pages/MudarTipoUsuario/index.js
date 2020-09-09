import React, { Fragment } from "react"

import { NavBar } from "../../navbar"
import Button from "../../Button"



function Inicio() {

	const user_type = localStorage.getItem("user_type")

	let cadastrarAdmsButton = (
		<Button
			link="/cadAdm"
			title="Tornar Adm"
			description="Torne usuários administradores"
		/>
   )
   
   let cadastrarGestorButton = (
		<Button
			link="/cadGestor"
			title="Tornar Gestor"
			description="Torne usuários gestores"
		/>
   )

   let cadastrarCoordenadorButton = (
		<Button
			link="/cadCoordenador"
			title="Tornar Coordenador"
			description="Torne usuários coordenadores"
		/>
   )

   let cadastrarPropositorButton = (
		<Button
			link="/cadPropositor"
			title="Tornar Propositor"
			description="Torne usuários propositores"
		/>
   )

   let cadastrarCursistaButton = (
		<Button
			link="/cadCursista"
			title="Tornar Cursista"
			description="Torne usuários novamente cursistas"
		/>
   )

   
	if (user_type !== "adm") {
      cadastrarAdmsButton = null
   }
   
   if (user_type !== "adm" || user_type === "gestor") {
		cadastrarGestorButton = null
   }
   
   if (user_type !== "adm" || user_type === "coordenador" ) {
		cadastrarCoordenadorButton = null
   }
   
   if (user_type !== "adm" || user_type === "coordenador" || user_type === "gestor" ) {
      cadastrarPropositorButton = null
      cadastrarCursistaButton = null
	}

	return (
		<Fragment>
			<NavBar />
			<main className="main-inicio">
				<h1 bold>Mude os tipos dos usuários desejados</h1>
				<div className="button__link-container">
					{cadastrarAdmsButton}
               {cadastrarGestorButton}
               {cadastrarCoordenadorButton}
               {cadastrarPropositorButton}
               {cadastrarCursistaButton}
				</div>
			</main>
		</Fragment>
	)
}

export default Inicio
