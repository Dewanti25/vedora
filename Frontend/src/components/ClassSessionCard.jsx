import React from 'react'

function formatDate(d){
  return d.toLocaleDateString()
}

export default function ClassSessionCard({session, onJoin}){
  const now = new Date()
  const start = new Date(session.startISO)
  const end = new Date(session.endISO)

  let status = 'Upcoming'
  if(now >= start && now <= end) status = 'Live'
  else if(now > end) status = 'Completed'

  return (
    <div className="card session-card">
      <div style={{display:'flex',justifyContent:'space-between',alignItems:'flex-start',gap:12}}>
        <div>
          <div style={{fontWeight:800,fontSize:16}}>{session.subject} • {session.batchName}</div>
          <div style={{color:'var(--muted)',marginTop:6}}>{session.chapter} — {session.topic}</div>
          <div style={{color:'var(--muted)',marginTop:8}}>{formatDate(start)} • {start.toLocaleTimeString([], {hour: '2-digit', minute:'2-digit'})} - {end.toLocaleTimeString([], {hour:'2-digit', minute:'2-digit'})}</div>
        </div>

        <div style={{textAlign:'right'}}>
          <div style={{display:'flex',alignItems:'center',gap:8,justifyContent:'flex-end'}}>
            <div className={`status-badge ${status.toLowerCase()}`}>{status}</div>
          </div>
          <div style={{marginTop:12}}>
            {status === 'Live' ? (
              <button className="join-btn" onClick={()=> onJoin(session)}>Join Now</button>
            ) : (
              <button className="join-btn" disabled>{status === 'Upcoming' ? 'Not Started' : 'Completed'}</button>
            )}
          </div>
        </div>
      </div>
    </div>
  )
}
