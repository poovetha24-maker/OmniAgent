import { Bot, User } from "lucide-react";

function Message({ role, content, loading }) {
  const isUser = role === "user";

  return (
    <div
      className={`message-row ${
        isUser ? "user" : "assistant"
      }`}
    >

      <div
        className={`message-avatar ${
          isUser ? "user-avatar" : "ai-avatar"
        }`}
      >
        {isUser ? (
          <User size={18} />
        ) : (
          <Bot size={18} />
        )}
      </div>

      <div className="message-content">

        <div className="message-name">
          {isUser ? "You" : "OmniAgent"}
        </div>

        <div
          className={`message-bubble ${
            loading ? "loading" : ""
          }`}
        >
          {loading ? (
            <div className="typing">
              <span></span>
              <span></span>
              <span></span>
            </div>
          ) : (
            content
          )}
        </div>

      </div>

    </div>
  );
}

export default Message;