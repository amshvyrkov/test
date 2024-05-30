from flask import Blueprint, jsonify, request
from sqlalchemy import asc, desc, or_

from app import db
from app.models.product import Product

api = Blueprint("api", __name__)


@api.route("/products", methods=["POST"])
def create_product():
    data = request.get_json()
    new_product = Product(
        name=data["name"],
        description=data["description"],
        price=data["price"],
        category=data["category"],
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify({"message": "Product created successfully"}), 201


@api.route("/products", methods=["GET"])
def get_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products]), 200


@api.route("/products/<int:id>", methods=["GET"])
def get_product(id):
    product = Product.query.get_or_404(id)
    return jsonify(product.to_dict()), 200


@api.route("/products/<int:id>", methods=["PUT"])
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.get_json()
    product.name = data.get("name", product.name)
    product.description = data.get("description", product.description)
    product.price = data.get("price", product.price)
    product.category = data.get("category", product.category)
    db.session.commit()
    return jsonify({"message": "Product updated successfully"}), 200


@api.route("/products/<int:id>", methods=["DELETE"])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted successfully"}), 200


@api.route("/products/search", methods=["GET"])
def search_products():
    query = request.args.get("query", "")
    sort_by = request.args.get("sort_by", "id")
    order = request.args.get("order", "asc")

    search_condition = or_(
        Product.name.ilike(f"%{query}%"), Product.description.ilike(f"%{query}%")
    )
    if order == "desc":
        products = Product.query.filter(search_condition).order_by(desc(sort_by)).all()
    else:
        products = Product.query.filter(search_condition).order_by(asc(sort_by)).all()

    return jsonify([product.to_dict() for product in products]), 200


def init_app(app):
    app.register_blueprint(api, url_prefix="/api")
