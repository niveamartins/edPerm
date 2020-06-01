import React, { Fragment } from "react"

import { NavBar } from "../../navbar"
import { Footer } from "../../footer"
import { Accessibility } from "../../accessibility"

import "./relatorios.css"

import CardRelatorio from "./CardRelatorio"

const relatorios = () => {
	return (
		<Fragment>
			<Accessibility />
			<NavBar />
			<main>
				<div className="document__links">
					<a href="#relatorio">
						<CardRelatorio title="CPF/Nome" />
					</a>
					<a href="#relatorio">
						<CardRelatorio title="Contato" />
					</a>
					<a href="#relatorio">
						<CardRelatorio title="Função/Cargo" />
					</a>
					<a href="#relatorio">
						<CardRelatorio title="Profissão" />
					</a>
					<a href="#relatorio">
						<CardRelatorio title="Superintendência" />
					</a>
					<a href="#relatorio">
						<CardRelatorio title="CAP" />
					</a>
					<a href="#relatorio">
						<CardRelatorio title="Unidade" />
					</a>
					<a href="#relatorio">
						<CardRelatorio title="Frequência" />
					</a>
					<a href="#relatorio">
						<CardRelatorio title="Concluintes" />
					</a>
				</div>
			</main>
			<Footer />
		</Fragment>
	)
}

export default relatorios
