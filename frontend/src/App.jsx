import { useState } from "react";
import Sidebar from "./components/Sidebar";
import ChatBox from "./components/ChatBox";
import Message from "./components/Message";

function App() {
  const [messages, setMessages] = useState([
    {
      role: "assistant",
      content: "Hello! 👋 I am OmniAgent. How can I help you today?"
    }
  ]);

  const [loading, setLoading] = useState(false);

  const sendMessage = async (text) => {
    if (!text.trim()) return;

    setMessages((previous) => [
      ...previous,
      {
        role: "user",
        content: text
      }
    ]);

    setLoading(true);

    try {
      const response = await fetch("http://localhost:8000/api/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          message: text
        })
      });

      if (!response.ok) {
        throw new Error("Backend request failed");
      }

      const data = await response.json();

      setMessages((previous) => [
        ...previous,
        {
          role: "assistant",
          content: data.response || data.message || "No response received."
        }
      ]);
    } catch (error) {
      console.error(error);

      setMessages((previous) => [
        ...previous,
        {
          role: "assistant",
          content:
            "⚠️ Backend is not connected. Please start the FastAPI backend."
        }
      ]);
    } finally {
      setLoading(false);
    }
  };

  const newChat = () => {
    setMessages([
      {
        role: "assistant",
        content: "New conversation started! How can I help you?"
      }
    ]);
  };

  return (
    <div className="app">
      <Sidebar onNewChat={newChat} />

      <main className="main-content">
        <header className="topbar">
          <div>
            <h1>OmniAgent</h1>
            <p>AI Agent with Memory & Tools</p>
          </div>

          <div className="status">
            <span className="status-dot"></span>
            Online
          </div>
        </header>

        <section className="chat-area">
          {messages.map((message, index) => (
            <Message
              key={index}
              role={message.role}
              content={message.content}
            />
          ))}

          {loading && (
            <Message
              role="assistant"
              content="Thinking..."
              loading={true}
            />
          )}
        </section>

        <ChatBox
          onSend={sendMessage}
          disabled={loading}
        />
      </main>
    </div>
  );
}

export default App;