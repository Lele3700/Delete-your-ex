import React, { useState } from "react";
import { Link } from "react-router-dom";
import "../App.css";

const ExIdentified = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [previewUrl, setPreviewUrl] = useState("");

  const imagePath = "/LaraBeingCute.jpg"

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
      <img
                src={"/HideYourExLogo.jpg"}
                alt="Random"
                style={{ width: "auto", maxWidth: "5%", height: "auto" }}
            />
        <h2>Hide Your Ex.</h2>
      </header>

      <main className="main">
        <h1>Successfully Identified !</h1>
        <div className="picture-box">
            <img
                src={imagePath}
                alt="Random"
                style={{ width: "auto", maxWidth: "50%", height: "auto" }}
            />
        </div>
        <button>
        <Link to="/emoji-selection" className="cta-btn">Go to Emoji Selection</Link>
        </button>
        
        
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
            <h3>2. Remove</h3>
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

export default ExIdentified;
