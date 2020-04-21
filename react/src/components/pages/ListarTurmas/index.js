import React from '../../../../node_modules/react';

import './cadastroAlunos.css'

// import { Link } from './node_modules/react-router-dom';
import { NavBar } from '../../navbar'
import { Footer } from '../../footer'


function ListarTurmas() {

    //fazer navegação para pág da turma e preencher dados da turma com db

  return (
        <div className="cadastroAlunos">
            <NavBar></NavBar>
            <main className="main">
                <div className="card-container">
                    <div className="card">
                        <table className="card-list">
                            <tr className="title">
                                <td>Natação</td>
                            </tr>
                            <tr className="tutor">
                                <td>Responsável:</td>
                                <td><span className="tutor__highlight">Fulaninho</span></td>
                            </tr>
                            <tr className="header">
                                <th>Turma</th>
                                <th>Informações</th>
                            </tr>
                            <tr>
                                <td className="name">Dia</td>
                                <td className="value">Terça</td>
                            </tr>
                            <tr>
                                <td className="name">Hora</td>
                                <td className="value">13:00</td>
                            </tr>
                            <tr>
                                <td className="name">Carga Horária Total</td>
                                <td className="value">120h</td>
                            </tr>
                            <tr>
                                <td className="name">Tolerância</td>
                                <td className="value">15min</td>
                            </tr>
                            <tr>
                                <td className="name">Modalidade</td>
                                <td className="value">Esportes</td>
                            </tr>
                            <tr>
                                <td className="name">Tag</td>
                                <td className="value">Atividade Física</td>
                            </tr>
                            <tr>
                                <a href="#" className="class-page" title="Página da Turma">
                                    <i className="material-icons">add</i>info.
                                </a>
                            </tr>
                        </table>
                    </div>
                </div>
            </main>
            <Footer></Footer>
        </div>
  )
}

export default ListarTurmas