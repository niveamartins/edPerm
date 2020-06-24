import React, { Fragment } from 'react'

import { NavBar } from "../../navbar"
import { Footer } from "../../footer"
import { Accessibility } from "../../accessibility"
import Button from "../../Button"

const opcoesTurmas = () => (
   <Fragment>
			<Accessibility />
			<NavBar />
			<main className="main-inicio">
				<h1>Funções disponíveis para Turmas:</h1>
				<div className="button__link-container">
					<Button
						link="/cadTurma"
						title="Criar Turma"
					/>
					<Button
						link="/turmas"
						title="Listar Turmas Inscritas"
					/>
					<Button
						link="/turmas"
						title="Listar turmas apoiador"
					/>
               <Button
						link="/turmas"
						title="Editar turmas"
					/>
				</div>
			</main>
			<Footer />
		</Fragment>
)

export default opcoesTurmas