import React from 'react'
import { Link } from 'react-router-dom'

export default function TestCard({test}){
  const due = new Date(test.date).toLocaleString()
  return (
    <div className="test-card card">
      <div style={{display:'flex',alignItems:'center',justifyContent:'space-between',gap:12}}>
        <div>
          <div style={{fontWeight:800}}>{test.title}</div>
          <div style={{fontSize:13,color:'var(--muted)'}}>{test.questions} questions • {test.duration}</div>
        </div>
        <div style={{textAlign:'right'}}>
          <div style={{fontWeight:700}}>{test.completed? `${test.score}%` : ''}</div>
          <div style={{fontSize:12,color:'var(--muted)'}}>{due}</div>
          <div style={{marginTop:8}}>
            <Link to={`/tests-quizzes/${test.id}`} className="icon-btn">{test.completed? 'View':'Start'}</Link>
          </div>
        </div>
      </div>
    </div>
  )
}
