import React, { Fragment } from 'react';

import './cadastroAlunos.css'

// {useState}
// import api from '../../services/api';

// import { Link } from './node_modules/react-router-dom';
import { NavBar } from '../../navbar'
import { Footer } from '../../footer'
import { Accessibility } from '../../accessibility'


function CadastrarAlunos() {

  /*    const [name, setName] = useState("");
      const [turma, setTurma] = useState("");  
  
      async function handleCreate(e) {
                  
          e.preventDefault();
      
          const data = {
            name,
            turma
  
          };
      
          try {
            api.post("/", data);
      
            alert(`O aluno foi cadastrado com sucesso!`);
  
          } catch (err) {
            console.log(err);
            alert("Erro no cadastro, tente novamente");
          }
        }
        */

  // mudar quando for integrar:
  // <input placeholder="Nome do Aluno" value={name} onChange={e => setName(e.target.value)}></input>
  // onSubmit={handleCreate}
  // <input placeholder="Código da Turma" value={turma} onChange={e => setTurma(e.target.value)}></input>

  return (
    <Fragment>
      <Accessibility />
      <NavBar />
      <main className="main">
        <div class="main-content-forms">
          <div class="form-page-container">
            <div class="form-container">
              <form>
                <h1>Cadastre seus alunos! </h1>
                <p>Cadastre seus alunos em sua turma.</p>
                <input name="aluno" class="form-input" placeholder="Nome do aluno" required />
                <input name="codigo" class="form-input" placeholder="Código da Turma" required />
                <input type="submit" class="button" value="cadastrar aluno" />
              </form>
            </div>
          </div>
        </div>
      </main>
      <Footer />
    </Fragment>
  );
}

export default CadastrarAlunos;