import React from 'react'

export default function BatchCard({batch, onJoin, joined=false}){
  const isFull = batch.current >= batch.max
  return (
    <div className="card batch-card">
      <div style={{display:'flex',justifyContent:'space-between',alignItems:'center'}}>
        <div>
          <div style={{fontWeight:800, fontSize:16}}>{batch.name}</div>
          <div style={{color:'var(--muted)',fontSize:13,marginTop:6}}>{batch.board} • Class {batch.class} • {batch.subject}</div>
        </div>
        <div style={{textAlign:'right'}}>
          <div style={{fontWeight:800}}>{batch.timing}</div>
          <div style={{color:'var(--muted)',fontSize:13,marginTop:6}}>{batch.current}/{batch.max} students</div>
        </div>
      </div>

      <div style={{display:'flex',justifyContent:'flex-end',marginTop:12}}>
        {joined ? (
          <button className="join-btn" disabled>Joined</button>
        ) : isFull ? (
          <button className="join-btn" disabled>Batch Full</button>
        ) : (
          <button className="join-btn" onClick={()=> onJoin(batch)}>Join</button>
        )}
      </div>
    </div>
  )
}
