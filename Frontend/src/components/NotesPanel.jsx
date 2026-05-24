import React from 'react'

const notes = [
  {id:1,title:'Trigonometry Formulas',subject:'Mathematics',size:'120 KB'},
  {id:2,title:'Work Energy Power',subject:'Physics',size:'98 KB'},
  {id:3,title:'Chemical Bonding Notes',subject:'Chemistry',size:'144 KB'},
]

export default function NotesPanel(){
  return (
    <div className="card card-panel notes-panel">
      <div style={{display:'flex',justifyContent:'space-between',alignItems:'center'}}>
        <h4>Notes Library</h4>
        <div style={{color:'var(--muted)'}}>Download</div>
      </div>
      <div style={{marginTop:12,display:'flex',flexDirection:'column',gap:8}}>
        {notes.map(n=> (
          <div key={n.id} className="note-card">
            <div style={{display:'flex',alignItems:'center',gap:12}}>
              <div className="card-icon">📄</div>
              <div>
                <div style={{fontWeight:800}}>{n.title}</div>
                <div style={{color:'var(--muted)',fontSize:13}}>{n.subject} • {n.size}</div>
              </div>
            </div>
            <div style={{marginLeft:'auto'}}>
              <button className="btn btn-ghost">Download</button>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}
