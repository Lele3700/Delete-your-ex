import React, { useState } from "react";
import Emoji from "./EmojiSelection";
import MassSelection from "./MassSelection";

const ParentComponent = () => {
  const [emojiName, setEmojiName] = useState(""); // Shared state for emoji

  return (
    <div>
      <Emoji emojiName={emojiName} setEmojiName={setEmojiName} />
      <MassSelection emojiName={emojiName} />
    </div>
  );
};

export default ParentComponent;