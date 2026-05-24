import React from 'react'
import ProgressCard from '../components/ProgressCard'
import ChartCard from '../components/ChartCard'

export default function Progress(){
  const stats = {
    study_time: '24h 36m',
    lessons_completed: 245,
    accuracy: '82%',
    current_streak: '12 Days'
  }

  const subjects = [
    {name:'Mathematics', percent:85},
    {name:'Physics', percent:70},
    {name:'Chemistry', percent:65},
    {name:'Programming', percent:90},
    {name:'English', percent:60},
  ]

  return (
    <div>
      <div style={{display:'flex',justifyContent:'space-between',alignItems:'center',marginBottom:12}}>
        <div>
          <div style={{fontSize:22,fontWeight:800}}>Progress Analytics</div>
          <div style={{color:'var(--muted)'}}>Your learning metrics and insights</div>
        </div>
      </div>

      <div className="stats-grid" style={{marginBottom:12}}>
        <ProgressCard title="Study Time" value={stats.study_time} />
        <ProgressCard title="Lessons Completed" value={stats.lessons_completed} />
        <ProgressCard title="Accuracy" value={stats.accuracy} />
        <ProgressCard title="Current Streak" value={stats.current_streak} />
      </div>

      <div className="section-grid">
        <ChartCard title="Weekly Activity" />

        <div className="card">
          <h3>Subject Progress</h3>
          <div style={{display:'flex',flexDirection:'column',gap:10,marginTop:8}}>
            {subjects.map(s=> (
              <div key={s.name} style={{display:'flex',alignItems:'center',justifyContent:'space-between',gap:8}}>
                <div style={{flex:1}}>
                  <div style={{fontWeight:700}}>{s.name}</div>
                  <div style={{height:8,background:'rgba(255,255,255,0.03)',borderRadius:8,overflow:'hidden',marginTop:6}}><div style={{width:`${s.percent}%`,height:8,background:'linear-gradient(90deg,var(--accent),var(--accent-2))'}} /></div>
                </div>
                <div style={{width:48,textAlign:'right',fontWeight:800}}>{s.percent}%</div>
              </div>
            ))}
          </div>
        </div>

        <div className="card">
          <h3>AI Insight</h3>
          <div style={{marginTop:8,color:'var(--muted)'}}>You are weak in Quadratic Equations. Start revision module.</div>
          <button style={{marginTop:12,background:'linear-gradient(90deg,var(--accent),var(--accent-2))',border:0,color:'#fff',padding:'8px 12px',borderRadius:8}}>Start Revision</button>
        </div>
      </div>
    </div>
  )
}
