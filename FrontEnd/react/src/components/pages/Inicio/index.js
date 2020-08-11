import React, { Fragment } from "react"

import { NavBar } from "../../navbar"
import Button from "../../Button"

import "./Inicio.css"

function Inicio() {
	let user_type = localStorage.getItem('user_type')

	function getButtonByType(){
		
		if (user_type == "cursista" || user_type == "apoiador"){
			return (
				<>
				<Button
						link="/opcoesTurmas"
						title="Turmas"
						description="Liste Turmas"
						/>
				</>
			)
		} else{
			return(
				<>
				<Button
						link="/opcoesTurmas"
						title="Turmas"
						description="Crie, Edite e Liste Turmas"
					/>


				</>
			)
		}
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
					{getButtonByType()}
					
					{ user_type === "adm" &&
					<Button
							link="/relatorios"
							title="Relatórios"
							description="Visualize os relatórios gerados"
						/>
					}
				</div>
			</main>
		</Fragment>
	)
}

export default Inicio
