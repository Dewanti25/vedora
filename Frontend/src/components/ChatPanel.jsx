import React, {useState, useEffect, useRef} from 'react'

export default function ChatPanel({session}){
  const [messages, setMessages] = useState([
    {id:1, sender:'AI', text:`Welcome to ${session.subject} — ${session.topic}. Ask your doubts anytime.`}
  ])
  const [input, setInput] = useState('')
  const listRef = useRef()

  useEffect(()=>{
    if(listRef.current) listRef.current.scrollTop = listRef.current.scrollHeight
  },[messages])

  const sendQuestion = (type='ask')=>{
    if(!input.trim()) return
    const id = Date.now()
    const newMsg = {id, sender:'You', text: input}
    setMessages(m=> [...m, newMsg])
    setInput('')

    // AI dummy response after short delay
    setTimeout(()=>{
      setMessages(m=> [...m, {id: id+1, sender:'AI', text: `AI: (auto) Answer to '${newMsg.text}' — this is a placeholder response.`}])
    }, 900 + Math.random()*800)
  }

  return (
    <div className="card" style={{display:'flex',flexDirection:'column',height:'100%'}}>
      <div style={{fontWeight:800,marginBottom:8}}>Class Chat</div>
      <div ref={listRef} style={{flex:1,overflowY:'auto',display:'flex',flexDirection:'column',gap:8,paddingRight:6}}>
        {messages.map(m=> (
          <div key={m.id} style={{alignSelf: m.sender==='You' ? 'flex-end':'flex-start',maxWidth:'78%'}}>
            <div className={m.sender==='AI' ? 'card' : 'card'} style={{padding:8}}>
              <div style={{fontSize:13,fontWeight:700}}>{m.sender}</div>
              <div style={{marginTop:6,color:'var(--muted)'}}>{m.text}</div>
            </div>
          </div>
        ))}
      </div>

      <div style={{marginTop:8,display:'flex',gap:8}}>
        <input value={input} onChange={(e)=>setInput(e.target.value)} placeholder="Type your question..." style={{flex:1,padding:10,borderRadius:8,border:'1px solid rgba(255,255,255,0.04)',background:'rgba(255,255,255,0.02)',color:'inherit'}}/>
        <button className="join-btn" onClick={()=> sendQuestion('ask')}>Ask Doubt</button>
      </div>
    </div>
  )
}
