import React, { Fragment } from "react"

import { NavBar } from "../../navbar"
import { Footer } from "../../footer"
import { Accessibility } from "../../accessibility"
import CardRelatorio from "./CardRelatorio"

import ArrowBackIcon from '@material-ui/icons/ArrowBack';

import "./relatorios.css"

const relatorios = () => {
	return (
		<Fragment>
			<Accessibility />
			<NavBar />
			<main>
				<a href="/turma">
					<ArrowBackIcon id="return-icon" />
				</a>
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
