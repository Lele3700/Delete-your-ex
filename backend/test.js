import React, { useState } from "react";
import axios from "axios";

function App() {
    const [images, setImages] = useState(["lara_lean2.jpeg", "lara_victoria.jpeg"]);
    const [exImage, setExImage] = useState("lara.jpeg");
    const [results, setResults] = useState([]);

    const processImages = async () => {
        try {
            const response = await axios.post("http://127.0.0.1:5000/process-image", {
                ex_image: exImage,
                images: images,
            });
            setResults(response.data.results);
        } catch (error) {
            console.error("Error processing images:", error);
        }
    };

    return (
        <div>
            <h1>Face Processing App</h1>
            <button onClick={processImages}>Process Images</button>
            <ul>
                {results.map((result, index) => (
                    <li key={index}>
                        {result.image}: {result.output || result.error}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default App;
