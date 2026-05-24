import React from 'react'
import { NavLink } from 'react-router-dom'
import IconDashboard from '../icons/IconDashboard'
import IconAI from '../icons/IconAI'
import IconCourses from '../icons/IconCourses'
import IconHomework from '../icons/IconHomework'
import IconNotes from '../icons/IconNotes'
import IconTests from '../icons/IconTests'
import IconSettings from '../icons/IconSettings'
import IconNotifications from '../icons/IconNotifications'

const items = [
  {label:'Dashboard', icon: IconDashboard, to:'/'},
  {label:'AI Classroom', icon: IconAI, to:'/ai-classroom'},
  {label:'Curriculum', icon: IconCourses, to:'/curriculum'},
  {label:'My Classes', icon: IconAI, to:'/my-classes'},
  {label:'Schedule', icon: IconNotifications, to:'/schedule'},
  {label:'Manage Batches', icon: IconSettings, to:'/admin/batches'},
  {label:'Textbooks', icon: IconCourses, to:'/admin/textbooks'},
  {label:'Syllabus Planner', icon: IconCourses, to:'/admin/syllabus'},
  {label:'Courses', icon: IconCourses, to:'/courses'},
  {label:'Homework', icon: IconHomework, to:'/homework'},
  {label:'Notes Library', icon: IconNotes, to:'/notes'},
  {label:'Tests & Quizzes', icon: IconTests, to:'/tests-quizzes'},
  {label:'Progress', icon: IconAI, to:'/progress'},
  {label:'Career Guidance', icon: IconAI, to:'/career-guidance'},
  {label:'Planner', icon: IconAI, to:'/planner'},
  {label:'Achievements', icon: IconAI, to:'/achievements'},
  {label:'Settings', icon: IconSettings, to:'/settings'},
]

export default function Sidebar(){
  const handleNavClick = () => {
    if (window.innerWidth <= 900) {
      const sb = document.querySelector('.sidebar')
      sb && sb.classList.remove('open')
    }
  }

  return (
    <aside className="sidebar">
      <div className="logo">
        <span className="dot" />
        <div>
          <div>Vedora AI</div>
          <div style={{fontSize:12,color:'var(--muted)'}}>Your AI Teacher</div>
        </div>
      </div>
      <nav className="nav">
        {items.map(({label,icon:Icon,to})=> (
          <NavLink key={label} to={to} end className={({isActive})=> isActive? 'nav-link active': 'nav-link'} onClick={handleNavClick}>
            <Icon className="sidebar-icon" />
            <span className="label">{label}</span>
          </NavLink>
        ))}
      </nav>
      <div className="upgrade-card">
        <small>Upgrade to Premium</small>
        <div style={{fontWeight:800,fontSize:14}}>Unlock all features</div>
        <button className="upgrade-btn">Upgrade Now</button>
        <div className="robot-figure">
          <div className="robot-avatar">🤖</div>
          <div style={{flex:1}}>
            <div style={{fontWeight:700}}>Aarav!</div>
            <div style={{fontSize:12,color:'var(--muted)'}}>Student</div>
          </div>
        </div>
      </div>

      <div className="sidebar-footer">
        <div className="quick-access">
          <div className="qa">AI</div>
          <div className="qa">Notes</div>
          <div className="qa">Tests</div>
        </div>
      </div>
    </aside>
  )
}
