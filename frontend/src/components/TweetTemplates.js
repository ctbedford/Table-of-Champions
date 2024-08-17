import React, { useState, useEffect } from 'react';
import styled from 'styled-components';
import { getTemplates, updateTemplate, syncTemplate } from '../api';

const TemplatesContainer = styled.div`
  padding: 2rem;
`;

const TemplateItem = styled.div`
  margin-bottom: 1rem;
`;

const Button = styled.button`
  background-color: #3498db;
  color: white;
  border: none;
  padding: 0.5rem 1rem;
  cursor: pointer;
  margin-right: 0.5rem;
  &:hover {
    background-color: #2980b9;
  }
`;

function TweetTemplates() {
  const [templates, setTemplates] = useState({});

  useEffect(() => {
    fetchTemplates();
  }, []);

  const fetchTemplates = async () => {
    const data = await getTemplates();
    setTemplates(data);
  };

  const handleUpdateTemplate = async (show, content) => {
    await updateTemplate(show, content);
    fetchTemplates();
  };

  const handleSyncTemplate = async (show) => {
    try {
      await syncTemplate(show);
      alert(`Tweet sent successfully for ${show}`);
    } catch (error) {
      alert(`Failed to send tweet for ${show}: ${error.message}`);
    }
  };

  return (
    <TemplatesContainer>
      <h1>Tweet Templates</h1>
      {Object.entries(templates).map(([show, content]) => (
        <TemplateItem key={show}>
          <h3>{show}</h3>
          <textarea
            value={content}
            onChange={(e) => handleUpdateTemplate(show, e.target.value)}
          />
          <Button onClick={() => handleSyncTemplate(show)}>Sync</Button>
        </TemplateItem>
      ))}
    </TemplatesContainer>
  );
}

export default TweetTemplates;
