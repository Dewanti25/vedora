import React from 'react'
import { useParams } from 'react-router-dom'

export default function TestDetail(){
  const { id } = useParams()
  return (
    <div>
      <h3>Test Detail</h3>
      <div className="card">
        <div style={{fontWeight:800}}>Test ID: {id}</div>
        <div style={{color:'var(--muted)'}}>This is a placeholder for the test/quiz detail page.</div>
      </div>
    </div>
  )
}
