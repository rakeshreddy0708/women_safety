import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { io } from 'socket.io-client';
import Dashboard from './components/Dashboard';

const socket = io('http://localhost:5000');

function App() {
  const [alerts, setAlerts] = useState([]);
  const [genderDistribution, setGenderDistribution] = useState({});
  const [weather, setWeather] = useState({});

  useEffect(() => {
    socket.on('new_alert', (data) => {
      setAlerts((prevAlerts) => [...prevAlerts, data]);
    });

    const fetchData = async () => {
      const alertsResponse = await axios.get('http://localhost:5000/alerts');
      setAlerts(alertsResponse.data);

      const genderResponse = await axios.get('http://localhost:5000/gender_distribution');
      setGenderDistribution(genderResponse.data);

      const weatherResponse = await axios.get('http://localhost:5000/weather');
      setWeather(weatherResponse.data);
    };

    fetchData();
  }, []);

  return (
    <div className="App">
      <h1>Women Safety Analytics</h1>
      <Dashboard alerts={alerts} genderDistribution={genderDistribution} weather={weather} />
    </div>
  );
}

export default App;
