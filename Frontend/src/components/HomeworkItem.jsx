import React from 'react'

export default function HomeworkItem({hw}){
  return (
    <div className="hw-item card">
      <div style={{display:'flex',alignItems:'center',gap:12}}>
        <div style={{width:48,height:48,background:'linear-gradient(90deg,var(--accent),var(--accent-2))',borderRadius:8,display:'flex',alignItems:'center',justifyContent:'center',fontWeight:700}}>{hw.type}</div>
        <div style={{flex:1}}>
          <div style={{fontWeight:700}}>{hw.title}</div>
          <div style={{fontSize:12,color:'var(--muted)'}}>{hw.size} • {hw.subject}</div>
        </div>
        <div style={{textAlign:'right'}}>
          <div style={{fontWeight:700}}>{hw.status}</div>
          <div style={{fontSize:12,color:'var(--muted)'}}>Due {hw.due}</div>
        </div>
      </div>
    </div>
  )
}
