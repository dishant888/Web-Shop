import './App.css';
import { Navigation } from './components/';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { HomePage, SignInPage, SignUpPage } from './pages';
import { useEffect, useState } from 'react';
import { Store } from './store';

function App() {

  let [items, setItems] = useState([])
  const getItems = async () => {
    let data = await (await fetch('http://127.0.0.1:8000/api/items/')).json()
    setItems(data.results)
  }

  useEffect(()=> {
    getItems()
  },[])

  return (
    <>
    <Store.Provider value={{items, setItems}}>
      <BrowserRouter>
      <Navigation/>
      <br/>
        <Routes>
          <Route  path='/shop' element={<HomePage/>} />
          <Route  path='/signup' element={<SignUpPage/>} />
          <Route  path='/login' element={<SignInPage/>} />
        </Routes>
      </BrowserRouter>
    </Store.Provider>
    </>
  );
}

export default App;
