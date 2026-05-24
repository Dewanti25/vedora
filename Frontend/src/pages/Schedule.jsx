import React from 'react'
import ClassSessionCard from '../components/ClassSessionCard'
import { getJoinedClasses } from '../utils/classService'

function makeCBSE8MathSchedule(){
  const now = new Date()
  // live session: start 5 min ago, end 25 min from now
  const liveStart = new Date(now.getTime() - 5*60000)
  const liveEnd = new Date(now.getTime() + 25*60000)

  const tomorrow = new Date(now.getTime() + 24*60*60000)
  const tStart = new Date(tomorrow.setHours(16,0,0,0))
  const tEnd = new Date(tStart.getTime() + 90*60000)

  const dayAfter = new Date(now.getTime() + 2*24*60*60000)
  const dStart = new Date(dayAfter.setHours(18,0,0,0))
  const dEnd = new Date(dStart.getTime() + 90*60000)

  return [
    {
      id: 'cbse-8-math-live',
      subject: 'Mathematics',
      chapter: 'Algebra',
      topic: 'Linear Equations',
      startISO: liveStart.toISOString(),
      endISO: liveEnd.toISOString(),
      batchName: 'Evening Batch',
      board: 'CBSE',
      class: '8th'
    },
    {
      id: 'cbse-8-math-2',
      subject: 'Mathematics',
      chapter: 'Geometry',
      topic: 'Triangles',
      startISO: tStart.toISOString(),
      endISO: tEnd.toISOString(),
      batchName: 'Weekend Batch',
      board: 'CBSE',
      class: '8th'
    },
    {
      id: 'cbse-8-math-3',
      subject: 'Mathematics',
      chapter: 'Number Systems',
      topic: 'Rational Numbers',
      startISO: dStart.toISOString(),
      endISO: dEnd.toISOString(),
      batchName: 'Morning Batch',
      board: 'CBSE',
      class: '8th'
    }
  ]
}

export default function Schedule(){
  const joined = getJoinedClasses()
  const cbseSchedule = makeCBSE8MathSchedule()

  // also create sessions for joined classes (one upcoming per joined)
  const joinedSessions = joined.flatMap(b => {
    const now = new Date()
    const nextStart = new Date(now.getTime() + (Math.floor(Math.random()*3)+1)*24*60*60000)
    nextStart.setHours(17,0,0,0)
    const nextEnd = new Date(nextStart.getTime() + 90*60000)
    return [{
      id: `session-${b.id}-1`,
      subject: b.subject,
      chapter: 'Revision',
      topic: 'Concepts Overview',
      startISO: nextStart.toISOString(),
      endISO: nextEnd.toISOString(),
      batchName: b.name,
      board: b.board,
      class: b.class
    }]
  })

  const sessions = [...cbseSchedule, ...joinedSessions]

  const handleJoin = (session)=>{
    const now = new Date()
    const start = new Date(session.startISO)
    const end = new Date(session.endISO)
    if(now >= start && now <= end){
      alert(`Joining live class: ${session.subject} — ${session.topic}`)
    } else {
      alert('Class is not live yet')
    }
  }

  return (
    <div>
      <h2>Schedule — Upcoming AI Classes</h2>
      <div style={{color:'var(--muted)',marginTop:6}}>Your scheduled AI class sessions. "Join Now" appears only when class is live.</div>

      <div style={{marginTop:16,display:'grid',gridTemplateColumns:'repeat(2,1fr)',gap:12}}>
        {sessions.map(s=> (
          <ClassSessionCard key={s.id} session={s} onJoin={handleJoin} />
        ))}
      </div>
    </div>
  )
}
