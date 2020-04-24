import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
// npm install react-router-dom


// Aqui iremos importar todas as páginas
import CadastrarAlunos from './components/pages/CadastrarAlunos';
import CadastrarTurma from './components/pages/CadastrarTurmas';
import Inicio from './components/pages/Inicio'
import CadastroUsuario from './components/pages/CadastroUsuario'
import EsqueciASenha from './components/pages/EsqueciASenha'
import ListarTurmas from './components/pages/ListarTurmas'
import Turma from './components/pages/Turma'
import Presenca from './components/pages/Presenca'
import CriarAula from './components/pages/CriarAula'

// Aqui definimos todas as rotas
export default function Routes() {
    return (
        <BrowserRouter>
            <Switch>
                <Route exact path="/" component={Inicio} /> 
                <Route path="/cadalunos" component={CadastrarAlunos} />
                <Route path="/cadturma" component={CadastrarTurma} />
                <Route path="/cadusuario" component={CadastroUsuario} /> 
                <Route path="/esqueciasenha" component={EsqueciASenha} /> 
                <Route path="/turmas" component={ListarTurmas} /> 
                <Route path="/turma" component={Turma} />
                <Route path="/presenca" component={Presenca}/>
                <Route path="/cadaula" component={CriarAula}/>
            </Switch>
        </BrowserRouter>
    );
}