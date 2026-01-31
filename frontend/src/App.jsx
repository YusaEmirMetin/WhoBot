import React, { useState } from 'react';
import './App.css';

function App() {
  const [searchName, setSearchName] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSearch = async (e) => {
    e.preventDefault();
    
    if (!searchName.trim()) {
      setError('Please enter a person\'s name');
      return;
    }

    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await fetch('http://localhost:5000/api/search', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ name: searchName }),
      });

      const data = await response.json();

      if (data.success) {
        setResult(data);
        setSearchName('');
      } else {
        setError(data.error || 'An error occurred');
      }
    } catch (err) {
      setError('Failed to connect to server. Make sure backend is running on http://localhost:5000');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <header className="header">
        <h1>🤖 WhoBot</h1>
        <p>Discover fascinating insights about anyone</p>
      </header>

      <main className="main">
        <form onSubmit={handleSearch} className="search-form">
          <input
            type="text"
            placeholder="Enter a person's name (e.g., Einstein, Marie Curie, Steve Jobs)..."
            value={searchName}
            onChange={(e) => setSearchName(e.target.value)}
            className="search-input"
            disabled={loading}
          />
          <button type="submit" className="search-btn" disabled={loading}>
            {loading ? 'Searching...' : 'Search'}
          </button>
        </form>

        {error && (
          <div className="error-box">
            <p>⚠️ {error}</p>
          </div>
        )}

        {result && (
          <div className="result-box">
            <h2>{result.name}</h2>
            <p className="result-text">{result.info}</p>
          </div>
        )}

        {!result && !error && !loading && (
          <div className="info-box">
            <p>👋 Welcome to WhoBot! Enter a person's name to get AI-generated insights about them.</p>
          </div>
        )}
      </main>

      <footer className="footer">
        <p>Powered by Groq API & React</p>
      </footer>
    </div>
  );
}

export default App;
