import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import React from 'react';


export default function TableComponent(props) {

  return (
    <TableContainer component={Paper}>
      <Table>
        <TableHead>
          <TableRow>
            <TableCell>Date</TableCell>
            <TableCell>Time</TableCell>
            <TableCell>Temperature</TableCell>
            <TableCell>Humidity</TableCell>
            <TableCell>Wind Direction</TableCell>
            <TableCell>Wind Speed</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {props.rows.map((row) => (
            <TableRow key={row.date_time_local}>
              <TableCell>
                {row.date}
              </TableCell>
              <TableCell>
                {row.time}
              </TableCell>
              <TableCell>{row.temperature}</TableCell>
              <TableCell>{row.relative_humidity}</TableCell>
              <TableCell>{row.wind_dir}</TableCell>
              <TableCell>{row.wind_speed}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>

  );
}

