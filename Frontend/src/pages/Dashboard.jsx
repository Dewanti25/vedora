import React from 'react'
import StatCard from '../components/StatCard'
import LearningCategories from '../components/LearningCategories'
import AIClassroomPanel from '../components/AIClassroomPanel'
import HomeworkPanel from '../components/HomeworkPanel'
import NotesPanel from '../components/NotesPanel'
import TestsPanel from '../components/TestsPanel'
import ProgressPanel from '../components/ProgressPanel'
import CareerPanel from '../components/CareerPanel'
import AchievementsPanel from '../components/AchievementsPanel'

export default function Dashboard() {
  // static dummy data per requirements
  const stats = {
    overall_progress: 75,
    study_time: '24h 36m',
    lessons_completed: 128,
    test_score: 85,
    current_streak: '12 Days',
    subject_progress: [{name:'Mathematics', percent:85},{name:'Physics', percent:72}],
  }

  return (
    <div>
      <div style={{display:'flex',alignItems:'center',justifyContent:'space-between',gap:12,marginBottom:8}}>
        <div>
          <div style={{fontSize:22,fontWeight:800}}>Good Morning, Aarav! 👋</div>
          <div style={{color:'var(--muted)',fontSize:13,marginTop:4}}>Let's learn, grow and achieve your dreams today.</div>
        </div>
        <div style={{display:'flex',gap:12}}>
          <div style={{textAlign:'right',color:'var(--muted)'}}>Welcome back</div>
        </div>
      </div>

      <div className="stats-grid">
        <StatCard title="Overall Progress" value={`${stats.overall_progress}%`} meta="Keep it up!" />
        <StatCard title="Study Time" value={stats.study_time} meta="+15% this week" />
        <StatCard title="Lessons Completed" value={stats.lessons_completed} meta="+18% this week" />
        <StatCard title="Test Score" value={`${stats.test_score}%`} meta="+8% this week" />
        <StatCard title="Current Streak" value={stats.current_streak} meta="Amazing!" />
      </div>

      <LearningCategories />

      <div className="dashboard-panels">
        <AIClassroomPanel />
        <HomeworkPanel />
        <NotesPanel />
        <TestsPanel />
        <ProgressPanel />
        <CareerPanel />
        <AchievementsPanel />
      </div>

      <div className="section-grid">
        <div className="chart-card section">
          <h3>Learning Progress</h3>
          <div style={{display:'flex',gap:18,alignItems:'center',justifyContent:'center',paddingTop:8}}>
            <div className="donut-wrap">
              {/** SVG donut chart using overall_progress */}
              <svg viewBox="0 0 36 36" className="donut">
                <path className="donut-ring" d="M18 2.0845
                  a 15.9155 15.9155 0 0 1 0 31.831
                  a 15.9155 15.9155 0 0 1 0 -31.831"/>
                <path className="donut-segment" style={{strokeDasharray: `${stats.overall_progress} ${100 - stats.overall_progress}`}} d="M18 2.0845
                  a 15.9155 15.9155 0 0 1 0 31.831
                  a 15.9155 15.9155 0 0 1 0 -31.831"/>
                <text x="18" y="20.35" className="donut-number">{stats.overall_progress}%</text>
              </svg>
            </div>
            <div style={{minWidth:180}}>
              <div style={{fontWeight:800,fontSize:16}}>Weekly Focus</div>
              <div style={{color:'var(--muted)',marginTop:6}}>Keep a steady pace — try to study at least 4 sessions this week.</div>
              <div style={{marginTop:10}}>
                {stats.subject_progress.map(s=> (
                  <div key={s.name} style={{marginTop:8}}>
                    <div style={{display:'flex',justifyContent:'space-between',fontSize:13}}>
                      <div>{s.name}</div>
                      <div style={{fontWeight:800}}>{s.percent}%</div>
                    </div>
                    <div className="progress-bar"><div className="progress-fill" style={{width:`${s.percent}%`}} /></div>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>

        <div className="card section">
          <h3>Subject Wise Performance</h3>
          <div style={{marginTop:8}}>
            {stats.subject_progress.map(s=> (
              <div key={s.name} style={{display:'flex',flexDirection:'column',gap:6,marginTop:8}}>
                <div style={{display:'flex',alignItems:'center',justifyContent:'space-between'}}>
                  <div style={{display:'flex',alignItems:'center',gap:8}}>
                    <div className="card-icon">{s.name[0]}</div>
                    <div style={{fontWeight:700}}>{s.name}</div>
                  </div>
                  <div style={{fontWeight:900}}>{s.percent}%</div>
                </div>
                <div className="progress-bar small"><div className="progress-fill" style={{width:`${s.percent}%`}} /></div>
              </div>
            ))}
          </div>
        </div>

        <div className="card section">
          <h3>Upcoming Plan</h3>
          <div style={{display:'flex',alignItems:'center',justifyContent:'space-between',marginTop:8}}>
            <div>
              <div style={{fontWeight:800}}>Physics - Mechanics</div>
              <div style={{color:'var(--muted)',marginTop:4}}>Tomorrow • 10:00 AM • 60 mins</div>
            </div>
            <div>
              <button className="btn btn-ghost">Add Reminder</button>
              <button className="btn btn-primary" style={{marginLeft:8}}>Join</button>
            </div>
          </div>
        </div>

        <div className="card section">
          <h3>AI Suggestion For You</h3>
          <div style={{display:'flex',alignItems:'center',justifyContent:'space-between',marginTop:8}}>
            <div>
              <div style={{fontWeight:700}}>You are weak in "Quadratic Equations"</div>
              <div style={{color:'var(--muted)',marginTop:6}}>Start a personalized 7-day module to strengthen this topic.</div>
            </div>
            <div style={{display:'flex',flexDirection:'column',gap:8}}>
              <button className="btn btn-primary">Start Learning</button>
              <button className="btn btn-ghost">Ask AI Tutor</button>
            </div>
          </div>
        </div>

        <div className="card section">
          <h3>Homework</h3>
          <div style={{marginTop:8}}>
            <div style={{display:'flex',justifyContent:'space-between'}}>
              <div style={{color:'var(--muted)'}}>Submissions</div>
              <div style={{fontWeight:800}}>3 / 5</div>
            </div>
            <div className="progress-bar small" style={{marginTop:8}}><div className="progress-fill" style={{width:`${(3/5)*100}%`}} /></div>
            <div style={{marginTop:8,color:'var(--muted)'}}>Next due: Maths Assignment 2 • Tomorrow</div>
          </div>
        </div>

        <div className="card section">
          <h3>Quick Access</h3>
          <div style={{display:'flex',gap:8,flexWrap:'wrap',marginTop:8}}>
            {['AI Teacher','Ask Doubt','Notes Library','Test Yourself','Spoken English'].map((t)=> (
              <div key={t} className="pill">{t}</div>
            ))}
          </div>
          <div style={{marginTop:12,display:'flex',gap:8}}>
            <button className="btn btn-primary">Go to Notes</button>
            <button className="btn btn-ghost">Open Tests</button>
          </div>
        </div>
      </div>
    </div>
  )
}
