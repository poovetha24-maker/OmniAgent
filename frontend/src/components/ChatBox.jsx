import { useState } from "react";
import {
  Send,
  Paperclip
} from "lucide-react";

function ChatBox({ onSend, disabled }) {
  const [input, setInput] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();

    if (!input.trim() || disabled) {
      return;
    }

    onSend(input);
    setInput("");
  };

  const handleKeyDown = (event) => {
    if (
      event.key === "Enter" &&
      !event.shiftKey
    ) {
      event.preventDefault();
      handleSubmit(event);
    }
  };

  return (
    <div className="chatbox-wrapper">

      <form
        className="chatbox"
        onSubmit={handleSubmit}
      >

        <button
          type="button"
          className="icon-button"
          title="Attach file"
        >
          <Paperclip size={20} />
        </button>

        <textarea
          value={input}
          onChange={(event) =>
            setInput(event.target.value)
          }
          onKeyDown={handleKeyDown}
          placeholder="Ask OmniAgent anything..."
          disabled={disabled}
          rows="1"
        />

        <button
          type="submit"
          className="send-button"
          disabled={
            disabled || !input.trim()
          }
        >
          <Send size={19} />
        </button>

      </form>

      <p className="input-hint">
        OmniAgent can use memory, tools and AI reasoning.
      </p>

    </div>
  );
}

export default ChatBox;