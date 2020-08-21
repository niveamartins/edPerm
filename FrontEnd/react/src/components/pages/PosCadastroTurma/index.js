import React, { Fragment } from "react"

import { NavBar } from "../../navbar"

import "./posCadastroTurma.css"
import FileCopyIcon from '@material-ui/icons/FileCopy';
import DoneIcon from '@material-ui/icons/Done';

function Inicio(props) {
  let DadosLink = props.location.state.detail
	function copiarTexto() {
		const linkTurma = document.getElementById("link-turma")

		//seleciona o texto
		linkTurma.select()
		linkTurma.setSelectionRange(0, 99999) //para mobile

		//copia o texto
		document.execCommand("copy")

		//msg exibida acima do button
		const tooltip = document.getElementById("myTooltip")
		tooltip.innerHTML = "Link copiado!"
	}

	//quando mouse sai do botão tooltip reseta para o texto "copie para..."
	function outFunc() {
		const tooltip = document.getElementById("myTooltip")
		tooltip.innerHTML = "Copie para a área de transferência"
	}

	window.addEventListener("load", () => {
		document.querySelector(".card-concluido").classList.add("loaded")
	})
  let link = window.location.hostname + "/cadlink/"+DadosLink.link_id_turma+'/'+DadosLink.token
	return (
		<Fragment>
			<NavBar />
			<main className="main">
				<div className="card-concluido">
					<div className="card-concluido__header">
						<h3>Turma cadastrada com sucesso!</h3>
                  <DoneIcon />
					</div>
					<p>Utilize o link abaixo para que alunos se inscrevam na turma:</p>
					<br/>
					<div className="card-concluido__link">
						<input type="text" id="link-turma" value={link} readOnly/>
						<div className="tooltip">
							<button onClick={copiarTexto} onMouseOut={outFunc}>
								<span class="tooltiptext" id="myTooltip">
									Copie para a área de transferência
								</span>
								copiar link
                        <FileCopyIcon className="copy-icon"/>
							</button>
						</div>
					</div>
				</div>
			</main>
		</Fragment>
	)
}

export default Inicio
