import React from '../../../node_modules/react';


export function Footer(){

    return (
        <div>
            <div className="links">
                <a href="https://prefeitura.rio/" target="_blanck" class="logo">
                    <img src="../../assets/logo-prefeitura.jpg" alt="Logo Prefeitura"/>
                </a>
                <a href="https://saude.gov.br/" target="_blanck" class="logo" >
                    <img src="../../assets/logo-ministerio-da-saude.png" alt="Logo Ministério da Saúde"/>
                </a>
            </div>
        </div>
    );
}