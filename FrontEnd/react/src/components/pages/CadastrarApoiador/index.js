import React, { Fragment, useState } from 'react'
import { Link } from '../../../../node_modules/react-router-dom';
import ArrowBackIcon from '@material-ui/icons/ArrowBack';

import api from '../../../services/api';


import { NavBar } from '../../navbar'
import { Footer } from '../../footer'
import { Accessibility } from '../../accessibility'



function CadastrarApoiador(props) {

    const [aluno, setAluno] = useState("");

    let info = props.location.state;

    const turma = info[0].id_turma;

    async function handleCreate(e) {
                
        e.preventDefault();
    
        const data = {
          turma, 
          aluno

        };
        
        console.log(data)
        /*
        try {
          api.post("/cadastrarhorario", data);
    
          alert(`O aluno foi cadastrado como apoiador da turma com sucesso!`);

        } catch (err) {
          console.log(err);
          alert("Erro no cadastro, tente novamente");
        }
        */
      }


    return (
        <Fragment>
            <Accessibility />
            <NavBar />
            <main className="main">
                {/* <Link to="/turma">
                    <ArrowBackIcon id="return-icon" />
                </Link> */}
                <div className="card-container">
					<div className="card">
						<table className="card-list">
							<tr className="title">
								<td>{info[0].nome_do_curso}</td>
							</tr>
							<tr className="tutor">
								<td>Responsável:</td>
								<td>
									<span className="tutor__highlight">
										{info[0].NomeDoPropositor}
									</span>
								</td>
							</tr>
							<tr className="header">
								<th>Turma</th>
								<th>Informações</th>
							</tr>
							<tr className="content">
								<td className="name">Carga horária total</td>
								<td className="value">{info[0].carga_horaria_total}</td>
							</tr>
							<tr className="content">
								<td className="name">Tolerância</td>
								<td className="value">{info[0].tolerancia}</td>
							</tr>
							<tr className="content">
								<td className="name">Modalidade</td>
								<td className="value">{info[0].modalidade}</td>
							</tr>
							<tr className="content">
								<td className="name">Tag</td>
								<td className="value">{info[0].modalidade}</td>
							</tr>
						</table>
					</div>
			    </div>
                <div className="info-turmas">
                    <div class="form-page-container">
                        <div class="form-container">
                            <form onSubmit={handleCreate}>
                                <h1>Cadastre o apoiador!</h1>
                                <p>Insira abaixo o código do aluno escolhido.</p>
                                <input name="aluno" class="form-input" placeholder="Código do Aluno" value={aluno} onChange={e => setAluno(e.target.value)} required />
                                <input type="submit" class="button" value="cadastrar apoiador" />
                            </form>

                        </div>
                    </div>
                </div>
            </main>
            <Footer />
        </Fragment>

    )
}

export default CadastrarApoiador
