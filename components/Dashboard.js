import React from 'react';
import { Line } from 'react-chartjs-2';
import Chart from 'chart.js/auto';

function Dashboard({ alerts, genderDistribution, weather }) {
  const data = {
    labels: ['Male', 'Female'],
    datasets: [
      {
        label: 'Gender Distribution',
        data: [genderDistribution.male_count || 0, genderDistribution.female_count || 0],
        backgroundColor: ['rgba(75, 192, 192, 0.2)', 'rgba(153, 102, 255, 0.2)'],
        borderColor: ['rgba(75, 192, 192, 1)', 'rgba(153, 102, 255, 1)'],
        borderWidth: 1
      }
    ]
  };

  return (
    <div>
      <h2>Alerts</h2>
      <ul>
        {alerts.map((alert) => (
          <li key={alert.id}>{alert.message} - {alert.alert_type}</li>
        ))}
      </ul>
      <h2>Gender Distribution</h2>
      <Line data={data} />
      <h2>Weather Information</h2>
      <p>Temperature: {weather.temperature}°C</p>
      <p>Condition: {weather.condition}</p>
    </div>
  );
}

export default Dashboard;
