import React from 'react'
import PowerSettingsNewIcon from '@material-ui/icons/PowerSettingsNew'
import MenuIcon from '@material-ui/icons/Menu'

import './navbar.css'
import { NavLink } from 'react-router-dom'

export function NavBar() {
    //Links
    /* <li><a href="cadastroturma" class="middle" title="Cadastrar Turma">Cadastrar Turma</a></li>
        <li><a href="listaturma" class="middle" title="Listar Turmas">Listar Turmas</a></li>
        <li><a href="#areas" class="middle" title="Cadastrar Horário">Cadastrar Horário</a></li>
        <li><a href="cadastrodadoscomplementares" class="middle" title="Dados complementares">Mais Dados</a></li>
    
    */

    return (
        <div>
            <header>

                <div className="logo"><a href="/turmas">Educação Permanente</a></div>

                <nav className="myNav" id="myNav">

                        {/* button for nav sliding */}
                        <input type="checkbox" id="check" />
                        <label for="check" class="checkbtn">
                            <MenuIcon id="toggle-button" />
                        </label>

                        <ul className="nav__links">
                            <li><NavLink to="/cadalunos" className="middle" title="Cadastrar Alunos" activeClassName="active__link">Cadastrar Alunos</NavLink></li>
                            <li><NavLink to="/cadturma" className="middle" title="Cadastrar Turma" activeClassName="active__link">Cadastrar Turma</NavLink></li>
                            <li><NavLink to="/turmas" className="middle" title="Listar Turmas" activeClassName="active__link">Turmas</NavLink></li>
                            <li><NavLink to="/Perfil" className="middle" title="Perfil" activeClassName="active__link">Perfil</NavLink></li>
                        </ul>
                </nav>

                    {/* logout button */}
                    <a href="/" title="Sair"> <PowerSettingsNewIcon id="nav-elements" /> </a>

            </header>
        </div>
    );
}