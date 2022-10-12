import * as React from 'react';
import Box from '@mui/material/Box';
import Alert from '@mui/material/Alert';
import AlertTitle from '@mui/material/AlertTitle';

export default function EmptyComponent(props) {

    return (
        <>
            {props.dateSelected ?
                <Box sx={{ width: '100%', maxWidth: 600, margin: 'auto' }}>
                    <Alert icon={false} style={{ color: 'black', border: 'none' }} variant="outlined" severity="error">
                        <AlertTitle><h4>There is no data available... — <strong>Upload new data <a rel="noreferrer" href='http://localhost:8000/' target="_blank">here</a> !!!</strong></h4></AlertTitle>
                    </Alert>
                </Box>
                : ''}
        </>
    );
}

