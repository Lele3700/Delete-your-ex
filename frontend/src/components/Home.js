import React, { useState } from "react";
import { Link } from "react-router-dom";
import "../App.css";

const Home = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [previewUrl, setPreviewUrl] = useState("");

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setSelectedFile(file);

      // Create a preview URL
      const filePreview = URL.createObjectURL(file);
      setPreviewUrl(filePreview);
    }
  };

  const handleFileUpload = () => {
    if (selectedFile) {
      // Logic to handle file upload (e.g., send to server)
      console.log("File uploaded:", selectedFile);
      alert("File uploaded successfully!");
    } else {
      alert("Please select a file first.");
    }
  };

  return (
    <div className="container">
      <header className="header">
        <h2>PUT YOU FIRST!</h2>
      </header>

      <main className="main">
        <h1>Delete Your Ex!</h1>
        <div className="preview-box">
          <input type="file" onChange={handleFileChange} />
          <button onClick={handleFileUpload}> Upload</button>
        </div>
        <p className="description">
          Easily remove undesired people from your Google Photos pictures or
          cover their face with emojis.
        </p>
        <button className="cta-btn" onClick={handleFileUpload}>
          Upload and Process
        </button>
        <Link to="/emoji-selection" className="cta-btn">Go to Emoji Selection</Link>

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

export default Home;
