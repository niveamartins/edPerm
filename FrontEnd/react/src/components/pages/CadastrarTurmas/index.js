import React, { Fragment, useState } from 'react';

import './cadastroTurma.css'
import api from '../../../services/api';

// import { Link } from './node_modules/react-router-dom';
import { NavBar } from '../../navbar'
import { Footer } from '../../footer'
import { Accessibility } from '../../accessibility'


function CadastrarTurma() {

     const [name, setName] = useState("");
      const [turma, setTurma] = useState("");  
  
      async function handleCreate(e) {
                  
          e.preventDefault();
      
          const data = {
            name,
            turma
  
          };
      
          try {
            api.post("/cadastrarturma", data);
      
            alert(`A turma foi cadastrada com sucesso!`);
  
          } catch (err) {
            console.log(err);
            alert("Erro no cadastro, tente novamente");
          }
        }
  

  // mudar quando for integrar:
  // <input placeholder="Nome do Aluno" value={name} onChange={e => setName(e.target.value)}></input>
  // onSubmit={handleCreate}
  // <input placeholder="Código da Turma" value={turma} onChange={e => setTurma(e.target.value)}></input>

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
              <form>
                <input name="responsavel" class="form-input" placeholder="Responsável" required />
                <input name="nome" class="form-input" placeholder="Nome do Curso" required />
                {/* <div class="form-line"> */}
                  <input name="dia" class="form-input" placeholder="Dia" required />
                  <input name="hora" class="form-input-second" placeholder="Hora" required />
                {/* </div> */}
                {/* <div class="form-line"> */}
                  <input name="carga" class="form-input" placeholder="Carga Horária" required />
                  <input name="tolerancia" class="form-input-second" placeholder="Tolerância" required />
                {/* </div> */}
                <input name="modalidade" class="form-input" placeholder="Modalidade" required />
                <input name="tag" class="form-input" placeholder="Tag" required />
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