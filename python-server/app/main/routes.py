
from flask import Flask, request, jsonify # type: ignore
import requests
from flask import Flask, render_template, jsonify
from flask_login import LoginManager, login_required, current_user
from models import db, User, Product
from app.main import bp
from flask import render_template # type: ignore
import asyncio
from app.main import scrapper

@bp.route('/')
def home():
    return render_template('index.html')


@bp.route('/about')
def about():
    return render_template('about.html')

# Synchronous Flask route that scrapes product data
@bp.route('/get_link/', methods=['GET'])
def scrape_ingredients():
    # Get the URL from the GET request (replace POST with GET for URL retrieval)
    user_url = request.args.get('url')

    if not user_url:
        return jsonify({'error': 'URL not provided'}), 400

    # Run the async scraping function in a synchronous Flask context
    product_data = asyncio.run(scrapper.scrape_product(user_url))

    if product_data is None:
        return jsonify({'error': 'Failed to scrape product data'}), 500

    return jsonify(product_data)


login_manager.login_view = 'login'
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@bp.route('/')
@login_required
def dashboard():
    return render_template('dashboard.html')

@bp.route('/get-products')
@login_required
def get_products():
    user_products = Product.query.filter_by(user_id=current_user.id).all()
    return render_template('product_table.html', products=user_products)
