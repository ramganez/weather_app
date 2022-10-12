import { useState } from 'react';

import './App.css';

import HeaderComponent from './components/Header';
import QueryComponent from './components/Query';
import TableComponent from './components/Table';
import EmptyComponent from './components/Empty';

function App() {
  const [rows, setRows] = useState([]);
  const [dateSelected, setDateSelected] = useState(false);

  return (
    <div className="App">
      <HeaderComponent></HeaderComponent>
      <QueryComponent setDateSelected={setDateSelected} setRows={setRows}></QueryComponent>
      {(rows.length > 0) ? <TableComponent rows={rows} setRows={setRows}></TableComponent> : <EmptyComponent dateSelected={dateSelected}></EmptyComponent>}
    </div>
  );
}

export default App;
