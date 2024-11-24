import React, { useState } from "react";
import axios from "axios";
import "../App.css";



const Emoji = ({ emojiName, setEmojiName }) => {
  const handleEmojiChange = (e) => setEmojiName(e.target.value);
  const [selectedFile, setSelectedFile] = useState(null);
  const [previewUrl, setPreviewUrl] = useState("");
  

  const handleEmojiClick = (emoji) => {
    console.log(`Emoji selected: ${emoji}`);
    alert(`You selected ${emoji}!`);
  };

  return (
    <div className="container">
      <header className="header">
        <h2>PUT YOU FIRST!</h2>
      </header>

      <main className="main">
        <h1>Delete Your Ex!</h1>
        <div className="preview-box">
          <div className="emoji-selection-container">
            <h4>Select Your Emoji</h4>
            <div className="emoji-grid">
            <button className="emoji-btn" onClick={() => handleEmojiChange("random")}>
                <img src="/game-die.png" alt="Emoji 1" className="emoji-img" />
              </button>
            <button className="emoji-btn" onClick={() => handleEmojiChange("skull")}>
                <img src="/skull-and-crossbones.png" alt="Emoji 1" className="emoji-img" />
              </button>
              <button className="emoji-btn" onClick={() => handleEmojiChange("goblin")}>
                <img src="/goblin.png" alt="Emoji 1" className="emoji-img" />
              </button>
              <button className="emoji-btn" onClick={() => handleEmojiChange("pile-of-poo")}>
                <img src="/pile-of-poo.png" alt="Emoji 2" className="emoji-img" />
              </button>
              <button className="emoji-btn" onClick={() => handleEmojiChange("ogre")}>
                <img src="/ogre.png" alt="Emoji 3" className="emoji-img" />
              </button>
              <button className="emoji-btn" onClick={() => handleEmojiChange("clown-face")}>
                <img src="/clown-face.png" alt="Emoji 4" className="emoji-img" />
              </button>
              <button className="emoji-btn" onClick={() => handleEmojiChange("angry-face")}>
                <img src="/angry-face-with-horns.png" alt="Emoji 5" className="emoji-img" />
              </button>
              <button className="emoji-btn" onClick={() => handleEmojiChange("nauseated-face")}>
                <img src="/nauseated-face.png" alt="Emoji 6" className="emoji-img" />
              </button>
              <button className="emoji-btn" onClick={() => handleEmojiChange("face-vomiting")}>
                <img src="/face-vomiting.png" alt="Emoji 7" className="emoji-img" />
              </button>
              <button className="emoji-btn" onClick={() => handleEmojiChange("robot")}>
                <img src="/robot.png" alt="Emoji 8" className="emoji-img" />
              </button>
            </div>
          </div>
        </div>
        <p className="description">
          Easily remove undesired people from your Google Photos pictures or
          cover their face with emojis.
        </p>
        <p>
          Upload and Process
        </p>
      </main>
      <section className="steps">
        <h2>How to remove your ex from your pictures</h2>
        <div className="steps-grid">
        <div className="step">
            <span className="icon">✔️</span>
            <h3>1. Select</h3>
            <p>
              Select a picture of the person you want to hide from your files.
            </p>
          </div>
          <div className="step">
            <span className="icon">🗑️</span>
            <h3>2. Hide</h3>
            <p>
              The app covers that person with the selected emoji.
            </p>
          </div>
          <div className="step">
            <span className="icon">🎉</span>
            <h3>3. Enjoy</h3>
            <p>
              Download the created pictures to your device.
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

export default Emoji;
