import React from 'react'

export default function ChartCard({title}){
  return (
    <div className="card chart-card">
      <div style={{display:'flex',justifyContent:'space-between',alignItems:'center'}}>
        <div style={{fontWeight:800}}>{title}</div>
      </div>
      <div style={{height:160,display:'flex',alignItems:'center',justifyContent:'center',color:'var(--muted)'}}>Weekly activity bar chart (placeholder)</div>
    </div>
  )
}
