import React, { Fragment, useState } from 'react';

import './cadastroAlunos.css'

import api from '../../../services/api';

// import { Link } from './node_modules/react-router-dom';
import { NavBar } from '../../navbar'
import { Footer } from '../../footer'
import { Accessibility } from '../../accessibility'


function CadastrarAlunos() {

      const [usuario, setUsuario] = useState("");
      const [nome_do_curso, setTurma] = useState("");  
  
      async function handleCreate(e) {
                  
          e.preventDefault();
      
          const data = {
            usuario,
            nome_do_curso
  
          };
      
          try {
            const token = localStorage.getItem("token")
            const AuthStr = 'Bearer '.concat(token); 
            
            api.post("/cadastraraluno", data, { headers: { Authorization: AuthStr }});
      
            alert(`O aluno foi cadastrado na turma com sucesso!`);
  
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
        <div class="main-content-forms">
          <div class="form-page-container">
            <div class="form-container">
              <form onSubmit={handleCreate}>
                <h1>Cadastre seus alunos! </h1>
                <p>Cadastre seus alunos em sua turma.</p>
                <input name="aluno" class="form-input" placeholder="Nome do aluno" value={usuario} onChange={e => setUsuario(e.target.value)} required />
                <input name="codigo" class="form-input" placeholder="Código da Turma" value={nome_do_curso} onChange={e => setTurma(e.target.value)} required />
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