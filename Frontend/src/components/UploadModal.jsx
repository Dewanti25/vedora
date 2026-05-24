import React, {useState} from 'react'

export default function UploadModal({visible,onClose,onSubmit}){
  const [subject,setSubject] = useState('Mathematics')
  const [title,setTitle] = useState('')
  const [file,setFile] = useState(null)

  function submit(e){
    e.preventDefault()
    onSubmit({subject,title,file})
    setTitle(''); setFile(null); onClose()
  }

  if(!visible) return null
  return (
    <div className="modal-backdrop">
      <div className="modal card">
        <h3>Upload Homework</h3>
        <form onSubmit={submit} style={{display:'flex',flexDirection:'column',gap:10}}>
          <label>
            Subject
            <select value={subject} onChange={e=>setSubject(e.target.value)}>
              <option>Mathematics</option>
              <option>Physics</option>
              <option>Chemistry</option>
              <option>English</option>
            </select>
          </label>
          <label>
            Homework Title
            <input value={title} onChange={e=>setTitle(e.target.value)} placeholder="e.g. Maths Assignment 2" />
          </label>
          <label>
            File
            <input type="file" onChange={e=>setFile(e.target.files[0])} />
          </label>
          <div style={{display:'flex',gap:8,justifyContent:'flex-end',marginTop:8}}>
            <button type="button" className="icon-btn" onClick={onClose}>Cancel</button>
            <button type="submit" className="send-btn">Submit</button>
          </div>
        </form>
      </div>
    </div>
  )
}
