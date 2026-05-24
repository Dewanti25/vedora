import React from 'react'
import BadgeCard from '../components/BadgeCard'

export default function Achievements(){
  const stats = {points:2450, level:12}
  const badges = [
    {id:1,icon:'🏆',title:'Quiz Master',description:'Score 90%+ in 5 quizzes',unlocked:true},
    {id:2,icon:'🔥',title:'Streak Master',description:'Study 10 days in a row',unlocked:true},
    {id:3,icon:'💡',title:'Concept Master',description:'Master 50 concepts',unlocked:false},
    {id:4,icon:'🎓',title:'Dedicated Learner',description:'Complete 100 lessons',unlocked:false},
  ]

  return (
    <div>
      <div style={{display:'flex',justifyContent:'space-between',alignItems:'center',marginBottom:12}}>
        <div>
          <div style={{fontSize:22,fontWeight:800}}>Achievements</div>
          <div style={{color:'var(--muted)'}}>Your gamified learning progress</div>
        </div>
      </div>

      <div className="stats-grid" style={{gridTemplateColumns:'repeat(2,1fr)',gap:12,marginBottom:12}}>
        <div className="card" style={{display:'flex',flexDirection:'column',alignItems:'flex-start',padding:16}}>
          <div style={{fontSize:12,color:'var(--muted)'}}>Total Points</div>
          <div style={{fontSize:28,fontWeight:800}}>{stats.points}</div>
        </div>
        <div className="card" style={{display:'flex',flexDirection:'column',alignItems:'flex-start',padding:16}}>
          <div style={{fontSize:12,color:'var(--muted)'}}>Level</div>
          <div style={{fontSize:28,fontWeight:800}}>{stats.level}</div>
        </div>
      </div>

      <div style={{marginBottom:12}}>
        <h3>Badges</h3>
        <div className="badges-grid">
          {badges.map(b=> <BadgeCard key={b.id} badge={b} />)}
        </div>
      </div>
    </div>
  )
}
