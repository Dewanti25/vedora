import React, {useState} from 'react'
import CareerModal from '../components/CareerModal'

export default function Career(){
  const [showModal,setShowModal] = useState(false)

  const skills = [
    {name:'Analytical Thinking', level: 88},
    {name:'Logical Reasoning', level: 82},
    {name:'Problem Solving', level: 90},
  ]

  const matches = [
    {title:'Data Scientist', score:92, icon:'DS'},
    {title:'Software Engineer', score:89, icon:'SE'},
    {title:'Research Analyst', score:85, icon:'RA'},
  ]

  return (
    <div>
      <div style={{display:'flex',justifyContent:'space-between',alignItems:'center',marginBottom:12}}>
        <div>
          <div style={{fontSize:22,fontWeight:800}}>Career Guidance</div>
          <div style={{color:'var(--muted)'}}>AI-driven career recommendations and report</div>
        </div>
        <div>
          <button className="send-btn" onClick={()=>setShowModal(true)}>View Full Career Report</button>
        </div>
      </div>

      <div className="section-grid">
        <div className="card">
          <h3>AI Career Prediction</h3>
          <div style={{display:'flex',gap:12,marginTop:8}}>
            <div style={{flex:1}}>
              <div style={{fontWeight:800}}>Top Skills</div>
              <div style={{marginTop:8,display:'flex',flexDirection:'column',gap:8}}>
                {skills.map(s=> (
                  <div key={s.name} style={{display:'flex',alignItems:'center',justifyContent:'space-between'}}>
                    <div style={{flex:1}}>
                      <div style={{fontWeight:700}}>{s.name}</div>
                      <div style={{height:8,background:'rgba(255,255,255,0.03)',borderRadius:8,overflow:'hidden',marginTop:6}}><div style={{width:`${s.level}%`,height:8,background:'linear-gradient(90deg,var(--accent),var(--accent-2))'}} /></div>
                    </div>
                    <div style={{width:48,textAlign:'right',fontWeight:800}}>{s.level}%</div>
                  </div>
                ))}
              </div>
            </div>
            <div style={{width:240}}>
              <div style={{fontWeight:800}}>Top Career Matches</div>
              <div style={{display:'flex',flexDirection:'column',gap:8,marginTop:8}}>
                {matches.map(m=> (
                  <div key={m.title} style={{display:'flex',alignItems:'center',justifyContent:'space-between',gap:8}}>
                    <div style={{display:'flex',alignItems:'center',gap:8}}>
                      <div style={{width:40,height:40,borderRadius:8,background:'linear-gradient(90deg,var(--accent),var(--accent-2))',display:'flex',alignItems:'center',justifyContent:'center',fontWeight:800}}>{m.icon}</div>
                      <div>
                        <div style={{fontWeight:700}}>{m.title}</div>
                        <div style={{fontSize:12,color:'var(--muted)'}}>{m.score}% match</div>
                      </div>
                    </div>
                    <div>
                      <button className="icon-btn" onClick={()=>setShowModal(true)}>Details</button>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>

        <div className="card">
          <h3>Career Snapshot</h3>
          <div style={{marginTop:8,color:'var(--muted)'}}>This section will show a short summary of your strengths, learning paths and recommended steps.</div>
        </div>

        <div className="card">
          <h3>Quick Actions</h3>
          <div style={{display:'flex',flexDirection:'column',gap:8,marginTop:8}}>
            <button className="icon-btn">Explore Careers</button>
            <button className="icon-btn">Generate Resume</button>
          </div>
        </div>
      </div>

      <CareerModal visible={showModal} onClose={()=>setShowModal(false)} />
    </div>
  )
}
