import React from '../../../node_modules/react';


export function NavBar(){
    //Links
    /* <li><a href="cadastroturma" class="middle" title="Cadastrar Turma">Cadastrar Turma</a></li>
        <li><a href="listaturma" class="middle" title="Listar Turmas">Listar Turmas</a></li>
        <li><a href="#areas" class="middle" title="Cadastrar Horário">Cadastrar Horário</a></li>
        <li><a href="cadastrodadoscomplementares" class="middle" title="Dados complementares">Mais Dados</a></li>
    
    */
    return (
        <div>
            <header>
                <div class="logo"><a href="/">Educação Permanente</a></div>
        
                <nav class="myNav" id="myNav">

                    <ul class="nav__links">
                    <li><a href="/cadalunos" class="middle" title="Cadastrar Alunos">Cadastrar Alunos</a></li>
                    <li><a href="/cadturma" class="middle" title="Cadastrar Alunos">Cadastrar Turma</a></li>
                    </ul>

                </nav>
            </header>
        </div>
    );
}