import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import { useContext, useEffect, useState } from 'react';
import { LoginContext } from '../Store';
import Table from 'react-bootstrap/Table';
import Button from 'react-bootstrap/Button';

export default function CartPage() {

    const { userToken } = useContext(LoginContext)
    const [cart, setCart] = useState([])

    const getCartItems = async () => {

        const requestOptions = { method: 'GET', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': `Bearer ${userToken.access}` } }
        let data = await (await fetch('http://127.0.0.1:8000/api/cart/', requestOptions)).json()
        setCart(data)
    }

    const handleDelete = async (item_id) => {
        const requestOptions = { method: 'GET', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': `Bearer ${userToken.access}` } }
        let data = await (await fetch(`http://127.0.0.1:8000/api/cart/delete/${item_id}`, requestOptions)).json()
        setCart(data);
    }

    const handleBuy = async () => {
        const requestOptions = { method: 'POST', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': `Bearer ${userToken.access}` } }
        let data = await (await fetch(`http://127.0.0.1:8000/api/cart/buy/`, requestOptions)).json()
        console.log(data);
        setCart(data);
    }

    let total = 0
    let list = cart.map((item, index) => {
        total += item.price
        return (
            <tr key={index}>
                <td>{index + 1}</td>
                <td>{item.title}</td>
                <td>€{item.price}</td>
                <td>{item.notification}</td>
                <td>
                    <Button size='sm' onClick={() => handleDelete(item.item_id)} variant='danger'>Remove</Button>
                </td>
            </tr>
        )
    })


    useEffect(() => {
        getCartItems()
    }, [])

    return (
        <Container>
            <Row>
                <Col>
                    {cart.length != 0 ?
                        <Table responsive>
                            <thead>
                                <tr>
                                    <th>#</th>
                                    <th>Item</th>
                                    <th>Price</th>
                                    <th></th>
                                    <th>Action</th>
                                </tr>
                            </thead>
                            <tbody>
                                {list}
                            </tbody>
                            <tfoot>
                                <tr>
                                    <td></td>
                                    <th>Total</th>
                                    <th>
                                        €{Math.fround(total).toFixed(2)}
                                    </th>
                                    <td></td>
                                    <td>
                                        <Button size='sm' onClick={handleBuy} variant='success'>Purchase</Button>
                                    </td>
                                </tr>
                            </tfoot>
                        </Table>
                        :
                        <h2> Cart is empty </h2>
                    }
                </Col>
            </Row>
        </Container>
    )
}
