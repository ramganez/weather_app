import { useState } from 'react';

import './App.css';

import HeaderComponent from './components/Header';
import QueryComponent from './components/Query';
import TableComponent from './components/Table';

function App() {
  const [rows, setRows] = useState([]);

  return (
    <div className="App">
      <HeaderComponent></HeaderComponent>
      <QueryComponent setRows={setRows}></QueryComponent>
      {(rows.length > 0) ? <TableComponent rows={rows} setRows={setRows}></TableComponent> : null}
    </div>
  );
}

export default App;
