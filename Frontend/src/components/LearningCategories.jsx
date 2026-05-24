import React from 'react'

const items = [
  {id:1,title:'Play Way',desc:'Nursery - KG',icon:'🐯', badge: 'Popular', color: 'purple'},
  {id:2,title:'Schooling',desc:'1st - 12th',icon:'🎒', badge: 'Core', color: 'blue'},
  {id:3,title:'College',desc:'Any Branch',icon:'🎓', color: 'teal'},
  {id:4,title:'Government Job',desc:'SSC, Banking, UPSC',icon:'🏛️', badge: 'Top', color: 'indigo'},
  {id:5,title:'Coding Skills',desc:'Python, Java, C++',icon:'💻', badge: 'New', color: 'cyan'},
  {id:6,title:'Interview Trainer',desc:'Mock interviews',icon:'🧑‍💼', color: 'rose'},
  {id:7,title:'Spoken English',desc:'Practice & grammar',icon:'🗣️', color: 'amber'},
  {id:8,title:'AI Career Counselor',desc:'One-to-one guidance',icon:'🧭', color: 'violet'},
]

export default function LearningCategories(){
  return (
    <div className="learning-strip-card">
      <div style={{display:'flex',justifyContent:'space-between',alignItems:'center',marginBottom:8}}>
        <h3>Choose Your Learning Model</h3>
        <div style={{color:'var(--muted)'}}>View All →</div>
      </div>

      <div className="learning-strip">
        {items.map(it=> (
          <div key={it.id} className={`learning-card small lc-${it.color || 'default'}`} role="button" onClick={()=>alert(`${it.title} clicked (placeholder)`)}>
            <div className="learning-card-top">
              <div className="learning-icon">{it.icon}</div>
              {it.badge && <div className="learning-badge">{it.badge}</div>}
            </div>
            <div style={{fontWeight:800,marginTop:10}}>{it.title}</div>
            <div style={{fontSize:13,color:'var(--muted)',marginTop:6}}>{it.desc}</div>
            <div className="learning-cta">Explore →</div>
          </div>
        ))}
      </div>
    </div>
  )
}
