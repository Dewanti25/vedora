import React from 'react'

export default function StatCard({title, value, meta}){
  return (
    <div className="card stat-card">
      <div style={{fontSize:12,color:'var(--muted)'}}>{title}</div>
      <div style={{fontSize:22,fontWeight:800,marginTop:8}}>{value}</div>
      {meta && <div style={{marginTop:8,color:'var(--muted)',fontSize:12}}>{meta}</div>}
    </div>
  )
}
