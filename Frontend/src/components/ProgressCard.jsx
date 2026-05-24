import React from 'react'

export default function ProgressCard({title, value, meta}){
  return (
    <div className="card progress-stat">
      <div style={{fontSize:12,color:'var(--muted)'}}>{title}</div>
      <div style={{fontSize:20,fontWeight:800,marginTop:6}}>{value}</div>
      {meta && <div style={{marginTop:8,color:'var(--muted)',fontSize:13}}>{meta}</div>}
    </div>
  )
}
