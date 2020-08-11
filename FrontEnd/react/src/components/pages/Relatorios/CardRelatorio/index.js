import React, { Fragment } from 'react'

import './cardRelatorios.css'

const card = (props) => {
   return (
      <Fragment>
         <div className="document__link">
            <h3 className="document__link-title bold">{props.title}</h3>
            <div className="line"></div>
            <div className="line"></div>
            <div className="line"></div>
            <div className="line"></div>
         </div>
      </Fragment>
   )
}

export default card