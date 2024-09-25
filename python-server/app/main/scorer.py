import pandas as pd

# Load the dataset from a CSV file
# Use raw string or forward slashes in the path
ingredients_df = pd.read_csv(r'python-server\app\static\data\ingredients_map.csv')
# or
# ingredients_df = pd.read_csv('python-server/app/static/data/ingredients_map.csv')

# Create a dictionary from the DataFrame for easier access
ingredients = {}
for index, row in ingredients_df.iterrows():
    ingredients[row['Ingredient'].strip().lower()] = {
        'name': row['Ingredient'],
        'skin_types': row['Skin Type'],
        'concerns': row['Concern']
    }

def is_ingredient_suitable(ingredient, user_skin_type):
    """Check if the ingredient is suitable for the user's skin type."""
    db_ingredient = ingredients.get(ingredient.strip().lower())
    if db_ingredient:
        # Check if the user's skin type matches the ingredient's skin types
        return user_skin_type.lower() in db_ingredient['skin_types'].lower() or 'all' in db_ingredient['skin_types'].lower()
    return False

def score_product(product_ingredients, user_skin_type):
    """Calculate the suitability score for the product based on ingredients and user skin type."""
    score = 0
    total_ingredients = 0
    matching_ingredients = []

    for ingredient in product_ingredients.split(','):
        ingredient = ingredient.strip().lower()
        total_ingredients += 1
        if is_ingredient_suitable(ingredient, user_skin_type):
            score += 1
            matching_ingredients.append(ingredients[ingredient])

    if total_ingredients > 0:
        score = (score / total_ingredients) * 5  # Normalize to a 0-5 scale

    print(f"Score for the product: {score:.2f} out of 5")
    print("Matching Ingredients:")
    for match in matching_ingredients:
        print(f" - {match['name']}: Suitable for {match['skin_types']}, Concerns: {match['concerns']}")

def analyze_ingredients(product_ingredients, user_skin_type):
    """Analyze the product ingredients for suitability against the user's skin type."""
    
    print("Ingredient Analysis:")
    for ingredient in product_ingredients.split(','):
        ingredient = ingredient.strip().lower()
        suitable = is_ingredient_suitable(ingredient, user_skin_type)
        
        if suitable:
            db_ingredient = ingredients.get(ingredient)
            if db_ingredient:
                print(f"Ingredient: {db_ingredient['name']}, Suitable: Yes, Concerns: {db_ingredient['concerns']}")
        else:
            print(f"Ingredient: {ingredient}, Suitable: No, Concerns: Not suitable for your skin type.")

# Example usage:
product_ingredients = "Alpha hydroxy acid (AHAs), Chamomile, Vitamin C"
user_skin_type = "Oily"
score_product(product_ingredients, user_skin_type)
analyze_ingredients(product_ingredients, user_skin_type)
