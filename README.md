# CRUD API

## Description
This project is a REST API for managing product data.

## Technologies
- Python 3.9
- Flask
- SQLAlchemy
- PostgreSQL
- Docker

## Installation

### Clone the repository
git clone https://your-repository-url.git
cd your-project-name

### Setting vars
SECRET_KEY=your_secret_key
DATABASE_URL=postgresql://username:password@localhost/dbname

### Build and setup
docker-compose up --build

## API DOCK 

### GET
curl http://localhost:5000/api/products

### POST
curl -X POST -H "Content-Type: application/json" -d '{"name":"New Product", "description":"Description of New Product", "price": 99.99, "category":"General"}' http://localhost:5000/api/products

### PUT 
curl -X PUT -H "Content-Type: application/json" -d '{"name":"Updated Product Name", "description":"Updated Description", "price": 89.99, "category":"Updated Category"}' http://localhost:5000/api/products/1

### DELETE 
curl -X DELETE http://localhost:5000/api/products/1

## TESTING
docker-compose run web pytest
