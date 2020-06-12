import React from 'react';
import logoPrefeitura from '../../assets/logo-prefeitura.jpg'
import logoSaude from '../../assets/logo-ministerio-da-saude.png'


export function Footer(){

    return (
        <footer>
            <div className="links">
                <a href="https://prefeitura.rio/" target="_blanck" class="logo">
                    <img src={logoPrefeitura} alt="Logo Prefeitura"/>
                </a>
                <a href="https://saude.gov.br/" target="_blanck" class="logo" >
                    <img src={logoSaude} alt="Logo Ministério da Saúde"/>
                </a>
            </div>
        </footer>
    )
}