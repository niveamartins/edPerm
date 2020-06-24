import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
// npm install react-router-dom


// Aqui iremos importar todas as páginas
import CadastrarAlunos from './components/pages/CadastrarAlunos';
import CadastrarTurma from './components/pages/CadastrarTurmas';
import Login from './components/pages/Login'
import CadastroUsuario from './components/pages/CadastroUsuario'
import EsqueciASenha from './components/pages/EsqueciASenha'
import Inicio from './components/pages/Inicio'
import OpcoesTurmas from './components/pages/OpcoesTurmas'
import ListarTurmas from './components/pages/ListarTurmas'
import Turma from './components/pages/Turma'
import Presenca from './components/pages/Presenca'
import CriarAula from './components/pages/CriarAula'
import CadastrarApoiador from './components/pages/CadastrarApoiador'
import Aulas from './components/pages/Aulas'
import Aula from './components/pages/Aula'
import LerPresenca from './components/pages/LerPresenca'
import Perfil from './components/pages/Perfil'
import EditarCadastro from './components/pages/editarCadastro'
import DadosPessoais from './components/pages/dadosPessoais'
import Relatorios from './components/pages/Relatorios'
import Relatorio from './components/pages/Relatorio'

// Aqui definimos todas as rotas
export default function Routes() {
    return (
        <BrowserRouter>
            <Switch>
                <Route exact path="/" component={Inicio}/>
                <Route path="/login" component={Login} /> 
                <Route path="/cadalunos" component={CadastrarAlunos} />
                <Route path="/cadturma" component={CadastrarTurma} />
                <Route path="/cadusuario" component={CadastroUsuario} /> 
                <Route path="/esqueciasenha" component={EsqueciASenha} /> 
                <Route path="/opcoesTurmas" component={OpcoesTurmas} />
                <Route path="/turmas" component={ListarTurmas} /> 
                <Route path="/turma" component={Turma} />
                <Route path="/presenca" component={Presenca}/>
                <Route path="/cadaula" component={CriarAula}/>
                <Route path="/cadapoiador" component={CadastrarApoiador} />
                <Route path="/aulas" component= {Aulas} />
                <Route path="/aula" component={Aula} />
                <Route path="/leitor" component= {LerPresenca} />
                <Route path="/perfil" component={Perfil} />
                <Route path="/editarDados" component={EditarCadastro}/>
                <Route path="/dadosPessoais" component={DadosPessoais}/>
                <Route path="/relatorios" component={Relatorios}/>
                <Route path="/relatorio" component={Relatorio}/>
            </Switch>
        </BrowserRouter>
    );
}