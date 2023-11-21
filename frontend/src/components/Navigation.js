import React from 'react';
import { Link } from 'react-router-dom';

const Navigation = () => {
    return (
        <nav>
            <ul>
                <li><Link to="/">Home</Link></li>
                <li><Link to="/reserve">Make a Reservation</Link></li>
            </ul>
        </nav>
    );
};

export default Navigation;
