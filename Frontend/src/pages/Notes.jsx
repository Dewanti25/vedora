import React, {useState} from 'react'
import NoteCard from '../components/NoteCard'

const dummyNotes = [
  {id:1,title:'Trigonometry Formulas',subject:'Mathematics',type:'PDF',size:'480 KB'},
  {id:2,title:'Physics - Work Energy Power',subject:'Physics',type:'PDF',size:'1.1 MB'},
  {id:3,title:'Chemical Bonding Notes',subject:'Chemistry',type:'DOC',size:'760 KB'},
  {id:4,title:'Human Heart Diagram',subject:'Biology',type:'PNG',size:'320 KB'},
  {id:5,title:'Input Output in Python',subject:'Computer Science',type:'PDF',size:'220 KB'},
]

export default function Notes(){
  const [q,setQ] = useState('')
  const [subject,setSubject] = useState('All')
  const [notes,setNotes] = useState(dummyNotes)

  const subjects = ['All', ...Array.from(new Set(dummyNotes.map(n=>n.subject)))]

  function filtered(){
    return notes.filter(n=>{
      if(subject !== 'All' && n.subject !== subject) return false
      if(q && !n.title.toLowerCase().includes(q.toLowerCase())) return false
      return true
    })
  }

  function handleDownload(note){
    // UI-only: show browser download placeholder (no backend)
    alert(`Download: ${note.title} (UI only)`) 
  }

  return (
    <div>
      <div style={{display:'flex',justifyContent:'space-between',alignItems:'center',marginBottom:12}}>
        <h3>Notes Library</h3>
        <div style={{display:'flex',gap:8}}>
          <input placeholder="Search notes..." value={q} onChange={e=>setQ(e.target.value)} style={{padding:8,borderRadius:8,border:'1px solid rgba(255,255,255,0.04)',background:'rgba(255,255,255,0.02)',color:'inherit'}} />
          <select value={subject} onChange={e=>setSubject(e.target.value)} style={{padding:8,borderRadius:8,border:'1px solid rgba(255,255,255,0.04)',background:'rgba(255,255,255,0.02)',color:'inherit'}}>
            {subjects.map(s=> <option key={s} value={s}>{s}</option>)}
          </select>
        </div>
      </div>

      <div className="note-list" style={{display:'grid',gap:10}}>
        {filtered().map(n=> <NoteCard key={n.id} note={n} onDownload={handleDownload} />)}
      </div>
    </div>
  )
}
