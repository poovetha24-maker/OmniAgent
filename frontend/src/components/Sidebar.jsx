import {
  Bot,
  Plus,
  MessageSquare,
  Settings,
  Database
} from "lucide-react";

function Sidebar({ onNewChat }) {
  return (
    <aside className="sidebar">

      <div className="logo-section">
        <div className="logo">
          <Bot size={25} />
        </div>

        <div>
          <h2>OmniAgent</h2>
          <span>AI Assistant</span>
        </div>
      </div>

      <button
        className="new-chat"
        onClick={onNewChat}
      >
        <Plus size={18} />
        New Chat
      </button>

      <div className="sidebar-title">
        CONVERSATIONS
      </div>

      <div className="conversation">
        <MessageSquare size={17} />
        <span>Current Conversation</span>
      </div>

      <div className="sidebar-title">
        SYSTEM
      </div>

      <div className="sidebar-item">
        <Database size={17} />
        <span>Memory</span>
      </div>

      <div className="sidebar-item">
        <Settings size={17} />
        <span>Settings</span>
      </div>

      <div className="sidebar-bottom">
        <div className="agent-card">
          <div className="agent-avatar">
            AI
          </div>

          <div>
            <strong>OmniAgent</strong>
            <small>Connected</small>
          </div>
        </div>
      </div>

    </aside>
  );
}

export default Sidebar;