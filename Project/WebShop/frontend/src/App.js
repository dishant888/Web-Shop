import './App.css';
import { Navigation } from './components/';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { HomePage, SignInPage, SignUpPage } from './pages';
import { useContext, useEffect } from 'react';
import { ItemContext } from './Store';


function App() {

  const {setItems} = useContext(ItemContext)
  
  const getItems = async () => {
    let data = await (await fetch('http://127.0.0.1:8000/api/items/')).json()
    setItems(data)
  }

  useEffect(()=> {
    getItems()
  },[])

  return (
    <>
      <BrowserRouter>
      <Navigation/>
      <br/>
        <Routes>
          <Route  path='/shop' element={<HomePage/>} />
          <Route  path='/signup' element={<SignUpPage/>} />
          <Route  path='/login' element={<SignInPage/>} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;