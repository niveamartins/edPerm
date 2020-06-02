import React, { Fragment, useState, useEffect } from 'react'


import { NavBar } from '../../navbar'
import { Footer } from '../../footer'
import { Accessibility } from '../../accessibility'

import api from '../../../services/api'

function Relatorio(props) { 
    const [relatorio, setRelatorio] = useState([]); 
    
    const url = props.location.state;

    useEffect(() => {
      try {
        api
        .get(url)
        .then(response => {
            setRelatorio(response.data);
        });
      } catch (err) {
          alert("Não foi possível encontrar o relatório, tente novamente");
      }  
    }, [])


    switch (props.location.state) {
        case "relatoriocontato":
            const getContatoContent = contato => {
                let content = [];
                console.log(relatorio)
                for (let idx in contato) {
                  const item = contato[idx];
                  console.log(item)
                  content.push( 
                    <li>
                        <div>
                            <p>{item.id}</p>
                            <p>{item.nome}</p>
                            <p>{item.email}</p>
                            <p>{item.telefone}</p>
                        </div>
                    </li>
                    )

                  // Aqui dentro do push devemos colocar o html da parte de cada um dos contatos
                  }
                
                return content
              };

            return (
                <Fragment>
                    <Accessibility />
                    <NavBar />
                    <main className="main">
                        <ul>
                            {getContatoContent(relatorio)}
                        </ul>
                    </main>
                    <Footer />
                </Fragment>
            )
        
        case "CPF":
            const getCPFContent = cpf => {
                let content = [];
                for (let idx in cpf) {
                  const item = cpf[idx];
                  content.push( 
                    <li>
                        <div>
                            <p>{item.id_turma}</p>
                            <p>{item.nomeDoCurso}</p>
                            <p>{item.idPropositor}</p>
                            <p>{item.propositor}</p>
                            <p>{//Um item.alunos é uma lista, tem que percorrer 
                            }</p>
                        </div>
                    </li>
                    )

                  // Dentro do push devemos colocar o html da parte de cada um dos cpfs
                }
                return content;
              };

            return (
                <Fragment>
                    <Accessibility />
                    <NavBar />
                    <main className="main">
                        <ul>
                            {getCPFContent(relatorio)}
                        </ul>
                    </main>
                    <Footer />
                </Fragment>
            )
        
        case "frequencia":
            const getFrequenciaContent = frequencia => {
                let content = [];
                for (let idx in frequencia) {
                  const item = frequencia[idx];
                  content.push(  
                    <li>
                        <div>
                            <p>{item.Nome}</p>
                            <p>{item.cpf}</p>
                            <p>{item.id_aluno}</p>
                            <p>{item.id_user_aluno}</p>
                            <p>{//Um item.Turma é uma lista, tem que percorrer 
                            }</p>
                        </div>
                    </li>
                   )

                  // Dentro do push devemos colocar o html da parte de cada um dos cpfs
                }
                return content;
              };

            return (
                <Fragment>
                    <Accessibility />
                    <NavBar />
                    <main className="main">
                        <ul>
                            {getFrequenciaContent(relatorio)}
                        </ul>
                    </main>
                    <Footer />
                </Fragment>
            )
        
        case "profissao":
            const getProfissaoContent = profissao => {
                let content = [];
                for (let idx in profissao) {
                  const item = profissao[idx];
                  content.push(   )

                  // Dentro do push devemos colocar o html da parte de cada um dos cpfs
                }
                return content;
              };

            return (
                <Fragment>
                    <Accessibility />
                    <NavBar />
                    <main className="main">
                        <ul>
                            {getProfissaoContent(relatorio)}
                        </ul>
                    </main>
                    <Footer />
                </Fragment>
            )
        
        case "CAP":
            const getCAPContent = cap => {
                let content = [];
                for (let idx in cap) {
                  const item = cap[idx];
                  content.push(   )

                  // Dentro do push devemos colocar o html da parte de cada um dos cpfs
                }
                return content;
              };

            return (
                <Fragment>
                    <Accessibility />
                    <NavBar />
                    <main className="main">
                        <ul>
                            {getCAPContent(relatorio)}
                        </ul>
                    </main>
                    <Footer />
                </Fragment>
            )
        
        case "superintendencia":
            const getSIContent = si => {
                let content = [];
                for (let idx in si) {
                  const item = si[idx];
                  content.push(   )

                  // Dentro do push devemos colocar o html da parte de cada um dos cpfs
                }
                return content;
              };

            return (
                <Fragment>
                    <Accessibility />
                    <NavBar />
                    <main className="main">
                        <ul>
                            {getSIContent(relatorio)}
                        </ul>
                    </main>
                    <Footer />
                </Fragment>
            )
        
        case "unidade":
            const getUnidadeContent = unid => {
                let content = [];
                for (let idx in unid) {
                  const item = unid[idx];
                  content.push(   )

                  // Dentro do push devemos colocar o html da parte de cada um dos cpfs
                }
                return content;
              };

            return (
                <Fragment>
                    <Accessibility />
                    <NavBar />
                    <main className="main">
                        <ul>
                            {getUnidadeContent(relatorio)}
                        </ul>
                    </main>
                    <Footer />
                </Fragment>
            )
        
        case "concluintes":
            const getConcluintesContent = concluintes => {
                let content = [];
                for (let idx in concluintes) {
                  const item = concluintes[idx];
                  content.push( 
                    <li>
                        <div>
                            <p>{item.id_turma}</p>
                            <p>{item.nome_do_curso}</p>
                            <p>{item.id_do_responsavel}</p>
                            <p>{item.nomeDoPropositor}</p>
                            <p>{item.Carga_Horaria_Total}</p>
                            <p>{//Um item.cursistas é uma lista, tem que percorrer 
                            }</p>
                        </div>
                    </li>
                    )

                  // Dentro do push devemos colocar o html da parte de cada um dos cpfs
                }
                return content;
              };

            return (
                <Fragment>
                    <Accessibility />
                    <NavBar />
                    <main className="main">
                        <ul>
                            {getConcluintesContent(relatorio)}
                        </ul>
                    </main>
                    <Footer />
                </Fragment>
            )
    }

}

export default Relatorio
