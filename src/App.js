import './App.css';
import { useEffect, useState } from 'react';
import Home from './components/Home'
import Test from './components/Test'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { UserProvider } from './common/TestContext.js';
import LandingPage from './components/LandingPage.js';



function App() {


  localStorage.setItem('scroll',0)
  localStorage.setItem('index',0)

 

  
  return (
    <UserProvider>
      <Router>
        <div className="App">
          <Routes>
            <Route path="/" element={<LandingPage />} />
            <Route path="/home" element={<Home />} />
            <Route path="/test" element={<Test />} />
          </Routes>
        </div>
      </Router>
    </UserProvider>
  );
}

export default App;
