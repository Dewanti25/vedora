import React from 'react'

function Avatar({name}){
  return <div style={{width:40,height:40,borderRadius:10,background:'linear-gradient(90deg,var(--accent),var(--accent-2))',display:'flex',alignItems:'center',justifyContent:'center',fontWeight:800}}>{name[0]}</div>
}

export default function StudentList(){
  const students = Array.from({length:12}).map((_,i)=>({id:i+1,name:`Student ${i+1}`,joined: true}))
  return (
    <div className="card" style={{height:'100%'}}>
      <div style={{fontWeight:800,marginBottom:8}}>Students ({students.length})</div>
      <div style={{display:'flex',flexDirection:'column',gap:8,overflowY:'auto',maxHeight:'calc(100% - 40px)'}}>
        {students.map(s=> (
          <div key={s.id} style={{display:'flex',alignItems:'center',gap:10,justifyContent:'space-between'}}>
            <div style={{display:'flex',alignItems:'center',gap:10}}>
              <Avatar name={s.name} />
              <div>
                <div style={{fontWeight:700}}>{s.name}</div>
                <div style={{fontSize:12,color:'var(--muted)'}}>Joined</div>
              </div>
            </div>
            <div style={{color:'var(--muted)',fontSize:12}}>●</div>
          </div>
        ))}
      </div>
    </div>
  )
}
