import React from 'react';
import { Link, useNavigate } from 'react-router-dom';
import styled from 'styled-components';

const Nav = styled.nav`
  background-color: #2c3e50;
  padding: 1rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
`;

const NavLink = styled(Link)`
  color: white;
  text-decoration: none;
  margin-right: 1rem;
  &:hover {
    color: #3498db;
  }
`;

const LogoutButton = styled.button`
  background-color: #e74c3c;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  cursor: pointer;
  &:hover {
    background-color: #c0392b;
  }
`;

function Navbar({ onLogout }) {
  const navigate = useNavigate();

  const handleLogout = () => {
    onLogout();
    navigate('/login');
  };

  return (
    <Nav>
      <div>
        <NavLink to="/">Dashboard</NavLink>
        <NavLink to="/templates">Tweet Templates</NavLink>
        <NavLink to="/poker-data">Poker Data</NavLink>
      </div>
      <LogoutButton onClick={handleLogout}>Logout</LogoutButton>
    </Nav>
  );
}

export default Navbar;
