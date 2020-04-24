import React, { Fragment } from 'react'
import HelpOutlineIcon from '@material-ui/icons/HelpOutline';

import './accessibility.css'



export function Accessibility() {
    
    //colocar opção de fechar ao clicar em qualquer local na tela
    function showHelp() {
        let elem = document.getElementById("help");
        if (elem.style.display === "none") {
            elem.style.display = "block";
        } else {
            elem.style.display = "none";
        }
    }

    return (
        <Fragment>
            <div id="help">
                <div className="help__content">
                    <ul>
                        {/* Mudar conforme a versão final do projeto, pra listar tudo o que ele faz */}
                        <li>(Mudar quando for a versão final)</li>
                        <li>Acompanhe as turmas disponíveis na plataforma Educação Permanente!</li>
                        <li><span className="list__title"> Gestores e Coordenadores:</span><br/>Abram novas turmas.</li>
                        <li><span className="list__title">Propositores:</span><br/>Organizem atividades de Educação Permanente! Definam carga-horária, emitam certificados, e mais.</li>
                        <li><span className="list__title">Alunos:</span><br/>Se inscrevam em turmas e recebam um QRCode por email para confirmar presença nos dias das aulas. E também se tornem instrutores de turmas já cursadas!</li>
                        <li><span className="list__title">Instrutores:</span><br/>Confirmem a presença de alunos em aulas.</li>
                    </ul>
                </div>
            </div>
            <div className="accessibility">
                <div alt="Ajuda" title="Ajuda" onClick={showHelp}>
                    <HelpOutlineIcon id="accessible-elements" />
                </div>
            </div>
        </Fragment>
    )
}