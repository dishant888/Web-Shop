import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import { ItemCard } from '../components';
import { useContext } from 'react';
import { Store } from '../Store';

export default function HomePage() {

  const { items } = useContext(Store)

  let list = items.map((item) =>
    <Col xs={12} md={6} lg={4} xl={3} style={{border: '1px solid green'}}>
      {item.title}
    </Col>
  )

  return (
    <Container style={{border: '1px solid black'}}>
      <Row style={{border: '1px solid red'}}>
        {list.length > 0 ? list: 'Empty'}
      </Row>
    </Container>
  )
}
