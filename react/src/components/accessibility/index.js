import React, { Fragment } from 'react'
import HelpOutlineIcon from '@material-ui/icons/HelpOutline';

import './accessibility.css'

export function Accessibility() {

    //colocar opção de fechar ao clicar em qualquer local na tela
//     function showHelp() {
//     let elem = document.getElementById("help");
//     if (elem.style.display === "none") {
//         elem.style.display = "block";
//     } else {
//         elem.style.display = "none";
//     }
// }

    return (
    <Fragment>
        <div className="accessibility">
            <div alt="Ajuda" title="Ajuda" onclick="showHelp()"> 
                <HelpOutlineIcon id="accessible-elements" />
            </div>
        </div>
    </Fragment>
    )
}