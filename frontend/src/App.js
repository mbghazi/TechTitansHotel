import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import RoomList from './components/RoomList';
import ReservationForm from './components/ReservationForm';
import Navigation from './components/Navigation';

const App = () => {
    return (
        <Router>
            <Navigation />
            <Switch>
                <Route path="/" exact component={RoomList} />
                <Route path="/reserve" component={ReservationForm} />
            </Switch>
        </Router>
    );
};

export default App;
