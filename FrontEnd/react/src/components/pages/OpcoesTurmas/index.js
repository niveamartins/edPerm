import React, { Fragment } from 'react'

import { NavBar } from "../../navbar"
import Button from "../../Button"

const opcoesTurmas = () => (
   <Fragment>
			<NavBar />
			<main className="main-inicio">
				<h1>Funções disponíveis para Turmas:</h1>
				<div className="button__link-container">
					<Button
						link="/cadTurma"
						title="Criar Turma"
					/>
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
					<Button
						link="/turmasApoiador"
						title="Listar turmas apoiador"
					/>
				</div>
			</main>
		</Fragment>
)

export default opcoesTurmas