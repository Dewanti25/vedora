import React, {useState} from 'react'
import HomeworkItem from '../components/HomeworkItem'
import UploadModal from '../components/UploadModal'

const dummy = [
  {id:1,title:'Maths Assignment 2', type:'PDF', size:'1.2 MB', status:'Submitted', due:'2026-05-26', subject:'Mathematics'},
  {id:2,title:'Physics Numericals', type:'PDF', size:'2.8 MB', status:'Pending', due:'2026-05-27', subject:'Physics'},
  {id:3,title:'Chemistry Lab Report', type:'DOC', size:'640 KB', status:'Evaluated', due:'2026-05-22', subject:'Chemistry'},
]

export default function Homework(){
  const [tab,setTab] = useState('my')
  const [items,setItems] = useState(dummy)
  const [showUpload,setShowUpload] = useState(false)

  function handleUpload(data){
    const f = {id:Date.now(), title: data.title || 'Untitled', type: data.file? data.file.name.split('.').pop().toUpperCase():'FILE', size: data.file? Math.round(data.file.size/1024)+' KB':'—', status:'Submitted', due:'2026-06-01', subject:data.subject}
    setItems(prev=>[f,...prev])
  }

  const filtered = items.filter(i=> {
    if(tab==='my') return true
    if(tab==='evaluated') return i.status.toLowerCase() === 'evaluated'
    if(tab==='pending') return i.status.toLowerCase() === 'pending'
    return true
  })

  return (
    <div>
      <div style={{display:'flex',justifyContent:'space-between',alignItems:'center',marginBottom:12}}>
        <h3>Homework</h3>
        <div style={{display:'flex',gap:8}}>
          <button className="icon-btn" onClick={()=>setShowUpload(true)}>Upload Homework</button>
        </div>
      </div>

      <div className="tabs" style={{display:'flex',gap:8,marginBottom:12}}>
        <button className={tab==='my'? 'active':''} onClick={()=>setTab('my')}>My Homework</button>
        <button className={tab==='evaluated'? 'active':''} onClick={()=>setTab('evaluated')}>Evaluated</button>
        <button className={tab==='pending'? 'active':''} onClick={()=>setTab('pending')}>Pending</button>
      </div>

      <div style={{display:'grid',gap:10}}>
        {filtered.map(hw=> <HomeworkItem key={hw.id} hw={hw} />)}
      </div>

      <UploadModal visible={showUpload} onClose={()=>setShowUpload(false)} onSubmit={handleUpload} />
    </div>
  )
}
