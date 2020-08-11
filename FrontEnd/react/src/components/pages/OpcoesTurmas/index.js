import React, { Fragment } from "react"

import { NavBar } from "../../navbar"
import Button from "../../Button"

const opcoesTurmas = () => {
	let criarTurmaButton = <Button link="/cadTurma" title="Criar Turma" />
	
	const user_type = localStorage.getItem("user_type")
	if (user_type == "cursista" || user_type == "apoiador") criarTurmaButton = null

	return (
		<Fragment>
			<NavBar />
			<main className="main-inicio">
				<h1>Funções disponíveis para Turmas:</h1>
				<div className="button__link-container">
					{criarTurmaButton}
					<Button
						// link="/turmasCriadas"
						link="turmas"
						title="Listar Turmas Criadas"
					/>
					<Button
						// link="/turmasInscritas"
						link="turmas"
						title="Listar Turmas Inscritas"
					/>
					<Button link="/turmasApoiador" title="Listar turmas apoiador" />
				</div>
			</main>
		</Fragment>
	)
}

export default opcoesTurmas
