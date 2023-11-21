import React, { useState, useEffect } from 'react';
import axios from 'axios';

const RoomList = () => {
    const [rooms, setRooms] = useState([]);

    useEffect(() => {
        axios.get('/rooms/') // Adjust this to your Django API endpoint
            .then(response => {
                setRooms(response.data);
            })
            .catch(error => console.error('Error fetching rooms: ', error));
    }, []);

    return (
        <div>
            <h1>Room List</h1>
            <ul>
                {rooms.map(room => (
                    <li key={room.id}>Room {room.room_number} - {room.room_type}</li>
                ))}
            </ul>
        </div>
    );
};

export default RoomList;
