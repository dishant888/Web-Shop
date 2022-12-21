import { useContext, useState } from 'react';
import Button from 'react-bootstrap/Button';

import Container from 'react-bootstrap/Container';
import Form from 'react-bootstrap/Form';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import { NavLink, Link } from "react-router-dom";
import { Store } from '../Store';

function Navigation() {

  const [keyword, setKeyword] = useState('')
  const {setItems} = useContext(Store)

  const handleInput = async (e) => {
    setKeyword(e.target.value)
    console.log("event",e.target.value)
    console.log("keyword",keyword)
    
    try {
      let data = await (await fetch(`http://127.0.0.1:8000/api/items/search/?title=${e.target.value}`)).json()
      setItems(data.results)
      console.table(data.results)
    } catch (e){
      console.error("error" , e)
    }

  }

  return (
    <Navbar bg="light" expand="lg">
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
            <Nav.Link as={NavLink} to='/signup' >Sign Up</Nav.Link>
            <Nav.Link as={NavLink} to='/login' >Sign In</Nav.Link>
            {/* <NavDropdown title="Link" id="navbarScrollingDropdown">
              <NavDropdown.Item href="#action3">Action</NavDropdown.Item>
              <NavDropdown.Item href="#action4">
                Another action
              </NavDropdown.Item>
              <NavDropdown.Divider />
              <NavDropdown.Item href="#action5">
                Something else here
              </NavDropdown.Item>
            </NavDropdown>
            <Nav.Link href="#" disabled>
              Link
            </Nav.Link> */}
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