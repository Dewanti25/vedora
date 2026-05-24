import React, {useState} from 'react'
import TestCard from '../components/TestCard'

const dummy = [
  {id:1,title:'Maths Chapter Test - 5',questions:20,duration:'30m',completed:false,date:'2026-05-30',score:0},
  {id:2,title:'Physics Numericals Test',questions:15,duration:'25m',completed:true,date:'2026-05-20',score:72},
  {id:3,title:'Chemistry Quick Test',questions:10,duration:'15m',completed:false,date:'2026-06-01',score:0},
  {id:4,title:'Biology Chapter Test',questions:25,duration:'40m',completed:true,date:'2026-05-10',score:88},
]

export default function TestsQuizzes(){
  const [tab,setTab] = useState('all')

  const filtered = dummy.filter(t=>{
    if(tab==='all') return true
    if(tab==='upcoming') return new Date(t.date) > new Date()
    if(tab==='completed') return t.completed
    return true
  })

  return (
    <div>
      <div style={{display:'flex',justifyContent:'space-between',alignItems:'center',marginBottom:12}}>
        <h3>Tests & Quizzes</h3>
      </div>

      <div className="tabs" style={{display:'flex',gap:8,marginBottom:12}}>
        <button className={tab==='all'? 'active':''} onClick={()=>setTab('all')}>All Tests</button>
        <button className={tab==='upcoming'? 'active':''} onClick={()=>setTab('upcoming')}>Upcoming</button>
        <button className={tab==='completed'? 'active':''} onClick={()=>setTab('completed')}>Completed</button>
      </div>

      <div style={{display:'grid',gap:10}}>
        {filtered.map(t=> <TestCard key={t.id} test={t} />)}
      </div>
    </div>
  )
}
