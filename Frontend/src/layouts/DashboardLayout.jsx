import React from 'react'
import { Outlet } from 'react-router-dom'
import Sidebar from '../components/Sidebar'
import TopNavbar from '../components/TopNavbar'

export default function DashboardLayout({me}){
  return (
    <div className="app-shell">
      <Sidebar />
      <main className="main">
        <TopNavbar me={me} />
        <Outlet />
      </main>
    </div>
  )
}
