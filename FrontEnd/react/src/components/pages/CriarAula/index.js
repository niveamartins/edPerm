import React, { Fragment, useState } from 'react'
// import AddIcon from '@material-ui/icons/Add';
import { Link } from '../../../../node_modules/react-router-dom';
import ArrowBackIcon from '@material-ui/icons/ArrowBack';

import './criarAula.css'

import { NavBar } from '../../navbar'
import { Footer } from '../../footer'
import { Accessibility } from '../../accessibility'



function CriarAula() {

    const [turma, setTurma] = useState("");  
    const [dia, setDia] = useState("");
    const [horaInicio, setInicio] = useState("");
    const [horaTermino, setTermino] = useState("");
    const [propositor, setPropositor] = useState("");

    async function handleCreate(e) {
                
        e.preventDefault();
    
        const data = {
          turma, 
          dia, 
          horaInicio,
          horaTermino,
          propositor

        };
    
        // try {
        //   api.post("/cadastrarhorario", data);
    
        //   alert(`A aula foi cadastrada com sucesso!`);

        // } catch (err) {
        //   console.log(err);
        //   alert("Erro no cadastro, tente novamente");
        // }
      }

    return (
        <Fragment>
            <Accessibility />
            <NavBar />
            <main className="main">
                <a href="/turma">
                    <ArrowBackIcon id="return-icon" />
                </a>
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
                            <tr className="content">
                                <td className="name">Dia</td>
                                <td className="value">Terça</td>
                            </tr>
                            <tr className="content">
                                <td className="name">Hora</td>
                                <td className="value">13:00</td>
                            </tr>
                            <tr className="content">
                                <td className="name">Carga horária total</td>
                                <td className="value">15min</td>
                            </tr>
                            <tr className="content">
                                <td className="name">Tolerância</td>
                                <td className="value">120h</td>
                            </tr>
                            <tr className="content">
                                <td className="name">Tolerância</td>
                                <td className="value">15min</td>
                            </tr>
                            <tr className="content">
                                <td className="name">Modalidade</td>
                                <td className="value">Esportes</td>
                            </tr>
                            <tr className="content">
                                <td className="name">Tag</td>
                                <td className="value">Atividade Física</td>
                            </tr>
                        </table>
                    </div>
                    <div className="info-turmas">
                        <div class="form-page-container">
                            <div class="form-container">
                                <form onSubmit={handleCreate}>
                                    <h1>Cadastre sua aula!</h1>
                                    <input type="date" name="data" class="form-input" placeholder="Data" required />
                                    <input name="turma" class="form-input" placeholder="Nome da Aula" required  />
                                    <input type="time" name="inicio" class="form-input" placeholder="Hora de Início" value={horaInicio} onChange={e => setInicio(e.target.value)} required />
                                    <input type="time" name="inicio" class="form-input" placeholder="Hora de Término" value={horaTermino} onChange={e => setTermino(e.target.value)} required />
                                    <input type="submit" class="button" value="cadastrar aula" />
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </main>
            <Footer />
        </Fragment>

    )
}

export default CriarAula
