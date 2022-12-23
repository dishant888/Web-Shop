import { useContext, useState } from 'react';
import Container from 'react-bootstrap/Container';
import Form from 'react-bootstrap/Form';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import { NavLink, Link } from "react-router-dom";
import { useNavigate } from 'react-router';
import { ItemContext, LoginContext } from '../Store';

function Navigation() {

  const [keyword, setKeyword] = useState('')
  const { setItems } = useContext(ItemContext)
  const { userToken, setUserToken } = useContext(LoginContext)
  const navigate = useNavigate()

  const handleInput = async (e) => {
    setKeyword(e.target.value)

    try {
      let data = await (await fetch(`http://127.0.0.1:8000/api/items/search/?title=${e.target.value}`)).json()
      setItems(data)
    } catch (e) {
      console.error("error", e)
    }
  }

  const handleLogout = () => {
    setUserToken({
      isLoggedIn: false,
      access: "",
      refresh: ""
    })
    navigate('/shop')
  }

  return (
    <Navbar bg="primary" variant='dark' expand="lg">
      <Container fluid>
        <Navbar.Brand as={Link} to="/shop">Web Shop</Navbar.Brand>
        <Navbar.Toggle aria-controls="navbarScroll" />
        <Navbar.Collapse id="navbarScroll">
          <Nav
            className="me-auto my-2 my-lg-0"
            style={{ maxHeight: '100px' }}
            navbarScroll
          >
            <Nav.Link as={NavLink} to='/shop' >Home</Nav.Link>

            {userToken.isLoggedIn ? <>
              <Nav.Link as={NavLink} to='/additem' >Add Item</Nav.Link>
              <Nav.Link as={NavLink} to='/myitems' >My Items</Nav.Link>
              <Nav.Link as={NavLink} to='/account' >Account</Nav.Link>
              <Nav.Link as={NavLink} to='/cart' >Cart</Nav.Link>
              <Nav.Link onClick={handleLogout} >Logout</Nav.Link>
            </> : <>
              <Nav.Link as={NavLink} to='/signup' >Sign Up</Nav.Link>
              <Nav.Link as={NavLink} to='/login' >Sign In</Nav.Link>
            </>}
          </Nav>
          <Form className="d-flex">
            <Form.Control
              type="search"
              placeholder="Search"
              className="me-2"
              aria-label="Search"
              onChange={(e) => handleInput(e)}
              value={keyword}
            />
          </Form>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default Navigation;