# app.py

from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


# @app.route('/')
# def index():
#     user_url = request.args.get('url')
    
#     if user_url:
#         return f"Received URL: {user_url}"
#     else:
#         return 'No URL provided.'
    

@app.route('/', methods=['GET'])
def scrape_ingredients():
    # Get the URL from the POST request
    user_url = request.args.get('url')
    return user_url
    if not user_url:
        return jsonify({'error': 'No URL provided'}), 400

    try:
        # Send a request to the URL
        response = requests.get(user_url)

        # Check if the request was successful
        if response.status_code != 200:
            return jsonify({'error': 'Failed to retrieve the webpage'}), 500

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Scrape ingredients (assuming they are in a div with class 'ingredients-list')
        ingredients = []
        ingredient_elements = soup.find_all(class_='ingredients-list')  # Modify based on the website's structure

        # Loop through and extract text
        for ingredient in ingredient_elements:
            ingredients.append(ingredient.get_text(strip=True))

        # If no ingredients found
        if not ingredients:
            return jsonify({'error': 'No ingredients found'}), 404

        # Return the scraped ingredients as JSON
        return jsonify({'ingredients': ingredients}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
