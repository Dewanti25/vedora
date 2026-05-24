import React, {useState} from 'react'
const BOARDS = ['CBSE','ICSE','State Board']
const CLASSES = ['6th','7th','8th','9th','10th']
const SUBJECTS = ['Mathematics','Science','English','Social Science','Hindi','Computer']

export default function AdminBatchForm({onCreate}){
  const [board,setBoard] = useState(BOARDS[0])
  const [cls,setCls] = useState(CLASSES[0])
  const [subject,setSubject] = useState(SUBJECTS[0])
  const [name,setName] = useState('')
  const [max,setMax] = useState(15)
  const [startDate,setStartDate] = useState('')
  const [days,setDays] = useState([])
  const [startTime,setStartTime] = useState('16:00')
  const [endTime,setEndTime] = useState('17:30')

  const toggleDay = (d)=>{
    setDays(prev => prev.includes(d) ? prev.filter(x=>x!==d) : [...prev,d])
  }

  const handleSubmit = (e)=>{
    e.preventDefault()
    if(!name.trim()) return alert('Batch name required')
    const batch = {
      board, class: cls, subject, name, max: Number(max || 15), startDate, days, startTime, endTime, students: 0
    }
    onCreate(batch)
    // reset minimal
    setName('')
    setDays([])
  }

  return (
    <form onSubmit={handleSubmit} className="card">
      <h3>Create Batch</h3>
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:12,marginTop:12}}>
        <div>
          <label style={{display:'block',fontWeight:700}}>Board</label>
          <select value={board} onChange={e=>setBoard(e.target.value)} style={{width:'100%',padding:8,marginTop:6}}>
            {BOARDS.map(b=> <option key={b} value={b}>{b}</option>)}
          </select>
        </div>
        <div>
          <label style={{display:'block',fontWeight:700}}>Class/Grade</label>
          <select value={cls} onChange={e=>setCls(e.target.value)} style={{width:'100%',padding:8,marginTop:6}}>
            {CLASSES.map(c=> <option key={c} value={c}>{c}</option>)}
          </select>
        </div>

        <div>
          <label style={{display:'block',fontWeight:700}}>Subject</label>
          <select value={subject} onChange={e=>setSubject(e.target.value)} style={{width:'100%',padding:8,marginTop:6}}>
            {SUBJECTS.map(s=> <option key={s} value={s}>{s}</option>)}
          </select>
        </div>
        <div>
          <label style={{display:'block',fontWeight:700}}>Batch Name</label>
          <input value={name} onChange={e=>setName(e.target.value)} style={{width:'100%',padding:8,marginTop:6}} placeholder="e.g. Evening Batch" />
        </div>

        <div>
          <label style={{display:'block',fontWeight:700}}>Max Students</label>
          <input type="number" value={max} onChange={e=>setMax(e.target.value)} style={{width:'100%',padding:8,marginTop:6}} />
        </div>
        <div>
          <label style={{display:'block',fontWeight:700}}>Start Date</label>
          <input type="date" value={startDate} onChange={e=>setStartDate(e.target.value)} style={{width:'100%',padding:8,marginTop:6}} />
        </div>

        <div style={{gridColumn:'1 / -1'}}>
          <label style={{display:'block',fontWeight:700}}>Class Days</label>
          <div style={{display:'flex',gap:8,flexWrap:'wrap',marginTop:6}}>
            {['Mon','Tue','Wed','Thu','Fri','Sat','Sun'].map(d=> (
              <button type="button" key={d} onClick={()=>toggleDay(d)} className={days.includes(d)?'board-card active':'board-card'}>{d}</button>
            ))}
          </div>
        </div>

        <div>
          <label style={{display:'block',fontWeight:700}}>Start Time</label>
          <input type="time" value={startTime} onChange={e=>setStartTime(e.target.value)} style={{width:'100%',padding:8,marginTop:6}} />
        </div>
        <div>
          <label style={{display:'block',fontWeight:700}}>End Time</label>
          <input type="time" value={endTime} onChange={e=>setEndTime(e.target.value)} style={{width:'100%',padding:8,marginTop:6}} />
        </div>
      </div>

      <div style={{display:'flex',justifyContent:'flex-end',marginTop:12}}>
        <button className="join-btn" type="submit">Create Batch</button>
      </div>
    </form>
  )
}
