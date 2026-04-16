import random
import time

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


def show_recipe(recipe):
    print("Analyzing cravings...")
    time.sleep(2)
    print("Almost there...\n")
    time.sleep(1)
    print(f"Tonight's dinner: {recipe}\n")
    time.sleep(1)


def ask_to_continue():
    return input("Want another round? (y/n): ").strip().lower() in ("yes", "y", "ja", "yas")


def main (): 

    while True:
        show_menu()
        preference = input("Pick your potion: (1-6)\t").strip()
        print("")

        if preference in choice_mapping:
            category = choice_mapping[preference]
            recipe = random.choice(recipes[category]) 

        elif preference == "5":
            all_recipes = []
            for category in recipes.values():
                all_recipes.extend(category)
            recipe = random.choice(all_recipes)

        elif preference == '6':
            print("I guess there is always Foodora...\n")
            print("Take care. BYE!\n")
            break

        else: 
            print("Sorry, I can't help you...\n")
            continue

        show_recipe(recipe)

        if not ask_to_continue():
            print("Take care. BYE!")
            break

main() 




    


