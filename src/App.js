import React, {useState, useEffect} from 'react';
import './App.css';
import { Pitches} from "./components/Pitches";

function App() {
  const [pitches,setPitches] = useState([]);
  useEffect(() => {
    fetch("/pitches").then(response =>
      response.json().then(data => {
        setPitches(data.pitches);
      })
    );
  }, []);


  return (
    <div className="App">
      <Pitches pitches={pitches} />
    </div>
  );
}

export default App;
