import React from 'react'
import { FaBell, FaBars } from 'react-icons/fa'

export default function TopNavbar({me}){
  const name = me?.email?.split('@')[0] || 'Aarav'
  return (
    <div className="topbar">
      <div className="mobile-hamburger" style={{display:'none'}}>
        <button onClick={() => {
          const sb = document.querySelector('.sidebar')
          if (!sb) return
          sb.classList.toggle('open')
        }} style={{background:'transparent',border:0,color:'var(--muted)',fontSize:18}}><FaBars /></button>
      </div>
      <div className="welcome">
        <div>
          <div style={{fontSize:18,fontWeight:700}}>Good Morning, {name}! 👋</div>
          <div style={{fontSize:12,color:'var(--muted)'}}>Let's learn, grow and achieve your dreams today.</div>
        </div>
      </div>
      <div className="search">
        <input placeholder="Search anything..." />
      </div>
      <div style={{display:'flex',alignItems:'center',gap:12}}>
        <div style={{position:'relative'}}>
          <FaBell style={{fontSize:18,color:'var(--muted)'}} />
          <span style={{position:'absolute',right:-6,top:-6,width:10,height:10,borderRadius:10,background:'#ff5c7c',border:'2px solid var(--panel)'}} />
        </div>
        <div style={{width:44,height:44,borderRadius:22,background:'linear-gradient(90deg,var(--accent),var(--accent-2))',display:'flex',alignItems:'center',justifyContent:'center',fontWeight:800}}>A</div>
      </div>
    </div>
  )
}
