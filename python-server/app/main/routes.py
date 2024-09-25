
from flask import Flask, request, jsonify # type: ignore
import requests
from flask import Flask, render_template, jsonify
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



