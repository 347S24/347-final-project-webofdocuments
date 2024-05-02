import './App.css'
import { useEffect , useState } from 'react';


function App() {
  // default value of owned_matricies is an empty list
  const [owned_matricies, set_owned_matricies] = useState([])

  // fetch the owned matricies of the currently logged in user of the app and 
  // async wait for the api fetch to succeed before updating the owned 
  useEffect(() => {
    if (username) {
      let owned_matricies = fetch('/api/matricies')
      // wait for the promise to be fulfilled then make it json then set the owned matricies variable
      owned_matricies.then(x => x.json()).then(set_owned_matricies)
    }
  }, [username])

  console.log(owned_matricies)
  console.log(owned_matricies[0])

  return (
    <>
    <nav class="navbar">
      {/* it remains to be seen if a home button is even required, hence why it's commented out*/}
      {/* <a href="/" class="home-btn">Home</a> */}

      {
        // this displays the currently logged in user's username, or prompts them to login
        username ? <div class='greeting-msg'>{username}</div> : <div class='greeting-msg'>Please Login</div>
      }

      {
        // if the user is logged in, display a logout button
        // if there is no user currently logged in, display a slightly lighter in color login button
        username ? <a href="/accounts/logout/" class="logout-btn">Log Out</a> : <a href="/accounts/login/" class="login-btn">Log In</a>
      }

      <div class="create-btns">
        <a href="/editor/new_matrix/" class='create-matrix'>New Matrix</a>
        <a href="/editor/new_node/" class='create-node'>New Node</a>
      </div>

      {
        // if the user is logged in and currently has owned matricies, display the title. otherwise display no matrix message
        username ? owned_matricies.length ?
        <select class='matrix-dropdown'>
          {owned_matricies.map((matrix, i)=>
            <option key={i} class='matrix-option'>
              {/* TODO: change href to the slug? */}
              <a key={i} href='#' class='matrix-name'>{matrix.title}</a>
            </option>
          )}
        </select>
        :
        // no matrix case
        <div class='matrix-name'>No matricies yet</div>
        :
        // no user logged in case
        <div class='matrix-name'>Login to make <br></br> a new matrix</div>
      }

      <div class='list-nodes'>
        {
          // if the user is logged in and currently has owned nodees, display them. otherwise display no nodes message
          username ? owned_matricies.length && owned_matricies[0].documents.length ?
          // TODO: change href to link to the slug?
          owned_matricies[0].documents.map((node, i)=>
            <a key={i} class='node-link' href='#'>{node.file_name}</a>
          )
          :
          // no nodes case
          <div class='node-link'>No nodes yet</div>
          :
          // no user logged in case
          <div class='node-link'><br></br>Login to start <br></br>taking notes</div>
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
