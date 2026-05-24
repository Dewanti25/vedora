import React from 'react'

export default function AIClassroomPanel(){
  return (
    <div className="card card-panel ai-classroom">
      <div style={{display:'flex',justifyContent:'space-between',alignItems:'center'}}>
        <h4>AI Classroom</h4>
        <div className="chip">Voice Mode</div>
      </div>
      <div style={{display:'flex',gap:12,marginTop:12}}>
        <div style={{flex:1}}>
          <div className="chat-window">
            <div className="messages">
              <div className="message message-ai"><div className="bubble">Welcome to AI Classroom — today we'll cover photosynthesis.</div></div>
              <div className="message message-user"><div className="bubble">Can you explain light reactions?</div></div>
            </div>
          </div>
          <div style={{display:'flex',gap:8,marginTop:8}}>
            <input placeholder="Ask the AI teacher" style={{flex:1,padding:10,borderRadius:10,border:'1px solid rgba(255,255,255,0.04)',background:'rgba(255,255,255,0.02)',color:'inherit'}} />
            <button className="icon-btn">Ask</button>
          </div>
        </div>
        <div style={{width:200,display:'flex',flexDirection:'column',gap:8}}>
          <div style={{fontWeight:800}}>This Session</div>
          <div style={{color:'var(--muted)'}}>Topic: Photosynthesis</div>
          <div style={{color:'var(--muted)'}}>Next: Q&A in 10 mins</div>
          <div style={{marginTop:12}}>
            <button className="btn btn-primary">Join Live</button>
          </div>
        </div>
      </div>
    </div>
  )
}
