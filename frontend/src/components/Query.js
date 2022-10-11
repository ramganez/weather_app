import * as React from 'react';
import dayjs from 'dayjs';
import TextField from '@mui/material/TextField';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider';
import { DateTimePicker } from '@mui/x-date-pickers/DateTimePicker';
import Stack from '@mui/material/Stack';

export default function QueryComponent() {
    const [value, setValue] = React.useState(dayjs('2018-01-01T00:00:00.000Z'));

    return (
        <LocalizationProvider dateAdapter={AdapterDayjs}>
            <Stack className='Query-Stack' spacing={3}>
                <DateTimePicker
                    className="DateTime-Input"
                    label="Responsive"
                    renderInput={(params) => <TextField {...params} />}
                    value={value}
                    onChange={(newValue) => {
                        setValue(newValue);
                    }}
                />
            </Stack>
        </LocalizationProvider>
    );
}
