import React, { Fragment } from "react"

import { NavBar } from "../../navbar"
import { HomeButton } from '../../HomeButton'
import Button from "../../Button"

const opcoesTurmas = () => {
	let criarTurmaButton = <Button link="/cadTurma" title="Criar Turma" description="Crie uma nova turma"/>

	const user_type = localStorage.getItem("user_type")
	if (user_type == "cursista" || user_type == "apoiador")
		criarTurmaButton = null

	return (
		<Fragment>
			<NavBar />
			<main className="main-inicio">
				<h1>Funções disponíveis para Turmas:</h1>
				<div className="button__link-container">
					{criarTurmaButton}
					<Button
						// link="turmasCriadas"
						link="turmas"
						title="Turmas"
						description="Liste todas as turmas"
					/>
					<Button
						link="turmasAluno"
						title="Turmas Aluno"
						description="Liste suas turmas como aluno"
					/>
					<Button
						link="turmasApoiador"
						title="Turmas Apoiador"
						description="Liste suas turmas como apoiador"
					/>
					<Button
						link="turmasPropositor"
						title="Turmas Propositor"
						description="Liste suas turmas como propositor"
					/>
				</div>
			</main>
		<HomeButton />
		</Fragment>
	)
}

export default opcoesTurmas
