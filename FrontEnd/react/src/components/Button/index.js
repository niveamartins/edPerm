import React from 'react'
import { Link } from 'react-router-dom'

import './button.css'

const button = (props) => (
      <Link to={props.link}>
         <div className="button__link">
            <h3 className="button__link-title bold">{props.title}</h3>
            <p className="button__link-description bold">{props.description}</p>
         </div>
      </Link>
)

export default button