import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Home from "./components/Home"; // Import the Home component
import ExIdentified from "./components/ExIdentified";
import Emoji from "./components/EmojiSelection";

const App = () => {
  return (
    <Router>
      <div>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/emoji-selection" element={<Emoji />} />
          <Route path="/ex-identified" element={<ExIdentified/>} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;


