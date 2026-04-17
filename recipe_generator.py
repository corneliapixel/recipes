import random
import time

import logging

# Configure logging ->
logging.basicConfig(
    filename='show_history.log',
    encoding="utf-8",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger = logging.getLogger(__name__)    # create logger for this file


# Dictionaries
recipes = {
    "vegetarian": ["Vegetarian Curry with Cauliflower and Chickpeas", "Vegetable Stir-Fry", "Halloumi and Carrot Steaks", "Sweetpotato Soup with Chevre", "Enchiladas"],
    "healthy": ["Salmon with Quinoa", "Grilled Chicken Salad", "Tuna Salad Asian Style", "Avocado Shrimp Salad", "Pumpkin Soup"], 
    "fastfood": ["Burgers and Fries", "Homemade Pizza", "Hot Dogs", "Mac 'n' Cheese", "Spaghetti and Meatballs"],
    "cheap": ["Carrot Biryani", "Nasi Goreng", "Spaghetti Carbonara", "Lentil Soup", "What's in the Fridge?"]
}

choice_mapping = {
        "1": "vegetarian",
        "2": "healthy",
        "3": "fastfood",
        "4": "cheap"
}

def show_menu():    # show menu for user 
    print("Welcome to the Randomized Recipe Generator!")
    print("☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰")
    print("  Any specific cravings?")
    print("☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰")
    print("  1. Vegetarian")
    print("  2. Healthy food")
    print("  3. Fast food")
    print("  4. Cheap food")
    print("  5. Random, please!")
    print("  6. Exit")
    print("☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰\n")


def show_recipe(category, recipe):
    print("Analyzing cravings...")
    time.sleep(2)
    print("Almost there...\n")
    time.sleep(1)
    print(f"Category: {category.title()}") # Display category with capitalized first letter
    print(f"Tonight's dinner: {recipe}\n")
    logger.info("Category: %s - Tonight's dinner: %s", category.title(), recipe)
    time.sleep(1)

# Returns a category and a random recipe based on the user's input or None if the input is invalid.
def fetch_recipe(preference):
    preference = preference.strip().lower() # tar bort mellanslag

    # Check if the user's choice matches a category
    if preference in choice_mapping:
        # Get category name from the mapping (under choice_mapping)
        category = choice_mapping[preference]
        recipe = random.choice(recipes[category])
        return category, recipe

    elif preference == "5":
        # Create an empty list to collect all recipes
        all_recipes = []

        # Loop through each list of recipes (one list per category) and save category + recipe to all_recipes list
        for category, recipe_list in recipes.items():
            for recipe in recipe_list:
                all_recipes.append((category, recipe))

        # Return a random recipe from the full list 
        return random.choice(all_recipes)

    # Return (None, None) when input is invalid so the function always return (category, recipe)
    return None, None


def ask_to_continue():
    return input("Want another round? (y/n): ").strip().lower() in ("yes", "y", "ja", "yas")


def main (): 
    while True:
        show_menu()
        preference = input("Pick your potion: (1-6)\t").strip()
        print("")

        # Exit
        if preference == '6':
            print("I guess there is always Foodora...\n")
            print("Take care. BYE!\n")
            break

        category, recipe = fetch_recipe(preference)

        if recipe is None:
            print("Sorry, I can't help you...\n")
            continue

        show_recipe(category, recipe)

        if not ask_to_continue():
            print("Take care. BYE!")
            break

main() 




    


