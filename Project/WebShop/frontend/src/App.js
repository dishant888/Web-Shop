import './App.css';
import { Navigation } from './components/';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { HomePage, SignInPage, SignUpPage } from './pages';
// import { useContext, useEffect } from 'react';
// import { ItemContext } from './Store';
import ProtectedRoutes from './components/ProtectedRoutes';
import AccountPage from './pages/AccountPage';
import MyItemsPage from './pages/MyItemsPage';
import CartPage from './pages/CartPage';
import AddItemPage from './pages/AddItemPage';


function App() {

  // const { setItems } = useContext(ItemContext)

  // const getItems = async () => {
  //   let data = await (await fetch('http://127.0.0.1:8000/api/items/')).json()
  //   setItems(data)
  // }

  // useEffect(() => {
  //   getItems()
  // }, [])

  return (
    <>
      <BrowserRouter>
        <Navigation />
        <br />
        <Routes>
          <Route element={<ProtectedRoutes />} >
            <Route path='/account' element={<AccountPage />} />
            <Route path='/additem' element={<AddItemPage />} />
            <Route path='/myitems' element={<MyItemsPage />} />
            <Route path='/cart' element={<CartPage />} />
          </Route>
          <Route path='/signup' element={<SignUpPage />} />
          <Route path='/login' element={<SignInPage />} />
          <Route path='/shop' element={<HomePage />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;