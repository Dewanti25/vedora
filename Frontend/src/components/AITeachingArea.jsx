import React, {useEffect, useState} from 'react'

export default function AITeachingArea({session}){
  const teachingLines = [
    `Today we'll cover ${session.topic} from ${session.chapter}.`,
    'Remember to solve the example problems at the end of the chapter.',
    'Pause the video and try the practice question shown on screen.',
    'I will explain step-by-step and you can ask doubts in chat.'
  ]

  const [index, setIndex] = useState(0)
  const [lines, setLines] = useState([teachingLines[0]])

  useEffect(()=>{
    const t = setInterval(()=>{
      setIndex(i=>{
        const next = i+1
        if(next < teachingLines.length){
          setLines(l=> [...l, teachingLines[next]])
        }
        return next
      })
    }, 3500)
    return ()=> clearInterval(t)
  },[])

  return (
    <div className="card" style={{height:'100%',display:'flex',flexDirection:'column'}}>
      <div style={{fontWeight:800,marginBottom:8}}>{session.subject} — {session.topic}</div>
      <div style={{flex:1,overflowY:'auto',color:'var(--muted)'}}>
        {lines.map((l,idx)=> (
          <div key={idx} style={{marginBottom:10,background:'rgba(255,255,255,0.01)',padding:10,borderRadius:8}}>{l}</div>
        ))}
      </div>
      <div style={{display:'flex',gap:8,marginTop:8}}>
        <button className="join-btn">Raise Hand</button>
        <button className="join-btn">Submit Answer</button>
        <button style={{background:'transparent',border:0,color:'var(--muted)'}}>Leave Class</button>
      </div>
    </div>
  )
}
