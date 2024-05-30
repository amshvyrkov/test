from flask_testing import TestCase

from app import create_app, db
from app.models.product import Product


class TestProductAPI(TestCase):
    def create_app(self):
        app = create_app()
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
        app.config["TESTING"] = True
        return app

    def setUp(self):
        db.create_all()
        db.session.add(
            Product(
                name="Test Product",
                description="A test product",
                price=9.99,
                category="Test Category",
            )
        )
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get_products(self):
        response = self.client.get("/api/products")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Test Product", response.data.decode())

    def test_search_products(self):
        response = self.client.get("/api/products/search?query=Test")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Test Product", response.data.decode())
