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

def main_menu():
    print("\nWelcome to the Randomized Recipe Generator!")
    print("☰" * 50)
    print("Main Menu")
    print("☰" * 50)
    print("  1. Choose a category")
    print("  2. Fetch a random recipe")
    print("  3. Show recipe history")
    print("  0. Exit program")
    print("☰" * 50 + "\n")

def show_categories():
    print("All categories")
    print("☰" * 25)
    print("  1. Vegetarian")
    print("  2. Healthy Food")
    print("  3. Fast Food")
    print("  4. Cheap Food")
    print("☰" * 25)


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
    
    # Return (None, None) when input is invalid so the function always return (category, recipe)
    return None, None


def fetch_random_recipe():
        # Create an empty list to collect all recipes
        all_recipes = []

        # Loop through each list of recipes (one list per category) and save category + recipe to all_recipes list
        for category, recipe_list in recipes.items():
            for recipe in recipe_list:
                all_recipes.append((category, recipe))

        # Return a random recipe from the full list 
        return random.choice(all_recipes)


def ask_to_continue():
    return input("Want another round? (y/n): ").strip().lower() in ("yes", "y", "ja", "yas")

# Function that displays the saved recipe history from show_history.log
def show_history():
    try:
        with open("show_history.log", "r", encoding="utf-8")  as file:
            print("\n\t\t\t  🍽   Recipe History  🍽  ") # print heading
            print("⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯")
            # Loop for each line in the file (each line = one logged recipe)
            for i, line in enumerate(file, start=1):
                print(f"{i}. {line}", end="") # Print each line together with its index number (starting from 1)
            print("⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯⋯")

        input("\n⏎ Press Enter for return ⏎")

    # If the file doesn't exist (no logged recipes)
    except FileNotFoundError:
        print("\n Sorry, no history logged yet")


def main (): 
    while True:
        main_menu()
        menu_choice = input("Make a choice: (0-4)\t").strip()
        print("☰" * 25)
        print("")

        # Exit
        if menu_choice == '0':
            print("I guess there is always Foodora...\n")
            print("Take care. BYE!\n")
            break

        elif menu_choice == '3':
            show_history()
            continue

        elif menu_choice == '1':
            show_categories()
            preference = input("\nPick a category: (1-4)\t")
            print("☰" * 25)
            print("")

            category, recipe = fetch_recipe(preference)

            if recipe is None:
                print("Sorry, I can't help you...\n")
                continue

            show_recipe(category, recipe)

        elif menu_choice == '2':
            category, recipe = fetch_random_recipe()
            show_recipe(category, recipe)

        else:
            print("Invalid menu choice. Please try again.\n")
            continue

        if not ask_to_continue():
            print("Take care. BYE!")
            break

main() 




    


