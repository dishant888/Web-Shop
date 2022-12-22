import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';
import { useContext, useState } from 'react';
import { LoginContext } from '../Store';

export default function AccountPage() {

  const initialFormState = {
    "current_password": "",
    "new_password": ""
  }

  const [formData, setFormData] = useState(initialFormState)
  const [errors, setErrors] = useState({})
  const [success, setSuccess] = useState("")
  const { userToken } = useContext(LoginContext)

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value })
  }

  const handleSubmit = async (e) => {
    e.preventDefault()

    const requestOptions = { method: 'PUT', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': `Bearer ${userToken.access}` }, body: JSON.stringify(formData) }
    let data = await (await fetch('http://127.0.0.1:8000/api/auth/change-password/', requestOptions)).json()
    console.log(data);
    if (data.message) {
      setErrors({})
      setSuccess(data.message)
      setFormData(initialFormState)
    } else {
      setErrors(data)
      setSuccess("")
    }
  }

  return (
    <Container>
      <Row>
        <Col xs={{ span: 10, offset: 1 }} md={{ span: 6, offset: 3 }} lg={{ span: 4, offset: 4 }}>
          <br />
          <h2>Change Password</h2>
          <br />
          <Form onSubmit={handleSubmit}>
            <Form.Group className="mb-3" controlId="formBasicUsername">
              <Form.Label>Curremt Password</Form.Label>
              <Form.Control name='current_password' onChange={handleChange} value={formData.current_password} type="text" placeholder="Enter current password" />
              <Form.Text className="text-danger">
                {errors.current_password}
              </Form.Text>
            </Form.Group>
            <Form.Group className="mb-3" controlId="formBasicPassword">
              <Form.Label>New Password</Form.Label>
              <Form.Control name='new_password' onChange={handleChange} value={formData.new_password} type="text" placeholder="Enter new password" />
              <Form.Text className="text-danger">
                {errors.new_password}
              </Form.Text>
              <Form.Text className="text-success">
                {success}
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
