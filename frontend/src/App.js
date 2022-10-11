import { useState } from 'react';

import './App.css';

import HeaderComponent from './components/Header';
import QueryComponent from './components/Query';

function App() {
  const [rows, setRows] = useState([]);

  return (
    <div className="App">
      <HeaderComponent></HeaderComponent>
      <QueryComponent setRows={setRows}></QueryComponent>
      <pre>{JSON.stringify(rows, undefined, 2)}</pre>
    </div>
  );
}

export default App;
