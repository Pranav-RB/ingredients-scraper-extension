import httpx
from bs4 import BeautifulSoup
import asyncio

# Async scraping function
async def scrape_product(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.text, 'html.parser')

        # These selectors might need adjustment based on the page structure
        try:
            name = soup.select_one('#productTitle').text.strip()
        except AttributeError:
            name = 'N/A'
        
        try:
            ingredients = soup.select_one('#a-normal a-spacing-micro').text.strip()
        except AttributeError:
            ingredients = 'N/A'
        
        try:
            skin_type = soup.select_one('#skin-type-info').text.strip()
        except AttributeError:
            skin_type = 'N/A'
        
        try:
            image_url = soup.select_one('#landingImage')['src']
        except AttributeError:
            image_url = 'N/A'

        try:
            active_ingredients_row = soup.find('tr', class_='a-spacing-small po-active_ingredients')

    # Extract the active ingredients text
            if active_ingredients_row:
                active_ingredients = active_ingredients_row.find('td', class_='a-span9').get_text(strip=True)
                print(f"Active Ingredients: {active_ingredients}")
            else:
                print("Active Ingredients not found.")
        except AttributeError:
            x = ['gahr ja'] 

        return {
            'name': name,
            'ingredients': active_ingredients,
            'skin_type': skin_type,
            'image_url': image_url
        }

