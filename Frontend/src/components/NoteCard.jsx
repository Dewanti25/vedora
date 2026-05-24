import React from 'react'

export default function NoteCard({note, onDownload}){
  return (
    <div className="note-card card">
      <div style={{display:'flex',alignItems:'center',gap:12}}>
        <div style={{width:56,height:56,borderRadius:10,background:'linear-gradient(90deg,var(--accent),var(--accent-2))',display:'flex',alignItems:'center',justifyContent:'center',fontWeight:800}}>{note.type}</div>
        <div style={{flex:1}}>
          <div style={{fontWeight:800}}>{note.title}</div>
          <div style={{fontSize:12,color:'var(--muted)'}}>{note.subject} • {note.size}</div>
        </div>
        <div style={{display:'flex',flexDirection:'column',alignItems:'flex-end',gap:8}}>
          <button className="icon-btn" onClick={()=>onDownload && onDownload(note)} title="Download">⬇</button>
          <div style={{fontSize:12,color:'var(--muted)'}}>{note.type}</div>
        </div>
      </div>
    </div>
  )
}
