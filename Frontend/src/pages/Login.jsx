import React, { useState } from 'react'
import { useNavigate, Link } from 'react-router-dom'
import api from '../api'

export default function Login() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [error, setError] = useState(null)
  const [loading, setLoading] = useState(false)
  const navigate = useNavigate()

  async function handle(e) {
    e.preventDefault()
    setLoading(true)
    setError(null)
    try {
      const res = await api.post('/login', { email, password })
      const token = res.data.access_token || res.data.accessToken || res.data.token
      if (token) {
        localStorage.setItem('token', token)
        navigate('/')
        return
      }
      setError('Login failed: no token returned')
    } catch (err) {
      const msg = err?.response?.data?.detail || err?.message || 'Login failed'
      setError(msg)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div style={{minHeight:'100vh',display:'flex',alignItems:'center',justifyContent:'center'}}>
      <div style={{width:420,maxWidth:'95%',padding:28,borderRadius:14,background:'linear-gradient(180deg,rgba(255,255,255,0.02), rgba(255,255,255,0.01))',boxShadow:'0 10px 30px rgba(2,6,23,0.6)'}}>
        <div style={{display:'flex',alignItems:'center',gap:12,marginBottom:18}}>
          <div style={{width:44,height:44,borderRadius:10,background:'linear-gradient(90deg,var(--accent),var(--accent-2))'}} />
          <div>
            <div style={{fontSize:20,fontWeight:800}}>Vedora AI</div>
            <div style={{fontSize:12,color:'var(--muted)'}}>Your Personal AI Teacher</div>
          </div>
        </div>

        <h2 style={{margin:'6px 0 18px 0'}}>Login</h2>
        <form onSubmit={handle}>
          <div style={{marginBottom:10}}>
            <input required value={email} onChange={e=>setEmail(e.target.value)} placeholder="Email" style={{width:'100%',padding:10,borderRadius:8,border:'1px solid rgba(255,255,255,0.04)',background:'transparent',color:'inherit'}} />
          </div>
          <div style={{marginBottom:8}}>
            <input required type="password" value={password} onChange={e=>setPassword(e.target.value)} placeholder="Password" style={{width:'100%',padding:10,borderRadius:8,border:'1px solid rgba(255,255,255,0.04)',background:'transparent',color:'inherit'}} />
          </div>
          <div style={{display:'flex',alignItems:'center',justifyContent:'space-between',marginBottom:12}}>
            <label style={{fontSize:13,color:'var(--muted)'}}><input type="checkbox" style={{marginRight:8}} /> Remember me</label>
            <a href="#" style={{color: 'var(--accent)',fontSize:13,textDecoration:'none'}}>Forgot?</a>
          </div>
          <button type="submit" disabled={loading} style={{width:'100%',padding:12,borderRadius:10,border:0,background:'linear-gradient(90deg,var(--accent),var(--accent-2))',color:'#fff',fontWeight:700}}>{loading? 'Signing in...' : 'Sign In'}</button>
        </form>
        {error && <div style={{color:'#ff8a8a',marginTop:12}}>{error}</div>}

        <div style={{marginTop:14,fontSize:13,color:'var(--muted)'}}>Don't have an account? <Link to="/register" style={{color:'var(--accent)'}}>Register</Link></div>
      </div>
    </div>
  )
}
