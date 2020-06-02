import React, { Fragment } from "react"

import { NavBar } from "../../navbar"
import { Footer } from "../../footer"
import { Accessibility } from "../../accessibility"

function EditarCadastro() {
	//Integrar cadastro com js

	// mudar quando for integrar:
	// <input placeholder="Nome do Aluno" value={name} onChange={e => setName(e.target.value)}></input>
	// onSubmit={handleCreate}
    // <input placeholder="Código da Turma" value={turma} onChange={e => setTurma(e.target.value)}></input>

    const title = {
        fontSize: '1.7em',
        marginBottom: '1em'
    }

	return (
		<Fragment>
			<Accessibility />
			<NavBar />
			<main className="main">
				<main className="main-content-forms">
					<div className="form-page-container">
						<div className="form-container">
							<form>
								<h1 style={title}>Edite suas informações abaixo</h1>
								<input
									type="text"
									name="usuario"
									class="form-input"
									placeholder="Usuário"
									required
								/>
								<input
									type="text"
									name="email"
									class="form-input"
									placeholder="Email"
									required
								></input>
								<input
									type="password"
									name="senha"
									class="form-input"
									placeholder="Senha"
									required
								/>
								<input
									type="password"
									name="confirme_senha"
									id="confirm_password"
									class="form-input"
									placeholder="Confirme a Senha"
									required
								/>
								<input type="submit" class="button" value="Editar" />
							</form>
						</div>
					</div>
				</main>
			</main>
			<Footer />
		</Fragment>
	)
}

export default EditarCadastro
