// import React, {useState, useEffect} from 'react';
// import './App.css';
// import { Pitches} from "./components/Pitches";
// import  Input  from "./components/Query";

// function App() {
//   const [pitches,setPitches] = useState([]);
//   useEffect(() => {
//     fetch("/pitches").then(response =>
//       response.json().then(data => {
//         setPitches(data.pitches);
//       })
//     );
//   }, []);
//
//
//   return (
//     <div className="App">
//       <Input/>
//       <Pitches pitches={pitches} />
//     </div>
//   );
// }
//
// export default App;

import React, { Component } from 'react';
import './App.css';

import Input from './components/Query';

class App extends Component {
  render() {
    const { input } = this.props;
    return (
      <div className="App">
        <Input input={input} />
      </div>
    );
  }
}

export default App;
