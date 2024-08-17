import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import { getLastUpdate, postTweet } from '../api';

const DashboardContainer = styled.div`
  padding: 2rem;
`;

const Button = styled.button`
  background-color: #3498db;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  cursor: pointer;
  &:hover {
    background-color: #2980b9;
  }
`;

function Dashboard() {
  const [lastUpdate, setLastUpdate] = useState(null);

  useEffect(() => {
    fetchLastUpdate();
  }, []);

  const fetchLastUpdate = async () => {
    const data = await getLastUpdate();
    setLastUpdate(data ? data.update_time : 'Never');
  };

  const handlePostTweet = async () => {
    try {
      await postTweet();
      alert('Tweet posted successfully!');
      fetchLastUpdate();
    } catch (error) {
      alert('Error posting tweet: ' + error.message);
    }
  };

  return (
    <DashboardContainer>
      <h1>Dashboard</h1>
      <p>Last update: {lastUpdate}</p>
      <Button onClick={handlePostTweet}>Post Tweet Now</Button>
    </DashboardContainer>
  );
}

export default Dashboard;
