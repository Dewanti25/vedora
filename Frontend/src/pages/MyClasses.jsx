import React from 'react'
import { getJoinedClasses, removeJoinedClass } from '../utils/classService'

export default function MyClasses(){
  const [items, setItems] = React.useState(()=> getJoinedClasses())

  const handleEnter = (batch)=>{
    alert(`Entering class: ${batch.name} — next ${batch.timing}`)
  }

  const handleLeave = (id)=>{
    const updated = removeJoinedClass(id)
    setItems(updated)
  }

  return (
    <div>
      <h2>My Classes</h2>
      {items.length === 0 && <div style={{color:'var(--muted)'}}>You have not joined any classes yet.</div>}
      <div style={{marginTop:12,display:'grid',gridTemplateColumns:'repeat(2,1fr)',gap:12}}>
        {items.map(it=> (
          <div key={it.id} className="card">
            <div style={{display:'flex',justifyContent:'space-between',alignItems:'center'}}>
              <div>
                <div style={{fontWeight:800}}>{it.subject}</div>
                <div style={{color:'var(--muted)',fontSize:13}}>{it.board} • Class {it.class}</div>
                <div style={{color:'var(--muted)',fontSize:13,marginTop:6}}>{it.name}</div>
              </div>
              <div style={{textAlign:'right'}}>
                <div style={{fontWeight:800}}>{it.timing}</div>
                <div style={{color:'var(--muted)',fontSize:13}}>AI Teacher</div>
              </div>
            </div>

            <div style={{display:'flex',gap:8,justifyContent:'flex-end',marginTop:12}}>
              <button className="join-btn" onClick={()=> handleEnter(it)}>Join Class</button>
              <button style={{background:'transparent',color:'var(--muted)',border:0,cursor:'pointer'}} onClick={()=> handleLeave(it.id)}>Leave</button>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
