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
      dadosQR = dadosQR.toString()
      let content = []
      content.push(
      
        <p>
          {dadosQR}
        </p>
      
      )
      return content
  
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