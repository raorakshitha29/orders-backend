# Order Management API

A simple and efficient REST API for managing orders built with FastAPI and SQLAlchemy.

## Features

- **Create Orders**: Add new orders with customer details and product information
- **View Orders**: Retrieve individual orders or list all orders
- **Filter Orders**: Filter orders by status with pagination support
- **Update Status**: Modify order status (Pending, Processing, Completed, Cancelled)
- **Database Integration**: SQLite database with SQLAlchemy ORM

## Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd orders
```

2. Install dependencies:

```bash
pip install fastapi uvicorn sqlalchemy
```

3. Run the application:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### Get API Info

- **GET** `/` - Returns API information

### Orders

- **POST** `/orders/` - Create a new order
- **GET** `/orders/{order_id}` - Get order by ID
- **GET** `/orders/` - List all orders (with optional filtering)
- **PATCH** `/orders/{order_id}/status` - Update order status

## Usage Examples

### Create Order

```bash
curl -X POST "http://localhost:8000/orders/" \
  -H "Content-Type: application/json" \
  -d '{
    "customer_name": "John Doe",
    "product_name": "Laptop",
    "quantity": 1,
    "price": 999.99
  }'
```

### Get Order

```bash
curl -X GET "http://localhost:8000/orders/1"
```

### List Orders with Filtering

```bash
curl -X GET "http://localhost:8000/orders/?status=Pending&limit=5"
```

### Update Order Status

```bash
curl -X PATCH "http://localhost:8000/orders/1/status" \
  -H "Content-Type: application/json" \
  -d '{"status": "Processing"}'
```

## Data Models

### Order

- `id`: Unique identifier
- `customer_name`: Customer's name
- `product_name`: Product name
- `quantity`: Order quantity
- `price`: Product price
- `status`: Order status (default: "Pending")
- `created_at`: Creation timestamp

## Development

### Project Structure

```
orders/
├── main.py          # FastAPI application and routes
├── models.py        # SQLAlchemy database models
├── schemas.py       # Pydantic models for API
├── crud.py          # Database operations
├── database.py      # Database configuration
└── README.md        # This file
```

### Interactive API Documentation

Visit `http://localhost:8000/docs` for Swagger UI documentation or `http://localhost:8000/redoc` for ReDoc.

## License

This project is open source and available under the MIT License.
