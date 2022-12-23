import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import { useContext, useState } from 'react';
import FloatingLabel from 'react-bootstrap/FloatingLabel';
import InputGroup from 'react-bootstrap/InputGroup';
import { LoginContext } from '../Store';

export default function AddItemPage() {

    const initialFormState = {
        "title": "",
        "description": "",
        "price": 0
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

        const requestOptions = { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': `Bearer ${userToken.access}` }, body: JSON.stringify(formData) }
        let data = await (await fetch('http://127.0.0.1:8000/api/items/add/', requestOptions)).json()
        console.log(data);
        if (data.id) {
            setErrors({})
            setFormData(initialFormState)
            setSuccess("New Item Added Successfully!")
        } else {
            setErrors(data)
            setSuccess("")
        }

        setTimeout(() => {
            setSuccess("")
        }, 1500)
    }

    return (
        <Container>
            <Row>
                <Col xs={{ span: 10, offset: 1 }} md={{ span: 6, offset: 3 }} lg={{ span: 4, offset: 4 }}>
                    <br />
                    <h2>Add New Item</h2>
                    <br />
                    <Form onSubmit={handleSubmit}>
                        <Form.Group className="mb-3" controlId="formBasicUsername">
                            <Form.Control onChange={handleChange} value={formData.title} name='title' type="text" placeholder="Enter item title" />
                            <Form.Text className="text-danger">
                                {errors.title}
                            </Form.Text>
                        </Form.Group>
                        <Form.Group className="mb-3" controlId="formBasicUsername">
                            <FloatingLabel controlId="floatingTextarea2" label="Description">
                                <Form.Control
                                    as="textarea"
                                    name='description'
                                    value={formData.description}
                                    placeholder="Enter Description"
                                    style={{ height: '100px' }}
                                    onChange={handleChange}
                                />
                            </FloatingLabel>
                            <Form.Text className="text-danger">
                                {errors.description}
                            </Form.Text>
                        </Form.Group>

                        <InputGroup className="mb-3">
                            <InputGroup.Text>€</InputGroup.Text>
                            <Form.Control type='number' onChange={handleChange} placeholder='Price' name='price' value={formData.price} />
                        </InputGroup>
                        <Form.Group>
                            <Form.Text className="text-danger">
                                {errors.price}
                            </Form.Text>
                            <Form.Text className="text-success">
                                {success}
                            </Form.Text>
                        </Form.Group>
                        <br />
                        <Button variant="primary" type="submit">
                            Submit
                        </Button>
                    </Form>
                </Col>
            </Row>
        </Container>
    )
}
