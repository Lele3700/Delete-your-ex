import React, { useState } from "react";
import { Link } from "react-router-dom";
import "../App.css";
import axios from "axios";

const MassSelection = ({ emojiName }) => {
  const [images, setImages] = useState([]);
  const [zipDownloadLink, setZipDownloadLink] = useState(""); // For download URL

  const handleImageChange = (e) => setImages([...e.target.files]);

  const handleSubmit = async () => {
    const formData = new FormData();
    images.forEach((image) => formData.append("images", image));
    formData.append("emoji_path", emojiName);

    try {
      const response = await axios.post(
        "http://127.0.0.1:5000/api/add-emojis",
        formData,
      { responseType: "blob" }
    );

      // Create a downloadable link for the zip file
      const blob = new Blob([response.data], { type: "application/zip" });
      const downloadUrl = URL.createObjectURL(blob);
      setZipDownloadLink(downloadUrl);
    } catch (err) {
      console.error("Error processing images:", err);
    }
  };

  return (
    <div className="container">
      <header className="header">
        <h2>Put You First.</h2>
      </header>

      <main className="main">
      <img
                src={"/HideYourExLogo.jpg"}
                alt="Random"
                style={{ width: "auto", maxWidth: "10%", height: "auto" }}
            />
        <h1>Put you First</h1>
        <div className="preview-box">
          <h3> select the files in which your ex appears.</h3>
          <input type="file" multiple onChange={handleImageChange} />
          <button onClick={handleSubmit} disabled={!emojiName || images.length === 0}>
            Add Emoji to Images
          </button>
          {zipDownloadLink && (
            <a href={zipDownloadLink} download="result.zip">
              Download Modified Images
            </a>
         )}
        </div>
        <p className="description">
          Easily remove undesired people from your Google Photos pictures or
          cover their face with emojis.
        </p>
        <button className="cta-btn" onClick={handleFileError}>
        <Link to="/ex-identified" className="cta-btn"> Go to Ex Identified Page</Link>
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

export default MassSelection;
