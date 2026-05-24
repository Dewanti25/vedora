import React from 'react'

const tests = [
  {id:1,title:'Maths Chapter Test',status:'Upcoming',score:'—'},
  {id:2,title:'Physics Numericals',status:'Completed',score:'72%'},
  {id:3,title:'Chemistry Quick Test',status:'Completed',score:'90%'},
]

export default function TestsPanel(){
  return (
    <div className="card card-panel tests-panel">
      <div style={{display:'flex',justifyContent:'space-between',alignItems:'center'}}>
        <h4>Tests & Quizzes</h4>
        <div style={{color:'var(--muted)'}}>All Tests</div>
      </div>
      <div style={{marginTop:12,display:'flex',flexDirection:'column',gap:8}}>
        {tests.map(t=> (
          <div key={t.id} style={{display:'flex',justifyContent:'space-between',alignItems:'center'}}>
            <div>
              <div style={{fontWeight:800}}>{t.title}</div>
              <div style={{color:'var(--muted)',fontSize:13}}>{t.status}</div>
            </div>
            <div style={{fontWeight:900}}>{t.score}</div>
          </div>
        ))}
      </div>
    </div>
  )
}
