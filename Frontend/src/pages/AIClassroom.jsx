import React, { useState, useRef, useEffect } from 'react'
import ChatMessage from '../components/ChatMessage'

export default function AIClassroom(){
  const [messages, setMessages] = useState([
    {id:1, sender:'ai', text:"Hi Aarav! I’m your AI Teacher. How can I help you today?", time: new Date()}
  ])
  const [input, setInput] = useState('')
  const messagesEnd = useRef(null)

  useEffect(()=>{
    messagesEnd.current?.scrollIntoView({behavior:'smooth'})
  },[messages])

  function sendMessage(){
    if(!input.trim()) return
    const userMsg = {id:Date.now(), sender:'user', text:input.trim(), time:new Date()}
    setMessages(prev=>[...prev, userMsg])
    setInput('')

    // dummy AI response
    setTimeout(()=>{
      const aiMsg = {id:Date.now()+1, sender:'ai', text:'Got it — I can help with that. Tell me more or ask a question!', time:new Date()}
      setMessages(prev=>[...prev, aiMsg])
    }, 700)
  }

  function onKeyDown(e){
    if(e.key==='Enter' && !e.shiftKey){
      e.preventDefault(); sendMessage()
    }
  }

  return (
    <div className="card chat-container">
      <h3>AI Classroom</h3>
      <div className="chat-window">
        <div className="messages">
          {messages.map(m=> <ChatMessage key={m.id} msg={m} />)}
          <div ref={messagesEnd} />
        </div>
      </div>

      <div className="input-row">
        <button className="icon-btn" title="Voice mode">🎤</button>
        <textarea value={input} onChange={e=>setInput(e.target.value)} onKeyDown={onKeyDown} placeholder="Ask AI Teacher..." />
        <button className="send-btn" onClick={sendMessage}>Send</button>
        <button className="toggle-btn" title="Voice Mode">Voice</button>
      </div>
    </div>
  )
}
