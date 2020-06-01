import React from 'react';
import { BrowserRouter } from 'react-router-dom'

import Routes from './routes';
import './global.css';

function App() {
  return (
    <BrowserRouter>
      <div className="grid-container">
          <Routes></Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;