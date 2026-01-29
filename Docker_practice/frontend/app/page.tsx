"use client";

import { useState, useEffect, useRef } from "react";
import "./chat.css";

type ChatItem = {
  user: string;
  bot: string;
};

export default function Home() {
  const [message, setMessage] = useState("");
  const [chat, setChat] = useState<ChatItem[]>([]);
  const [loading, setLoading] = useState(false);
  const [mounted, setMounted] = useState(false); // Fix SSR hydration issues
  const scrollRef = useRef<HTMLDivElement>(null);

  // Placeholder options
  const placeholders = [
    "💬 Ask me anything, I’m listening…",
    "🤖 Type your question… let’s get smart!",
    "✨ What do you want to discover today?",
    "🧠 Feed me your curiosity…",
    "🚀 Your next idea starts here…",
    "🌟 Ask away… I’ll handle the rest!",
    "🔮 Type a question, see some magic…",
    "💡 Your AI assistant awaits your command…",
    "⚡ Shoot a question, get answers fast!",
    "🕹️ Control your AI — type something…"
  ];

  // Random placeholder on client
  const [placeholder, setPlaceholder] = useState("");
  useEffect(() => {
    setMounted(true);
    setPlaceholder(placeholders[Math.floor(Math.random() * placeholders.length)]);
  }, []);

  // Auto scroll whenever chat updates
  useEffect(() => {
    if (scrollRef.current) {
      scrollRef.current.scrollTo({
        top: scrollRef.current.scrollHeight,
        behavior: "smooth",
      });
    }
  }, [chat]);

  const sendMessage = async () => {
    if (!message.trim() || loading) return;

    const userMsg = message;
    setMessage("");
    setLoading(true);

    // Add user message and temporary bot placeholder
    setChat((prev) => [
      ...prev,
      { user: userMsg, bot: "⏳ Agent is generating response..." },
    ]);

    try {
      const res = await fetch("https://waqar5-backend-agent.hf.space/chat", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ message: userMsg }),
});

      const text = await res.text();
      let reply = text;

      try {
        const json = JSON.parse(text);
        reply = json.reply ?? text;
      } catch {}

      // Update last bot message with actual reply
      setChat((prev) =>
        prev.map((c, i) =>
          i === prev.length - 1 ? { ...c, bot: reply } : c
        )
      );
    } catch (err) {
      setChat((prev) =>
        prev.map((c, i) =>
          i === prev.length - 1
            ? { ...c, bot: "❌ Failed to reach server" }
            : c
        )
      );
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === "Enter") sendMessage();
  };

  if (!mounted) return null; // Prevent SSR mismatch

  return (
    <div className="app-container">
      {/* Fixed Header */}
      <h1 className="app-title">🤖 Cognitic AI Chat</h1>

      {/* Scrollable Chat Window */}
      <div ref={scrollRef} className="chat-window">
        {chat.length === 0 && (
          <p className="chat-placeholder">
            {placeholders[Math.floor(Math.random() * placeholders.length)]}
          </p>
        )}

        {chat.map((c, i) => (
          <div key={i} className="chat-message">
            {c.user && (
              <div className="message user-message">
                <img src="/hacker.png" className="avatar" />
                <div className="bubble user-bubble">{c.user}</div>
              </div>
            )}

            {c.bot && (
              <div className="message bot-message">
                <img src="/robot-assistant.png" className="avatar" />
                <div className="bubble bot-bubble">
                  {loading && i === chat.length - 1 ? (
                    <span className="typing">
                      <span>.</span>
                      <span>.</span>
                      <span>.</span>
                    </span>
                  ) : (
                    c.bot
                  )}
                </div>
              </div>
            )}
          </div>
        ))}
      </div>

      {/* Fixed Input */}
      <div className="input-container">
        <input
          type="text"
          placeholder={placeholder} // Random input placeholder
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={handleKeyDown}
          disabled={loading}
          className="chat-input"
        />
        <button
          className="send-btn"
          onClick={sendMessage}
          disabled={loading}
        >
          {loading ? "Thinking..." : "Send"}
        </button>
      </div>
    </div>
  );
}
