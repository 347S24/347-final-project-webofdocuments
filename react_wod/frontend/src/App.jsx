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

      {/* <a href="/" class="home-btn">Home</a> */}

      {
        username ? <div class='greeting-msg'>{username}</div> : <div class='greeting-msg'>Please Login</div>
      }

      {
        username ? <a href="/accounts/logout/" class="logout-btn">Log Out</a> : <a href="/accounts/login/" class="login-btn">Log In</a>
      }

      <div class="create-btns">
        <a href="" class='create-matrix'>New Matrix</a>
        <a href="" class='create-node'>New Node</a>
      </div>

      <div class='matrix-name'>Matrix Name</div>
      <div class='list-nodes'>
        {
          // need to add some way to list each thing of 
        }
      </div>
    </nav>
      <div>
        {
          username ? 
          <p>Hello {username}! Welcome to Web of Documents. <br></br> <br></br>
          To get started, try making a matrix to hold all your connected documents! <br></br>
          If you have already made a matrix, it's time to make your documents!</p>
          :
          <p>Hello & welcome to Web of Documents, your solution to cluttered notes!<br></br><br></br>
            Please login to utilize our app!</p>
        }
      </div>
    </>
  )
}

export default App
