import "bootstrap/dist/css/bootstrap.min.css"
import { useState } from 'react'
import { BrowserRouter as Router, Route } from 'react-router-dom'
import Header from './components/Header'
import Description from './components/Description'
import Navbar from './components/Navbar'
import button1 from "./components/CustomButtonComponent"


function App() {
  const [showAddUser, setShowAddUser] = useState(false)
  return (
    <Router>
      <div>
        <Navbar />
      </div>
      <div className="container">
        < Header />
        < Description />
      </div>
    </Router>
  );
}

export default App;
