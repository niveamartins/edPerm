import React, { Fragment, useState, useEffect } from 'react'
// import AddIcon from '@material-ui/icons/Add';
import { NavBar } from '../../navbar'
import { Footer } from '../../footer'
import { Accessibility } from '../../accessibility'

import api from "../../../services/api"

const qrcodeimg = require('../../../assets/qr-code-teste.png')

function DadosPessoais() {
    const [dados, setDados] = useState([])

	useEffect(() => {
		try {
            const token = localStorage.getItem("token")
            const AuthStr = 'Bearer '.concat(token); 
			api.get("/dadosPessoais", { headers: { Authorization: AuthStr }}).then((response) => {
                setDados(response.data)
			})
		} catch (err) {
			alert("Não foi possível encontrar o usuário desejada, tente novamente")
		}
    }, [])
    

    const getDadosContent = (dado) => {
		let content = []
	
		const item = dado
		content.push(
                <table className="card-list">
                        <tbody>
                            <tr className="title">
                                <td>Usuário</td>
                            </tr>
                            <tr className="content">
                                <td>Nome de Usuário</td>
                                <td><span className="tutor__highlight">{item.usuario}</span></td>

                            </tr>
                            <tr className="content">
                                <td className="name">CPF</td>
                                <td className="value">{item.cpf}</td>
                            </tr>
                            <tr className="content">
                                <td className="name">E-mail</td>
                                <td className="value">{item.email}</td>
                            </tr>
                            <tr className="content">
                                <td className="name">Telefone</td>
                                <td className="value">{item.telefone}</td>
                            </tr>
                            <tr className="content">
                                <td className="name">Tipo</td>
                                <td className="value">{item.tipo}</td>
                            </tr>
                        </tbody>
                    </table>
				
            )
        

		return content
	}

    return (
        <Fragment>
            <Accessibility />
            <NavBar />
            <main className="main">
                <div className="card-container dados-pessoais">
                    <div className="card">
                        <img src={qrcodeimg}/>
                    </div>
                    <div className="card">
                        {getDadosContent(dados)}
                    </div>    
                </div>
                
            </main>
            <Footer />
        </Fragment>

    )
}

export default DadosPessoais
