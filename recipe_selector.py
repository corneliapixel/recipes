import random

def show_menu():    # show menu for user 
    print("Welcome to the Randomized Recipe Generator!")
    print("☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰")
    print("  Any specific cravings?")
    print("☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰")
    print("  1. Vegetarian")
    print("  2. Healthy option")
    print("  3. Fastfood")
    print("  4. Cheap option")
    print("  5. Random, please!")
    print("☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰")

vegetarian_recipes = ["Vegetarian Curry with Cauliflower and Chickpeas", "Vegetable Stir-Fry", "Halloumi and Carrot Steaks", "Sweetpotato Soup with Chevre", "Enchiladas"]

healthy_recipes = ["Salmon with Quinoa", "Grilled Chicken Salad", "Tuna Salad Asian Style", "Avocado Shrimp Salad", "Pumpkin Soup"]

fastfood_recipes = ["Burgers and Fries", "Homemade Pizza", "Hot Dogs", "Mac 'n' Cheese", "Spaghetti and Meatballs"]

cheap_recipes = ["Carrot Biryani", "Nasi Goreng", "Spaghetti Carbonara", "Lentil Soup", "What's in the Fridge?"]

recipes = ["Tacos", "Chili sin carne", "Bolognese", "Korvstroganoff"]
recipe_name = (random.choice(recipes))

print(f"Idag blir det {recipe_name} till middag!")


def main (): 

    while True:
        show_menu()
        preference = input("Pick your potion: (1-5)").strip()

        if preference == '1':
            preference = random.choice(vegetarian_recipes) 

        elif preference == '2':
            preference = random.choice(healthy_recipes)

        elif preference == '3':
            preference = random.choice(fastfood_recipes)

        elif preference == '4':
            preference = random.choice(cheap_recipes) 

        elif preference == '5':
            all_recipes = (vegetarian_recipes + 
                               healthy_recipes + 
                               fastfood_recipes + 
                               cheap_recipes)
            preference = random.choice(all_recipes)

        else: 
            print("Sorry, I can't help you...\n")
            continue

        print("Analyzing cravings...")
        print("Almost there...")
        print(f"Tonight's dinner: {preference}")

main() 




    


