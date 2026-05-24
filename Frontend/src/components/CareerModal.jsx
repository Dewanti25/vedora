import React from 'react'

export default function CareerModal({visible,onClose}){
  if(!visible) return null
  return (
    <div className="modal-backdrop">
      <div className="modal card">
        <h3>Career Detail (Placeholder)</h3>
        <div style={{color:'var(--muted)'}}>Detailed career report will be shown here. This is a placeholder modal.</div>
        <div style={{display:'flex',justifyContent:'flex-end',marginTop:12}}>
          <button className="icon-btn" onClick={onClose}>Close</button>
        </div>
      </div>
    </div>
  )
}
