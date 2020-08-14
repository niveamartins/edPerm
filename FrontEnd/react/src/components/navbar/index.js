import React, { Component } from "react"
import { Link } from "react-router-dom"

import "./navbar.css"
import Acessibility from "../accessibility/index"

// icons
import LogoEduca from "../../assets/img/logo.png"
import LogoPrefeitura from '../../assets/img/LogoPref.png'
import Logout from '../../assets/img/IconePower.png'
export class NavBar extends Component {
	render() {
		let icons = (
			<div className="nav-icons-container">
				<Acessibility />
				<Link to="/login" title="Sair">
					<img src={Logout} alt="Ícone Logout" className="nav-icons"></img>
				</Link>
			</div>
		)

		let redirectLogoLink = "/"
		let barHiddenStatus = "shown"

		if (this.props.login) {
			icons = null
			redirectLogoLink = "/login"
			barHiddenStatus = "invisible"
		}
		return (
				<header>
					<div className="logo">
						<Link to={redirectLogoLink}>
							<img src={LogoEduca}></img>
						</Link>
					</div>
					<div className="header-content">
						<img src={LogoPrefeitura} alt="Logo Prefeitura Rio" className={`nav-logo bar-${barHiddenStatus}`} />
						<div id="separate-icons" className={`bar-${barHiddenStatus}`}></div>
						{icons}
					</div>
				</header>
		)
	}
}

export default NavBar