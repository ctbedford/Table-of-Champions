import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import styled from 'styled-components';
import Navbar from './components/Navbar';
import Dashboard from './components/Dashboard';
import TweetTemplates from './components/TweetTemplates';
import PokerData from './components/PokerData';
import Login from './components/Login';
import { logout } from './api';

const AppContainer = styled.div`
  background-color: #1a1b26;
  color: white;
  min-height: 100vh;
`;

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem('access_token');
    setIsAuthenticated(!!token);
  }, []);

  const handleLogout = () => {
    logout();
    setIsAuthenticated(false);
  };

  return (
    <Router>
      <AppContainer>
        {isAuthenticated && <Navbar onLogout={handleLogout} />}
        <Routes>
          <Route path="/login" element={<Login setIsAuthenticated={setIsAuthenticated} />} />
          <Route
            path="/"
            element={isAuthenticated ? <Dashboard /> : <Navigate to="/login" />}
          />
          <Route
            path="/templates"
            element={isAuthenticated ? <TweetTemplates /> : <Navigate to="/login" />}
          />
          <Route
            path="/poker-data"
            element={isAuthenticated ? <PokerData /> : <Navigate to="/login" />}
          />
        </Routes>
      </AppContainer>
    </Router>
  );
}

export default App;
