import React, {useState, useMemo} from 'react'
import { getTextbooks } from '../utils/textbookService'
import { addPlan, updatePlan } from '../utils/plannerService'

const BOARDS = ['CBSE','ICSE','State Board']
const CLASSES = ['6th','7th','8th','9th','10th']
const SUBJECTS = ['Mathematics','Science','English','Social Science','Hindi','Computer']

function sampleChaptersFromTitle(title){
  // generate 8 sample chapters based on title
  return Array.from({length:8}).map((_,i)=> ({
    name: `Chapter ${i+1}`,
    topics: [`Topic ${i+1}.1`, `Topic ${i+1}.2`, `Topic ${i+1}.3`]
  }))
}

export default function AdminSyllabusPlanner(){
  const textbooks = getTextbooks()
  const [board,setBoard] = useState(BOARDS[0])
  const [cls,setCls] = useState(CLASSES[0])
  const [subject,setSubject] = useState(SUBJECTS[0])
  const [textbookId,setTextbookId] = useState(textbooks[0]?.id || '')
  const [startDate,setStartDate] = useState('')
  const [endDate,setEndDate] = useState('')
  const [classesPerWeek,setClassesPerWeek] = useState(3)
  const [examDate,setExamDate] = useState('')

  const [generatedPlan, setGeneratedPlan] = useState(null)

  const chapters = useMemo(()=>{
    if(!textbookId) return sampleChaptersFromTitle('Default')
    const tb = textbooks.find(t=> t.id === textbookId)
    return tb ? sampleChaptersFromTitle(tb.title || tb.fileName || 'Book') : sampleChaptersFromTitle('Book')
  },[textbookId, textbooks])

  function daysBetween(a,b){
    const da = new Date(a); const db = new Date(b)
    if(isNaN(da)||isNaN(db)) return 0
    const diff = Math.max(0, Math.ceil((db - da) / (1000*60*60*24)))
    return diff
  }

  const generate = ()=>{
    if(!startDate || !endDate) return alert('Please select start and end dates')
    const totalDays = daysBetween(startDate,endDate)
    const totalWeeks = Math.max(1, Math.ceil(totalDays / 7))

    // distribute chapters across weeks
    const weeks = []
    for(let w=0; w<totalWeeks; w++){
      const chap = chapters[w] || {name:`Revision Week ${w+1}`, topics:['Revision','Practice']}
      weeks.push({
        week: w+1,
        chapter: chap.name,
        topics: chap.topics,
        classCount: classesPerWeek,
        homework: `Exercises for ${chap.name}`,
        quizDay: ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'][ (w+3) % 7 ]
      })
    }

    const plan = {
      meta: {board, class: cls, subject, textbookId, startDate, endDate, classesPerWeek, examDate},
      weeks,
      approved: false,
      createdAt: new Date().toISOString()
    }
    setGeneratedPlan(plan)
  }

  const approve = ()=>{
    if(!generatedPlan) return alert('Generate a plan first')
    const items = addPlan(generatedPlan)
    const saved = items[0]
    // mark approved and update
    const updated = {...saved, approved: true}
    updatePlan(updated)
    alert('Plan approved and saved')
    setGeneratedPlan(updated)
  }

  return (
    <div className="card">
      <h3>Auto Syllabus Planner</h3>
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:12,marginTop:12}}>
        <div>
          <label style={{display:'block',fontWeight:700}}>Board</label>
          <select value={board} onChange={e=>setBoard(e.target.value)} style={{width:'100%',padding:8,marginTop:6}}>
            {BOARDS.map(b=> <option key={b} value={b}>{b}</option>)}
          </select>
        </div>
        <div>
          <label style={{display:'block',fontWeight:700}}>Class</label>
          <select value={cls} onChange={e=>setCls(e.target.value)} style={{width:'100%',padding:8,marginTop:6}}>
            {CLASSES.map(c=> <option key={c} value={c}>{c}</option>)}
          </select>
        </div>

        <div>
          <label style={{display:'block',fontWeight:700}}>Subject</label>
          <select value={subject} onChange={e=>setSubject(e.target.value)} style={{width:'100%',padding:8,marginTop:6}}>
            {SUBJECTS.map(s=> <option key={s} value={s}>{s}</option>)}
          </select>
        </div>
        <div>
          <label style={{display:'block',fontWeight:700}}>Textbook / Course</label>
          <select value={textbookId} onChange={e=>setTextbookId(e.target.value)} style={{width:'100%',padding:8,marginTop:6}}>
            <option value="">-- Default --</option>
            {textbooks.map(t=> <option key={t.id} value={t.id}>{t.title || t.fileName}</option>)}
          </select>
        </div>

        <div>
          <label style={{display:'block',fontWeight:700}}>Start Date</label>
          <input type="date" value={startDate} onChange={e=>setStartDate(e.target.value)} style={{width:'100%',padding:8,marginTop:6}} />
        </div>
        <div>
          <label style={{display:'block',fontWeight:700}}>End Date</label>
          <input type="date" value={endDate} onChange={e=>setEndDate(e.target.value)} style={{width:'100%',padding:8,marginTop:6}} />
        </div>

        <div>
          <label style={{display:'block',fontWeight:700}}>Classes per week</label>
          <input type="number" value={classesPerWeek} onChange={e=>setClassesPerWeek(Number(e.target.value))} style={{width:'100%',padding:8,marginTop:6}} />
        </div>
        <div>
          <label style={{display:'block',fontWeight:700}}>Exam Date</label>
          <input type="date" value={examDate} onChange={e=>setExamDate(e.target.value)} style={{width:'100%',padding:8,marginTop:6}} />
        </div>
      </div>

      <div style={{display:'flex',gap:8,justifyContent:'flex-end',marginTop:12}}>
        <button className="join-btn" onClick={generate}>Generate Plan</button>
        <button className="join-btn" onClick={approve} disabled={!generatedPlan || generatedPlan.approved}>Approve Plan</button>
      </div>

      {generatedPlan && (
        <div style={{marginTop:16}}>
          <h4>Weekly Plan Preview</h4>
          <div style={{overflowX:'auto',marginTop:8}}>
            <table style={{width:'100%',borderCollapse:'collapse'}}>
              <thead>
                <tr style={{textAlign:'left',color:'var(--muted)'}}>
                  <th>Week</th>
                  <th>Chapter</th>
                  <th>Topics</th>
                  <th>Class Count</th>
                  <th>Homework</th>
                  <th>Quiz/Revision</th>
                </tr>
              </thead>
              <tbody>
                {generatedPlan.weeks.map(w=> (
                  <tr key={w.week} style={{borderTop:'1px solid rgba(255,255,255,0.03)'}}>
                    <td style={{padding:8}}>{w.week}</td>
                    <td style={{padding:8}}>{w.chapter}</td>
                    <td style={{padding:8}}>{w.topics.join(', ')}</td>
                    <td style={{padding:8}}>{w.classCount}</td>
                    <td style={{padding:8}}>{w.homework}</td>
                    <td style={{padding:8}}>{w.quizDay}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}
    </div>
  )
}
