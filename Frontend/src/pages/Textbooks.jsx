import React from 'react'
import TextbookUploadForm from '../components/TextbookUploadForm'
import { getTextbooks, removeTextbook } from '../utils/textbookService'

function formatDate(iso){
  try{ return new Date(iso).toLocaleString() }catch(e){return iso}
}

export default function Textbooks(){
  const [items, setItems] = React.useState(()=> getTextbooks())

  const handleCreate = (list)=> setItems(list)
  const handleRemove = (id)=>{
    if(!confirm('Remove textbook?')) return
    const res = removeTextbook(id)
    setItems(res)
  }

  return (
    <div>
      <h2>Textbook Uploads</h2>
      <div style={{display:'grid',gridTemplateColumns:'380px 1fr',gap:12,marginTop:12}}>
        <TextbookUploadForm onCreate={handleCreate} />

        <div className="card">
          <h3>Uploaded Textbooks</h3>
          <div style={{marginTop:12,overflowX:'auto'}}>
            <table style={{width:'100%',borderCollapse:'collapse'}}>
              <thead>
                <tr style={{textAlign:'left',color:'var(--muted)'}}>
                  <th>Book Title</th>
                  <th>Board</th>
                  <th>Class</th>
                  <th>Subject</th>
                  <th>File Name</th>
                  <th>Upload Date</th>
                  <th>Status</th>
                  <th></th>
                </tr>
              </thead>
              <tbody>
                {items.map(it=> (
                  <tr key={it.id} style={{borderTop:'1px solid rgba(255,255,255,0.03)'}}>
                    <td style={{padding:'10px 8px'}}>{it.title}</td>
                    <td style={{padding:'10px 8px'}}>{it.board}</td>
                    <td style={{padding:'10px 8px'}}>{it.class}</td>
                    <td style={{padding:'10px 8px'}}>{it.subject}</td>
                    <td style={{padding:'10px 8px'}}>{it.fileName}</td>
                    <td style={{padding:'10px 8px'}}>{formatDate(it.uploadDate)}</td>
                    <td style={{padding:'10px 8px'}}>{it.status}</td>
                    <td style={{padding:'10px 8px',textAlign:'right'}}>
                      <button style={{background:'transparent',border:0,color:'var(--muted)',cursor:'pointer'}} onClick={()=> handleRemove(it.id)}>Remove</button>
                    </td>
                  </tr>
                ))}
                {items.length === 0 && (
                  <tr><td colSpan={8} style={{padding:12,color:'var(--muted)'}}>No textbooks uploaded yet.</td></tr>
                )}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  )
}
