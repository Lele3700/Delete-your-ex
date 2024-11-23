import React from "react";
import "./App.css";
//import GooglePicker from './components/GooglePicker';


const App = () => {
  // useEffect(() => {
  //   const script = document.createElement('script');
  //   script.src = 'https://apis.google.com/js/api.js';
  //   script.onload = () => {
  //     console.log('Google API script loaded.');
  //   };
  //   script.onerror = () => {
  //     console.error('Google API script failed to load.');
  //   };
  //   document.body.appendChild(script);
  // }, []);
  return (
    <div className="container">
      <header className="header">
        <h2>Put you first!</h2>
      </header>

      <main className="main">
        <h1>Delete your Ex!</h1>
        <div className="dropdown">
          <button className="dropdown-btn">Select method ▼</button>
        </div>
        <div className="preview-box">
        </div>
        <p className="description">
          Easily remove undesired people from your Google Photos pictures or
          cover their face with emojis.
        </p>
        <button className="cta-btn">
          The quick and easy solution for your peace of mind.
        </button>
      </main>

      <section className="steps">
        <h2>How to remove your ex from your pictures</h2>
        <div className="steps-grid">
          <div className="step">
            <span className="icon">✔️</span>
            <h3>1. Select</h3>
            <p>
              Log in to Google Photos and select a picture of the person you
              want to remove.
            </p>
          </div>
          <div className="step">
            <span className="icon">🗑️</span>
            <h3>2. Remove</h3>
            <p>
              The app removes that person from your Google Photos Library.
            </p>
          </div>
          <div className="step">
            <span className="icon">🎉</span>
            <h3>3. Enjoy</h3>
            <p>
              Find the pictures without that person in your library and delete
              the old pictures.
            </p>
          </div>
        </div>
      </section>

      <footer className="footer">
        <div className="social-icons">
          <a href="#">Instagram</a>
          <a href="#">Facebook</a>
          <a href="#">Twitter</a>
          <a href="#">YouTube</a>
          <a href="#">LinkedIn</a>
        </div>
      </footer>
    </div>
  );
};

export default App;

