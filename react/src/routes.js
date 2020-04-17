import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
// npm install react-router-dom


// Aqui iremos importar todas as páginas
import CadastrarAlunos from './components/pages/CadastrarAlunos';
import CadastrarTurma from './components/pages/CadastrarTurmas';

// Aqui definimos todas as rotas
export default function Routes() {
    return (
        <BrowserRouter>
            <Switch>
                <Route path="/cadalunos" component={CadastrarAlunos} />
                <Route path="/cadturma" component={CadastrarTurma} />
            </Switch>
        </BrowserRouter>
    );
}