import Card from 'react-bootstrap/Card';
import Button from 'react-bootstrap/Button';

function truncate(str, n){
  return (str.length > n) ? str.slice(0, n-1) + '...' : str;
};

export default function ItemCard({item}) {
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
        <div className="text-dark float-start">€{item.price}</div>
        <div className='float-end'>
          <Button size='sm' variant="primary">Add to cart</Button>
        </div>
      </Card.Footer>
    </Card>
  )
}
