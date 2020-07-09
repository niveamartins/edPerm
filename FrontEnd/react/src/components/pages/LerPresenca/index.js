import React, { Component } from 'react';
//npm install --save react-qr-reader
import QrReader from 'react-qr-reader';



class LerPresenca extends Component {

    constructor(props) {
        super(props);
        this.state = {
          delay: 300,
          result: "No result"
        };
        this.handleScan = this.handleScan.bind(this);

      }
  
    handleScan = data => {
      if (data) {
        this.setState({
          result: data
        })
        alert('O QR Code foi lido!');
      }
    }
    handleError = err => {
      console.error(err)
    }

    getDadosQR = dadosQR => {

      if (dadosQR != "No result") {
        dadosQR = dadosQR.toString()
        dadosQR = JSON.parse(dadosQR)

        let content = []
        content.push(
      
        
          <table className="card-list">
            <tr className="content">
              <td className="name">CPF</td>
              <td className="value">{dadosQR.cpf}</td>
            </tr>
            <tr className="content">
              <td className="name">E-mail</td>
              <td className="value">{dadosQR.email}</td>
            </tr>
          </table>
      
      )
      return content
      }
  
    }

    render() {
      return ( 
          <div>
            <h2>Leitor de QrCode</h2>
            
            <div>
              <QrReader
              delay={300}
              onError={this.handleError}
              onScan={this.handleScan}
              facingMode="enviroment"
              style={{ height:'100%' }}
              />
            </div>
            
            <div>
              {this.getDadosQR(this.state.result)}
            </div>
          
            <button className="button">Confirmar</button>
          
          

          </div>

      )
    }
  }

export default LerPresenca;