import React from 'react'

export default function AchievementsPanel(){
  const badges = [
    {id:1,title:'Quiz Master',desc:'Top scorer'},
    {id:2,title:'Streak 10',desc:'10 days streak'},
    {id:3,title:'Speed Reader',desc:'Finished 5 books'},
  ]
  return (
    <div className="card card-panel achievements-panel">
      <div style={{display:'flex',justifyContent:'space-between',alignItems:'center'}}>
        <h4>Achievements</h4>
        <div style={{color:'var(--muted)'}}>Level 12</div>
      </div>
      <div style={{marginTop:12,display:'flex',gap:10,alignItems:'center'}}>
        <div style={{flex:1}}>
          <div style={{fontSize:24,fontWeight:900}}>2450</div>
          <div style={{color:'var(--muted)'}}>Total Points</div>
        </div>
        <div style={{display:'flex',flexDirection:'column',gap:8}}>
          {badges.map(b=> (
            <div key={b.id} style={{display:'flex',alignItems:'center',gap:8}}>
              <div className="card-icon">🏆</div>
              <div>
                <div style={{fontWeight:800}}>{b.title}</div>
                <div style={{color:'var(--muted)',fontSize:12}}>{b.desc}</div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}
