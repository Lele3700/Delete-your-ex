import React, { useState } from "react";
import { Link } from "react-router-dom";
import axios from "axios";

import "../App.css";

const Home = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [image, setImage] = useState(null);
  const [error, setError] = useState(null);
  const [processedImage, setProcessedImage] = useState(null);
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
  const handleUpload = async () => {
    const formData = new FormData();
    formData.append("file", image);

    try {
      const response = await axios.post("http://127.0.0.1:5000/api/upload-image", formData, {
        responseType: "blob",
      });
      const blob = new Blob([response.data], { type: "image/jpeg" });
      const imageUrl = URL.createObjectURL(blob);
      setProcessedImage(imageUrl);
      alert("File uploaded successfully!");
    } catch (err) {
      console.error(err);
      setError("Error processing the image");
    }
  };

  const handleFileError = () => {
    if (!selectedFile) {
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
      
        <h1>Put you First!</h1>
        <h2>The quick and easy solution for your peace of mind</h2>
        <div className="choose-file-box">
          <input type="file" onChange={handleFileChange} />
          <button onClick={handleUpload}> Upload Your Photo</button>
          {processedImage && <img src={processedImage} alt="Processed" />}

        </div>
        <p className="description">
          Easily hide undesired people from your gallery by
          covering their face with emojis of your choice.
        </p>
        <button className="cta-btn" onClick={handleFileError}>
        <Link to="/ex-identified" className="cta-btn"> Next Steps!</Link>
        </button>
   


      </main>
      <section className="steps">
        <h2>How to hide your ex from your pictures</h2>
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

export default Home;
