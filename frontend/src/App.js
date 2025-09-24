

import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

const BACKEND_URL = 'http://127.0.0.1:8888';

function App() {
  const [mood, setMood] = useState('');
  const [tracks, setTracks] = useState([]); // State to hold the list of songs
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState('');

  const handleFormSubmit = async (event) => {
    event.preventDefault();
    setIsLoading(true);
    setTracks([]); // Clear previous results
    setError('');

    try {
      const response = await axios.post(
        `${BACKEND_URL}/api/get-recommendations`,
        { mood: mood }
      );
      setTracks(response.data.tracks); // Save the list of songs
    } catch (err) {
      console.error('Failed to get recommendations:', err);
      setError('Could not get recommendations. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>AI Mood Playlist Generator</h1>
        <p className="subtitle">Tell us your vibe, and we'll suggest some songs.</p>
        
        <div className="generator-container">
          <form onSubmit={handleFormSubmit}>
            <textarea
              value={mood}
              onChange={(e) => setMood(e.target.value)}
              placeholder="e.g., 'rainy afternoon' or 'upbeat workout'"
              rows="3"
              disabled={isLoading}
            />
            <button type="submit" className="spotify-button" disabled={isLoading}>
              {isLoading ? 'Finding Songs...' : 'Get Recommendations'}
            </button>
          </form>

          {/* If there are tracks, display them in a list */}
          {tracks.length > 0 && (
            <div className="results-list">
              {tracks.map((track, index) => (
                <div key={index} className="track-item">
                  <img src={track.album_art} alt={`Album art for ${track.title}`} className="album-art" />
                  <div className="track-info">
                    <div className="track-title">{track.title}</div>
                    <div className="track-artist">{track.artist}</div>
                  </div>
                </div>
              ))}
            </div>
          )}

          {error && <p className="error">{error}</p>}
        </div>
      </header>
    </div>
  );
}

export default App;

