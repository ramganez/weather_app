import * as React from 'react';

import TextField from '@mui/material/TextField';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { MobileDatePicker } from '@mui/x-date-pickers/MobileDatePicker';
import { MobileTimePicker } from '@mui/x-date-pickers/MobileTimePicker';
import Stack from '@mui/material/Stack';

const axios = require('axios').default;

export default function QueryComponent(props) {
    const [dateValue, setDateValue] = React.useState();
    const [timeValue, setTimeValue] = React.useState("");

    const handleCloseDate = () => {
        axios.post('/api/weekly', {
            query: dateValue.format('YYYY-MM-DD'),
            withTime: false,
        })
            .then(function (response) {
                props.setRows(response.data);
            })
            .catch(function (error) {
                console.log(error);
            });
    };

    const handleCloseTime = () => {
        axios.post('/api/weekly', {
            query: dateValue.format('YYYY-MM-DD') + timeValue.format(" H:mm"),
            withTime: true,
        })
            .then(function (response) {
                props.setRows(response.data);
            })
            .catch(function (error) {
                console.log(error);
            });
    };

    return (
        <>
            <LocalizationProvider dateAdapter={AdapterDayjs}>
                <Stack className='Query-Stack' spacing={3}>
                    <MobileDatePicker
                        className="DateTime-Input"
                        label="Select Date"
                        renderInput={(params) => <TextField {...params} />}
                        value={dateValue}
                        onChange={(newValue) => {
                            setDateValue(newValue);
                        }}
                        onClose={handleCloseDate}
                    />
                    <MobileTimePicker
                        className="DateTime-Input"
                        label="Select Time"
                        value={timeValue}
                        onChange={(newValue) => {
                            setTimeValue(newValue);
                        }}
                        renderInput={(params) => <TextField {...params} />}
                        onClose={handleCloseTime}
                    />
                </Stack>
            </LocalizationProvider>
        </>
    );
}
