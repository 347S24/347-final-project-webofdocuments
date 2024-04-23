import { useState } from 'react'
import reactLogo from './assets/react.svg'
import djangoLogo from './assets/django.svg'
import viteLogo from './assets/vite.svg'
import './App.css'

// function App({username}) {
function App() {
  console.log("username is ", username);
  console.log(window);
  const [count, setCount] = useState(0)

  return (
    <>
    <nav class="navbar">

      <a href="/" class="home-btn">Home</a>

      {
        username ? <a href="/accounts/logout/" class="login-btn">Log Out</a> : <a href="/accounts/login/" class="login-btn">Log In</a>
      }

      <div class="create-btns">
        <a href="" class='create-btn'>New Matrix</a>
        <a href="" class='create-btn'>New Node</a>
      </div>

      <div class='matrix-name'>placeholder matrix</div>
      <div class='list-nodes'>
      </div>
    </nav>
      <div className="card">
        <p>
          You are logged in as {username}.
        </p>
      </div>
    </>
  )
}

export default App
