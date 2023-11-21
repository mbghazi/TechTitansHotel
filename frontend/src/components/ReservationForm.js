import React, { useState } from 'react';
import axios from 'axios';

const ReservationForm = () => {
    const [reservation, setReservation] = useState({
        guest: '', // Adjust fields based on your model
        room: '',
        startDate: '',
        endDate: '',
        // Add other fields as necessary
    });

    const handleChange = (e) => {
        setReservation({ ...reservation, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post('/api/reservations/', reservation)
            .then(response => {
                console.log('Reservation created:', response.data);
                // Handle success (e.g., redirect to a confirmation page)
            })
            .catch(error => console.error('Error creating reservation: ', error));
    };

    return (
        <form onSubmit={handleSubmit}>
            <h1>Create Reservation</h1>
            {/* Create form fields based on your reservation model */}
            <input type="text" name="guest" value={reservation.guest} onChange={handleChange} />
            {/* Add other input fields */}
            <button type="submit">Submit</button>
        </form>
    );
};

export default ReservationForm;
