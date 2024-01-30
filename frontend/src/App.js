import {useEffect, useState} from 'react';
import './App.css';

function App() {

  const [custumers, setCustumers] = useState([])


  useEffect(() => {
    const loadData = () => {
      fetch('http://127.0.0.1:8000/api/custumers/')
      .then(response => response.json())
      .then(data => setCustumers(data))
    }

    loadData()

  }, [])


  return (
    <div className="App">
      <header className="App-header">
        {custumers.map(custumer => (
          <h1 key={custumer.id}>{custumer.first_name} {custumer.last_name} {custumer.date_of_birth}</h1>
        ))}
      </header>
    </div>
  );
}

export default App;
