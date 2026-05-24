import React from 'react'

export default function ChatMessage({msg}){
  const isAI = msg.sender === 'ai'
  return (
    <div className={`message ${isAI? 'message-ai':'message-user'}`}>
      <div className="bubble">
        <div className="text">{msg.text}</div>
        <div className="time">{new Date(msg.time).toLocaleTimeString([], {hour:'2-digit',minute:'2-digit'})}</div>
      </div>
    </div>
  )
}
