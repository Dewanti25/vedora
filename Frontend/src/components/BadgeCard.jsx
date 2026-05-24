import React from 'react'

export default function BadgeCard({badge}){
  return (
    <div className={`badge-card ${badge.unlocked? 'unlocked':''}`}>
      <div className="badge-icon">{badge.icon}</div>
      <div style={{flex:1}}>
        <div style={{fontWeight:800}}>{badge.title}</div>
        <div style={{fontSize:13,color:'var(--muted)',marginTop:6}}>{badge.description}</div>
      </div>
      <div style={{marginLeft:12,textAlign:'right'}}>
        <div style={{fontWeight:800}}>{badge.unlocked? 'Unlocked' : 'Locked'}</div>
      </div>
    </div>
  )
}
