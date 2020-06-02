import React, { Fragment, Component } from "react"
import HelpOutlineIcon from "@material-ui/icons/HelpOutline"

import "./accessibility.css"

export class Accessibility extends Component {
	constructor(props) {
		super(props)

		this.state = {
			helpVisible: false,
		}

		this.handleClick = this.handleClick.bind(this)
		this.handleOutsideClick = this.handleOutsideClick.bind(this)
	}

	handleClick() {
		if (!this.state.helpVisible) {
            //se visível adiciona eventListener
			document.addEventListener("click", this.handleOutsideClick, false)
		} else {
            //se não visível remove eventListener
			document.removeEventListener("click", this.handleOutsideClick, false)
		}

		this.setState((prevState) => ({
			helpVisible: !prevState.helpVisible,
		}))
	}

	handleOutsideClick(e) {
		// ignora clicks no popup (this.node === null para corrigir bug ao clicar link nav)
		if ( this.node === null || this.node.contains(e.target)) {
			return
		}

		this.handleClick()
	}

	render() {
		const { helpVisible } = this.state
		return (
			<Fragment>
				{helpVisible && (
					<div
						id="help"
						ref={(node) => {
							this.node = node
						}}
					>
						<div className="help__content">
							<ul>
								<li>(Mudar quando for a versão final)</li>
								<li>
									Acompanhe as turmas disponíveis na plataforma Educação
									Permanente!
								</li>
								<li>
									<span className="list__title">Gestores e Coordenadores:</span>
									<br />
									Abram novas turmas.
								</li>
								<li>
									<span className="list__title">Propositores:</span>
									<br />
									Organizem atividades de Educação Permanente! Definam
									carga-horária, emitam certificados, e mais.
								</li>
								<li>
									<span className="list__title">Alunos:</span>
									<br />
									Se inscrevam em turmas e recebam um QRCode por email para
									confirmar presença nos dias das aulas. E também se tornem
									instrutores de turmas já cursadas!
								</li>
								<li>
									<span className="list__title">Instrutores:</span>
									<br />
									Confirmem a presença de alunos em aulas.
								</li>
							</ul>
						</div>
					</div>
				)}
				<div className="accessibility">
					<div alt="Ajuda" title="Ajuda" onClick={this.handleClick}>
						<HelpOutlineIcon id="accessible-elements" />
					</div>
				</div>
			</Fragment>
		)
	}
}

export default Accessibility
