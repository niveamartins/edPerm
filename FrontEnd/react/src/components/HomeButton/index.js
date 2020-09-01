import React from 'react'
import { Link } from 'react-router-dom'

import IconeHome from '../../assets/img/IconeHomeAzul.png'
import './homeButton.css'

export const HomeButton = () => {
   const width = window.innerWidth

   const isHomeButtonShown = width >= 1200 ? true : false
   
   return (
      <div className="home-desktop-button">
         { isHomeButtonShown && <Link to="/"><img src={IconeHome} alt="Ícone Casa Azul" title="Voltar para página inicial"></img></Link> }
      </div>
   )
}
