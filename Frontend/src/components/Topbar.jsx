import React from 'react'

export default function Topbar({me}){
  const name = me?.email?.split('@')[0] || 'Aarav'
  return (
    <div className="topbar">
      <div className="welcome">
        <div>
          <div style={{fontSize:18,fontWeight:700}}>Good Morning, {name}! 👋</div>
          <div style={{fontSize:12,color:'var(--muted)'}}>Let's learn, grow and achieve your dreams today.</div>
        </div>
      </div>

      <div className="search">
        <input placeholder="Search anything..." />
      </div>

      <div className="controls">
        <div className="mini-stat">
          <div style={{fontSize:12,color:'var(--muted)'}}>Overall Progress</div>
          <div style={{fontWeight:800}}>75%</div>
        </div>
        <div className="mini-stat">
          <div style={{fontSize:12,color:'var(--muted)'}}>Study Time</div>
          <div style={{fontWeight:800}}>24h 36m</div>
        </div>
        <div className="avatar">A</div>
      </div>
    </div>
  )
}
