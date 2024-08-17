import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import { getPokerData } from '../api';

const PokerDataContainer = styled.div`
  padding: 2rem;
`;

const Table = styled.table`
  width: 100%;
  border-collapse: collapse;
`;

const Th = styled.th`
  background-color: #2c3e50;
  color: white;
  padding: 0.5rem;
`;

const Td = styled.td`
  border: 1px solid #34495e;
  padding: 0.5rem;
`;

function PokerData() {
  const [pokerData, setPokerData] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchPokerData();
  }, []);

  const fetchPokerData = async () => {
    try {
      setIsLoading(true);
      const data = await getPokerData();
      setPokerData(data);
      setError(null);
    } catch (error) {
      setError('Failed to fetch poker data. Please try again later.');
    } finally {
      setIsLoading(false);
    }
  };

  if (isLoading) return <PokerDataContainer>Loading...</PokerDataContainer>;
  if (error) return <PokerDataContainer>{error}</PokerDataContainer>;

  return (
    <PokerDataContainer>
      <h1>Poker Data</h1>
      <Table>
        <thead>
          <tr>
            <Th>Name</Th>
            <Th>Net Winnings</Th>
            <Th>VPIP</Th>
            <Th>PFR</Th>
            <Th>Hours Played</Th>
            <Th>Hourly</Th>
            <Th>BB/Hour</Th>
          </tr>
        </thead>
        <tbody>
          {pokerData.map((player, index) => (
            <tr key={index}>
              <Td>{player.name}</Td>
              <Td>{player.net_winnings}</Td>
              <Td>{player.vpip}</Td>
              <Td>{player.pfr}</Td>
              <Td>{player.hours_played}</Td>
              <Td>{player.hourly}</Td>
              <Td>{player.bb_per_hour}</Td>
            </tr>
          ))}
        </tbody>
      </Table>
    </PokerDataContainer>
  );
}

export default PokerData;
