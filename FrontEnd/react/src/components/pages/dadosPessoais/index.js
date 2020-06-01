import React, { Fragment } from 'react'
// import AddIcon from '@material-ui/icons/Add';
import { Link } from '../../../../node_modules/react-router-dom';

import { NavBar } from '../../navbar'
import { Footer } from '../../footer'
import { Accessibility } from '../../accessibility'


const qrcodeimg = require('../../../assets/qr-code-teste.png')


function DadosPessoais() {

    //preencher dados da turma com db

    return (
        <Fragment>
            <Accessibility />
            <NavBar />
            <main className="main">
                <div className="card-container">
                    <div className="card">
                        <img src={qrcodeimg}/>
                    </div>
                    <div className="card">
                        <table className="card-list">
                            <tr className="title">
                                <td>Usuário</td>
                            </tr>
                            <tr className="content">
                                <td>Nome Completo:</td>
                                <td><span className="tutor__highlight">Fulaninho</span></td>

                            </tr>
                            <tr className="content">
                                <td className="name">Data de Nascimento</td>
                                <td className="value">20/02/2000</td>
                            </tr>
                            
                        </table>
                    </div>    
                </div>
                
            </main>
            <Footer />
        </Fragment>

    )
}

export default DadosPessoais
