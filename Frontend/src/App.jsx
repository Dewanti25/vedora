import React, { useEffect } from 'react'
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import Login from './pages/Login'
import Register from './pages/Register'
import Dashboard from './pages/Dashboard'
import DashboardLayout from './layouts/DashboardLayout'
import AIClassroom from './pages/AIClassroom'
import Courses from './pages/Courses'
import Homework from './pages/Homework'
import Notes from './pages/Notes'
import TestsQuizzes from './pages/TestsQuizzes'
import TestDetail from './pages/TestDetail'
import Progress from './pages/Progress'
import Career from './pages/Career'
import Planner from './pages/Planner'
import Achievements from './pages/Achievements'
import Settings from './pages/Settings'
import Curriculum from './pages/Curriculum'
import MyClasses from './pages/MyClasses'
import Schedule from './pages/Schedule'
import ClassroomSession from './pages/ClassroomSession'
import AdminBatches from './pages/AdminBatches'
import Textbooks from './pages/Textbooks'
import SyllabusPlanner from './pages/SyllabusPlanner'

function PrivateRoute({ children }) {
  // Direct access: always allow children (no login required)
  return children
}

export default function App() {
  useEffect(() => {
    // no-op in direct-access mode
  }, [])
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />

        <Route path="/" element={<PrivateRoute><DashboardLayout /></PrivateRoute>}>
          <Route index element={<Dashboard />} />
          <Route path="ai-classroom" element={<AIClassroom />} />
          <Route path="courses" element={<Courses />} />
          <Route path="homework" element={<Homework />} />
          <Route path="notes" element={<Notes />} />
          <Route path="tests-quizzes" element={<TestsQuizzes />} />
          <Route path="tests-quizzes/:id" element={<TestDetail />} />
          <Route path="progress" element={<Progress />} />
          <Route path="career-guidance" element={<Career />} />
          <Route path="planner" element={<Planner />} />
          <Route path="curriculum" element={<Curriculum />} />
          <Route path="my-classes" element={<MyClasses />} />
          <Route path="schedule" element={<Schedule />} />
          <Route path="classroom/:sessionId" element={<ClassroomSession />} />
          <Route path="admin/batches" element={<AdminBatches />} />
          <Route path="admin/textbooks" element={<Textbooks />} />
          <Route path="admin/syllabus" element={<SyllabusPlanner />} />
          <Route path="achievements" element={<Achievements />} />
          <Route path="settings" element={<Settings />} />
        </Route>

      </Routes>
    </BrowserRouter>
  )
}
