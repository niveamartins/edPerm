import React, { Fragment, useState, useEffect } from 'react'
// import AddIcon from '@material-ui/icons/Add';
import { NavBar } from '../../navbar'

import api from "../../../services/api"

const QRCode = require('qrcode.react')

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
 
    function createQR(dadosQR){
        let a = {}
		for (var key in dadosQR){
			var attrName = key;
			if (attrName != "email" && attrName != "cpf") {
                continue
			}
            a[attrName] = dadosQR[attrName]
		}

		a = JSON.stringify(a)
		
		let content = []
		content.push(
		
			<QRCode value={a} renderAs='svg' size='300' />
		
		)
		return content

	}

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
                            {/* {<tr className="content">
                                <td className="name">Tipo</td>
                                <td className="value">{item.tipo}</td>
                            </tr>} */}
                        </tbody>
                    </table>
				
            )
        

		return content
	}

    return (
        <Fragment>
            <NavBar />
            <main className="main">
                <div className="card-container dados-pessoais">
                    <div className="card">
                        {createQR(dados)}
                    </div>
                    <div className="card">
                        {getDadosContent(dados)}
                    </div>    
                </div>
                
            </main>
        </Fragment>

    )
}

export default DadosPessoais
