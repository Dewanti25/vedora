import React from 'react'

const sample = [
  {id:1,title:'Maths Assignment 2',due:'Tomorrow',status:'Submitted'},
  {id:2,title:'Physics Numericals',due:'In 2 days',status:'Pending'},
  {id:3,title:'Chemistry Lab Report',due:'May 27',status:'Pending'},
]

export default function HomeworkPanel(){
  return (
    <div className="card card-panel homework-panel">
      <div style={{display:'flex',justifyContent:'space-between',alignItems:'center'}}>
        <h4>Homework</h4>
        <div style={{color:'var(--muted)'}}>View All</div>
      </div>
      <div style={{marginTop:12,display:'flex',flexDirection:'column',gap:10}}>
        {sample.map(s=> (
          <div key={s.id} className="hw-item">
            <div style={{flex:1}}>
              <div style={{fontWeight:800}}>{s.title}</div>
              <div style={{color:'var(--muted)',fontSize:13}}>{s.due}</div>
            </div>
            <div style={{textAlign:'right'}}>
              <div style={{fontWeight:800}}>{s.status}</div>
            </div>
          </div>
        ))}
      </div>
      <div style={{marginTop:12,textAlign:'center'}}>
        <button className="btn btn-primary">Upload Homework</button>
      </div>
    </div>
  )
}
