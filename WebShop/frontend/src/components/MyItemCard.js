import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';
import { useContext, useState } from 'react';
import InputGroup from 'react-bootstrap/InputGroup';
import Form from 'react-bootstrap/Form';
import { LoginContext } from '../Store';

function truncate(str, n) {
    return (str.length > n) ? str.slice(0, n - 1) + '...' : str;
};

const Input = ({ value, onChange }) => {
    return (
        <InputGroup className="mb-3">
            <InputGroup.Text>€</InputGroup.Text>
            <Form.Control onChange={(e) => onChange(e)} type='number' value={value} />
        </InputGroup>
    )
}

const EditBtn = ({ item, onClick }) => {
    return (
        <div className='float-end'>
            <Button hidden={!item.on_sale} onClick={onClick} size='sm' variant="primary">Edit</Button>
        </div>
    )
}

const SaveBtn = ({ item, onClick }) => {
    return (
        <div>
            <Button size='sm' onClick={(e) => onClick(e, item)} variant="success">Save</Button>
        </div>
    )
}

export default function MyItemCard({ item }) {

    const [editClicked, setEditClicked] = useState(false)
    const [price, setPrice] = useState(item.price)
    const { userToken } = useContext(LoginContext)

    const handleEdit = () => {
        setEditClicked(true)
    }

    const handleSave = async (e, item) => {
        const requestOptions = { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': `Bearer ${userToken.access}` }, body: JSON.stringify({ price }) }
        let data = await (await fetch(`http://127.0.0.1:8000/api/items/edit/${item.id}`, requestOptions)).json()
        setEditClicked(false)
    }

    const handleChange = (e) => {
        setPrice(e.target.value)
    }

    return (
        <Card bg=''>
            <Card.Header>
                <Card.Title>
                    {item.title}
                </Card.Title>
            </Card.Header>
            <Card.Body>
                <Card.Subtitle className="mb-2 text-muted">{item.date}</Card.Subtitle>
                <Card.Text>
                    {truncate(item.description, 200)}
                </Card.Text>
            </Card.Body>
            <Card.Footer className="text-muted">
                {editClicked ? <Input value={price} onChange={handleChange} /> : <div className="text-dark float-start">€{price}</div>}
                {editClicked ? <SaveBtn item={item} onClick={handleSave} /> : <EditBtn item={item} onClick={handleEdit} />}
            </Card.Footer>
        </Card>
    )
}
