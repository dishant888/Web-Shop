import { useContext, useEffect, useState } from 'react';
import { LoginContext } from '../Store';
import { MyItemCard } from '../components';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Form from 'react-bootstrap/Form';

export default function MyItemsPage() {

  const { userToken } = useContext(LoginContext)
  const [myItems, setMyItems] = useState([])

  const getMyItems = async (filter = 'sale') => {

    const requestOptions = { method: 'GET', headers: { 'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': `Bearer ${userToken.access}` } }
    let data = await (await fetch(`http://127.0.0.1:8000/api/items/inventory/?filter_by=${filter}`, requestOptions)).json()
    setMyItems(data);
  }

  let list = myItems.map((item) =>
    <Col key={item.id} xs={12} md={6} lg={4} xl={3} style={{ textAlign: 'center' }}>
      <MyItemCard item={item} />
      <br />
    </Col>
  )

  const handleChange = (e) => {
    getMyItems(e.target.value)
  }

  useEffect(() => {
    getMyItems()
  }, [])

  return (
    <Container>
      <Row>
        <Col style={{ textAlign: 'center' }}>
          <Form.Select onChange={handleChange}>
            <option selected value="sale">On Sale</option>
            <option value="sold">Sold</option>
            <option value="purchased">Purchased</option>
          </Form.Select>
          <br />
        </Col>
      </Row>
      <Row>
        {list.length > 0 ? list : <h3>Item Not Found</h3>}
      </Row>
    </Container>
  )
}
