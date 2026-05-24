import React from 'react'
import AdminBatchForm from '../components/AdminBatchForm'
import { getBatches, addBatch, removeBatch } from '../utils/batchService'

function Timing({b}){
  return <div>{b.startTime} - {b.endTime} ({b.days.join(',')})</div>
}

export default function AdminBatches(){
  const [batches, setBatches] = React.useState(()=> getBatches())

  const handleCreate = (batch)=>{
    const res = addBatch(batch)
    setBatches(res)
  }

  const handleRemove = (id)=>{
    if(!confirm('Remove batch?')) return
    const res = removeBatch(id)
    setBatches(res)
  }

  return (
    <div>
      <h2>Manage Batches</h2>
      <div style={{display:'grid',gridTemplateColumns:'380px 1fr',gap:12,marginTop:12}}>
        <AdminBatchForm onCreate={handleCreate} />

        <div className="card">
          <h3>Created Batches</h3>
          <div style={{marginTop:12,overflowX:'auto'}}>
            <table style={{width:'100%',borderCollapse:'collapse'}}>
              <thead>
                <tr style={{textAlign:'left',color:'var(--muted)'}}>
                  <th>Batch Name</th>
                  <th>Board</th>
                  <th>Class</th>
                  <th>Subject</th>
                  <th>Timing</th>
                  <th>Students</th>
                  <th>Status</th>
                  <th></th>
                </tr>
              </thead>
              <tbody>
                {batches.map(b=> (
                  <tr key={b.id} style={{borderTop:'1px solid rgba(255,255,255,0.03)'}}>
                    <td style={{padding:'10px 8px'}}>{b.name}</td>
                    <td style={{padding:'10px 8px'}}>{b.board}</td>
                    <td style={{padding:'10px 8px'}}>{b.class}</td>
                    <td style={{padding:'10px 8px'}}>{b.subject}</td>
                    <td style={{padding:'10px 8px'}}><Timing b={b} /></td>
                    <td style={{padding:'10px 8px'}}>{b.students}/{b.max}</td>
                    <td style={{padding:'10px 8px'}}>{b.students >= (b.max||15) ? 'Full' :'Open'}</td>
                    <td style={{padding:'10px 8px',textAlign:'right'}}>
                      <button style={{background:'transparent',border:0,color:'var(--muted)',cursor:'pointer'}} onClick={()=> handleRemove(b.id)}>Remove</button>
                    </td>
                  </tr>
                ))}
                {batches.length === 0 && (
                  <tr><td colSpan={8} style={{padding:12,color:'var(--muted)'}}>No batches created yet.</td></tr>
                )}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  )
}
