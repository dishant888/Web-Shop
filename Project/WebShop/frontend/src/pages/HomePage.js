import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import { ItemCard } from '../components';
import { useContext} from 'react';
import { ItemContext } from '../Store';
import Pagination from 'react-bootstrap/Pagination';

export default function HomePage() {

  const { items, setItems } = useContext(ItemContext)

  const getNextPage = async () => {
    let data = await (await fetch(items.next)).json()
    setItems(data)
  }

  const getPreviousPage = async () => {
    let data = await (await fetch(items.previous)).json()
    setItems(data)
  }

  let list = items.results.map((item) =>
    <Col key={item.id} xs={12} md={6} lg={4} xl={3} style={{textAlign: 'center'}}>
      <ItemCard item={item} />
      <br/>
    </Col>
  )

  return (
    <Container>
      <Row>
        {list.length > 0 ? list: <h3>Item Not Found</h3>}
      </Row>
      <Row>
        <Col>
          <br/>
          <Pagination>
            {items.previous && <Pagination.Prev onClick={getPreviousPage}> &#60; Previous</Pagination.Prev>}
            {items.next && <Pagination.Next onClick={getNextPage}>Next &#62;</Pagination.Next>}
          </Pagination>
        </Col>
      </Row>
    </Container>
  )
}
