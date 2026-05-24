import React, {useState} from 'react'
import { addTextbook, updateTextbook } from '../utils/textbookService'

const BOARDS = ['CBSE','ICSE','State Board']
const CLASSES = ['6th','7th','8th','9th','10th']
const SUBJECTS = ['Mathematics','Science','English','Social Science','Hindi','Computer']

export default function TextbookUploadForm({onCreate}){
  const [board,setBoard] = useState(BOARDS[0])
  const [cls,setCls] = useState(CLASSES[0])
  const [subject,setSubject] = useState(SUBJECTS[0])
  const [title,setTitle] = useState('')
  const [file,setFile] = useState(null)
  const [loading,setLoading] = useState(false)

  const handleFile = (e)=>{
    const f = e.target.files[0]
    if(f && f.type !== 'application/pdf'){
      alert('Only PDF allowed')
      return
    }
    setFile(f)
  }

  const handleSubmit = async (e)=>{
    e.preventDefault()
    if(!title.trim()||!file) return alert('Title and PDF required')
    const entry = {
      board, class: cls, subject, title, fileName: file.name, uploadDate: new Date().toISOString(), status: 'Processing'
    }
    setLoading(true)
    const items = addTextbook(entry)
    onCreate(items)

    // simulate processing delay then mark Ready
    setTimeout(()=>{
      const updated = {...entry, status: 'Ready'}
      updateTextbook({...updated, id: items[0].id})
      onCreate(getUpdated())
      setLoading(false)
    }, 1500 + Math.random()*2000)
  }

  function getUpdated(){
    // read latest
    try{ return JSON.parse(localStorage.getItem('vedora_textbooks') || '[]') }catch(e){return []}
  }

  return (
    <form onSubmit={handleSubmit} className="card">
      <h3>Upload Textbook</h3>
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
          <label style={{display:'block',fontWeight:700}}>Book Title</label>
          <input value={title} onChange={e=>setTitle(e.target.value)} style={{width:'100%',padding:8,marginTop:6}} placeholder="e.g. Mathematics - Class 8" />
        </div>

        <div style={{gridColumn:'1 / -1'}}>
          <label style={{display:'block',fontWeight:700}}>Upload PDF</label>
          <input type="file" accept="application/pdf" onChange={handleFile} style={{width:'100%',padding:8,marginTop:6}} />
          {file && <div style={{marginTop:8,color:'var(--muted)'}}>File: {file.name}</div>}
        </div>
      </div>

      <div style={{display:'flex',justifyContent:'flex-end',marginTop:12}}>
        <button className="join-btn" type="submit" disabled={loading}>{loading? 'Uploading...' : 'Upload'}</button>
      </div>
    </form>
  )
}
