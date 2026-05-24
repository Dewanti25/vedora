import React, {useState, useMemo} from 'react'
import BatchCard from './BatchCard'

const BOARDS = ['CBSE','ICSE','State Board']
const CLASSES = ['6th','7th','8th','9th','10th']
const SUBJECTS = ['Mathematics','Science','English','Social Science','Hindi','Computer']

function makeDummyBatches(board, cls, subject){
  // create 4 dummy batches with different times and student counts
  const samples = [
    {name: `${subject} - Morning Batch`, timing: '08:00 - 09:30'},
    {name: `${subject} - Afternoon Batch`, timing: '14:00 - 15:30'},
    {name: `${subject} - Evening Batch`, timing: '18:00 - 19:30'},
    {name: `${subject} - Weekend`, timing: 'Sat 10:00 - 12:00'},
  ]
  return samples.map((s,i)=>({
    id: `${board}-${cls}-${subject}-${i}`,
    name: s.name,
    timing: s.timing,
    board,
    class: cls,
    subject,
    current: Math.floor(Math.random()*12)+1,
    max: 15,
  }))
}

export default function CurriculumSelector(){
  const [board, setBoard] = useState(null)
  const [cls, setCls] = useState(null)
  const [subject, setSubject] = useState(null)

  const batches = useMemo(()=>{
    if(!board || !cls || !subject) return []
    return makeDummyBatches(board, cls, subject)
  },[board,cls,subject])

  // track joined ids so UI updates immediately
  const [joinedIds, setJoinedIds] = React.useState(()=>{
    try{ const raw = localStorage.getItem('vedora_joined_classes'); return raw? JSON.parse(raw).map(i=>i.id): [] }catch(e){return []}
  })

  const handleJoin = (batch)=>{
    if(batch.current >= batch.max) return alert('Batch is full')
    // add to localStorage
    try{
      const raw = localStorage.getItem('vedora_joined_classes')
      const items = raw? JSON.parse(raw): []
      if(!items.find(i=> i.id===batch.id)){
        items.push(batch)
        localStorage.setItem('vedora_joined_classes', JSON.stringify(items))
        setJoinedIds(items.map(i=>i.id))
        alert(`Joined: ${batch.name}`)
      }else{
        alert('Already joined')
      }
    }catch(e){
      alert('Could not join (storage error)')
    }
  }

  return (
    <div className="card">
      <h2>Choose Board, Class & Subject</h2>

      <div style={{marginTop:12}}>
        <div style={{marginBottom:8,fontWeight:700}}>Select Board</div>
        <div className="curriculum-grid">
          {BOARDS.map(b=> (
            <button key={b} className={`board-card ${board===b? 'active':''}`} onClick={()=>setBoard(b)}>{b}</button>
          ))}
        </div>
      </div>

      <div style={{marginTop:16}}>
        <div style={{marginBottom:8,fontWeight:700}}>Select Class</div>
        <div className="curriculum-grid">
          {CLASSES.map(c=> (
            <button key={c} className={`class-card ${cls===c? 'active':''}`} onClick={()=>setCls(c)}>{c}</button>
          ))}
        </div>
      </div>

      <div style={{marginTop:16}}>
        <div style={{marginBottom:8,fontWeight:700}}>Select Subject</div>
        <div className="curriculum-grid">
          {SUBJECTS.map(s=> (
            <button key={s} className={`subject-card ${subject===s? 'active':''}`} onClick={()=>setSubject(s)}>{s}</button>
          ))}
        </div>
      </div>

      <div style={{marginTop:18}}>
        <div style={{display:'flex',justifyContent:'space-between',alignItems:'center'}}>
          <div style={{fontWeight:700}}>Available Batches</div>
          <div style={{color:'var(--muted)'}}>{batches.length} found</div>
        </div>

        <div className="batches-grid" style={{marginTop:12}}>
          {batches.length === 0 && (
            <div style={{color:'var(--muted)'}}>Select board, class and subject to see batches.</div>
          )}
          {batches.map(b=> (
            <BatchCard key={b.id} batch={b} onJoin={handleJoin} joined={joinedIds.includes(b.id)} />
          ))}
        </div>
      </div>
    </div>
  )
}
