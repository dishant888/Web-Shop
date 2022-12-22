import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';
import { useContext, useState } from 'react';
import { useNavigate } from 'react-router';
import { LoginContext } from '../Store';

export default function SignInPage() {

  const initialFormState = {
    "username": "",
    "password": ""
  }

  const [formData, setFormData] = useState(initialFormState)

  const [errors, setErrors] = useState({})

  const { userToken, setUserToken } = useContext(LoginContext)

  const navigate = useNavigate()

  const handleChange = (e) => {
    setFormData({...formData, [e.target.name]: e.target.value})
  }

  const handleSubmit = async (e) => {
    e.preventDefault()

    const requestOptions = {method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' }, body: JSON.stringify(formData)}
    try{
      let data = await (await fetch('http://127.0.0.1:8000/api/auth/login/', requestOptions)).json()
      
      if (!data.access){
        setErrors(data)
      }else {
        setErrors({})
        setFormData(initialFormState)
        setUserToken({isLoggedIn: true, ...data})
        navigate('/shop')  
      }
    }catch(e){
      console.log(e);
    }
  }

  return (
    <Container>
      <Row>
        <Col xs={{ span: 10, offset: 1 }} md={{ span: 6, offset: 3 }} lg={{span: 4, offset: 4}}>
          <br/>
          <h2>Login</h2>
          <br/>
          <Form onSubmit={handleSubmit}>
            <Form.Group className="mb-3" controlId="formBasicUsername">
              <Form.Label>Username</Form.Label>
              <Form.Control onChange={handleChange} value={formData.username} name='username' type="text" placeholder="Enter username" />
              <Form.Text className="text-danger">
                {errors.username}
              </Form.Text>
            </Form.Group>
            <Form.Group className="mb-3" controlId="formBasicPassword">
              <Form.Label>Password</Form.Label>
              <Form.Control onChange={handleChange} value={formData.password} name='password' type="password" placeholder="Password" />
              <Form.Text className="text-danger">
                {errors.password}
              </Form.Text>
              <Form.Text className="text-danger">
                {errors.detail}
              </Form.Text>
            </Form.Group>
            <Button variant="primary" type="submit">
              Submit
            </Button>
          </Form>
        </Col>
      </Row>
    </Container>
  )
}
