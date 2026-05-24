import React from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import AITeachingArea from '../components/AITeachingArea'
import ChatPanel from '../components/ChatPanel'
import StudentList from '../components/StudentList'

function makeDummySession(id){
  // create a dummy live session for demonstration
  const now = new Date()
  const start = new Date(now.getTime() - 5*60000)
  const end = new Date(now.getTime() + 25*60000)
  return {
    id,
    subject: 'Mathematics',
    chapter: 'Algebra',
    topic: 'Linear Equations',
    batchName: 'Evening Batch',
    students: 12,
    startISO: start.toISOString(),
    endISO: end.toISOString()
  }
}

export default function ClassroomSession(){
  const { sessionId } = useParams()
  const navigate = useNavigate()
  const session = React.useMemo(()=> makeDummySession(sessionId || 'demo'), [sessionId])

  return (
    <div>
      <div style={{display:'flex',justifyContent:'space-between',alignItems:'center'}}>
        <div>
          <div style={{fontSize:20,fontWeight:800}}>{session.subject} — {session.topic}</div>
          <div style={{color:'var(--muted)'}}>{session.chapter} • {session.batchName}</div>
        </div>
        <div style={{textAlign:'right'}}>
          <div style={{fontWeight:800}}>{session.students} students</div>
          <div style={{color:'var(--muted)'}}>AI Teacher</div>
        </div>
      </div>

      <div className="classroom-layout" style={{marginTop:12,display:'grid',gridTemplateColumns:'2fr 320px',gap:12}}>
        <div style={{display:'grid',gridTemplateRows:'1fr 320px',gap:12}}>
          <AITeachingArea session={session} />
          <ChatPanel session={session} />
        </div>
        <StudentList />
      </div>
    </div>
  )
}
