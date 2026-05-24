import React from 'react'

export default function ProgressPanel(){
  const stats = {studyTime:'68h 20m',lessons:245,accuracy:82}
  return (
    <div className="card card-panel progress-panel">
      <div style={{display:'flex',justifyContent:'space-between',alignItems:'center'}}>
        <h4>Progress</h4>
        <div style={{color:'var(--muted)'}}>This Month</div>
      </div>
      <div style={{marginTop:12}}>
        <div style={{display:'flex',justifyContent:'space-between'}}>
          <div style={{color:'var(--muted)'}}>Study Time</div>
          <div style={{fontWeight:800}}>{stats.studyTime}</div>
        </div>
        <div style={{display:'flex',justifyContent:'space-between',marginTop:8}}>
          <div style={{color:'var(--muted)'}}>Lessons</div>
          <div style={{fontWeight:800}}>{stats.lessons}</div>
        </div>
        <div style={{display:'flex',justifyContent:'space-between',marginTop:8}}>
          <div style={{color:'var(--muted)'}}>Accuracy</div>
          <div style={{fontWeight:800}}>{stats.accuracy}%</div>
        </div>
        <div style={{marginTop:12}} className="progress-bar"><div className="progress-fill" style={{width:`${stats.accuracy}%`}} /></div>
      </div>
    </div>
  )
}
