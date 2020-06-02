import React, { Fragment, useState } from 'react';

import './cadastroTurma.css'
import api from '../../../services/api';

// import { Link } from './node_modules/react-router-dom';
import { NavBar } from '../../navbar'
import { Footer } from '../../footer'
import { Accessibility } from '../../accessibility'


function CadastrarTurma() {

    const [responsavel, setResponsavel] = useState("");
    const [turma, setTurma] = useState("");  
    const [carga_horaria, setCarga] = useState("");
    const [tolerancia, setTolerancia] = useState("");
    const [modalidade, setModalidade] = useState("");
    const [tag, setTag] = useState("");
  
      async function handleCreate(e) {
                  
          e.preventDefault();
      
          const data = {
            responsavel,
            turma,
            carga_horaria,
            tolerancia,
            modalidade,
            tag
  
          };
      
          try {
            api.post("/cadastrarturma", data);
      
            alert(`A turma foi cadastrada com sucesso!`);
  
          } catch (err) {
            console.log(err);
            alert("Erro no cadastro, tente novamente");
          }
        }
        
  return (
    <Fragment>
      <Accessibility />
      <NavBar />
      <main className="main">
        <main className="main-content-forms">
          <div class="form-page-container">
            <div class="form-container">
              <h1>Cadastre sua turma!</h1>
              <p>Cadastre aqui sua turma Educação Permanente.</p>
              <form onSubmit={handleCreate}>
                <input name="nome" class="form-input" placeholder="Nome do Curso" value={turma} onChange={e => setTurma(e.target.value)} required />
                {/* <div class="form-line"> */}
                {/* </div> */}
                {/* <div class="form-line"> */}
                  <input name="carga" class="form-input" placeholder="Carga Horária" required />
                  <input name="tolerancia" class="form-input-second" placeholder="Tolerância" required />
                {/* </div> */}
                <input name="modalidade" class="form-input" placeholder="Modalidade" value={modalidade} onChange={e => setModalidade(e.target.value)} required />
                <input name="tag" class="form-input" placeholder="Tag" value={tag} onChange={e => setTag(e.target.value)} required />
                <input type="submit" className="button" id="cad__class-button" value="cadastrar Turma" />
              </form>
            </div>
          </div>
        </main>
      </main>
      <Footer />
    </Fragment>
  );
}

export default CadastrarTurma;