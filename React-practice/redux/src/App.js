import './App.css';

function App() {
  const party  = new Array(1, 2, 3, 4)
  party.unshift('안녕', '안녕')
  party.pop()
  party.shift()
  party.slice()
  

  return (
    <div className="App">
     {party}
    </div>
  );
}

export default App;
