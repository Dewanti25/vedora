import React from 'react'

export default function CareerPanel(){
  const careers = [
    {id:1,title:'Data Scientist',match:92},
    {id:2,title:'Software Engineer',match:86},
    {id:3,title:'Research Analyst',match:78},
  ]
  return (
    <div className="card card-panel career-panel">
      <div style={{display:'flex',justifyContent:'space-between',alignItems:'center'}}>
        <h4>Career Guidance</h4>
        <div style={{color:'var(--muted)'}}>Find Fit</div>
      </div>
      <div style={{marginTop:12,display:'flex',flexDirection:'column',gap:8}}>
        {careers.map(c=> (
          <div key={c.id} style={{display:'flex',justifyContent:'space-between',alignItems:'center'}}>
            <div style={{display:'flex',alignItems:'center',gap:12}}>
              <div className="card-icon">🎯</div>
              <div>
                <div style={{fontWeight:800}}>{c.title}</div>
                <div style={{color:'var(--muted)',fontSize:13}}>{c.match}% match</div>
              </div>
            </div>
            <div><button className="btn btn-primary">View</button></div>
          </div>
        ))}
      </div>
    </div>
  )
}
