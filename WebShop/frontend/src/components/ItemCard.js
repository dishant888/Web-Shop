import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';
import { useContext, useState } from 'react';
import { LoginContext } from '../Store';
import Alert from 'react-bootstrap/Alert';


function truncate(str, n) {
  return (str.length > n) ? str.slice(0, n - 1) + '...' : str;
};

export default function ItemCard({ item }) {

  const [error, setError] = useState("")
  const [success, setSuccess] = useState("")
  const { userToken } = useContext(LoginContext)

  const handleClick = async () => {
    const requestOptions = { method: 'GET', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': `Bearer ${userToken.access}` } }
    let data = await (await fetch(`http://127.0.0.1:8000/api/cart/add/${item.id}`, requestOptions)).json()

    if (data.code) {
      setError("Please login to add item to your cart.")
      setSuccess("")
    } else if (data.seller) {
      setError(data.seller)
      setSuccess("")
    } else {
      setError("")
      setSuccess("Item added to the cart.")
    }
    setTimeout(() => {
      setError("")
      setSuccess("")
    }, 1500)
  }

  return (
    <>
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
          <div className="text-dark float-start">€{item.price}</div>
          <div className='float-end'>
            <Button size='sm' onClick={handleClick} variant="primary">Add to cart</Button>
          </div>
        </Card.Footer>
      </Card>
      <br />
      <Alert hidden={!error} variant='danger'>
        {error}
      </Alert>
      <Alert hidden={!success} variant='success'>
        {success}
      </Alert>
    </>
  )
}
