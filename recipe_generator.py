import random

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
    print("☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰☰")

vegetarian_recipes = ["Vegetarian Curry with Cauliflower and Chickpeas", "Vegetable Stir-Fry", "Halloumi and Carrot Steaks", "Sweetpotato Soup with Chevre", "Enchiladas"]

healthy_recipes = ["Salmon with Quinoa", "Grilled Chicken Salad", "Tuna Salad Asian Style", "Avocado Shrimp Salad", "Pumpkin Soup"]

fastfood_recipes = ["Burgers and Fries", "Homemade Pizza", "Hot Dogs", "Mac 'n' Cheese", "Spaghetti and Meatballs"]

cheap_recipes = ["Carrot Biryani", "Nasi Goreng", "Spaghetti Carbonara", "Lentil Soup", "What's in the Fridge?"]


def main (): 

    while True:
        show_menu()
        preference = input("Pick your potion: (1-5)\t").strip()
        print("")

        if preference == '1':
            recipe = random.choice(vegetarian_recipes) 

        elif preference == '2':
            recipe = random.choice(healthy_recipes)

        elif preference == '3':
            recipe = random.choice(fastfood_recipes)

        elif preference == '4':
            recipe = random.choice(cheap_recipes) 

        elif preference == '5':
            all_recipes = (vegetarian_recipes + 
                               healthy_recipes + 
                               fastfood_recipes + 
                               cheap_recipes)
            recipe = random.choice(all_recipes)

        else: 
            print("Sorry, I can't help you...\n")
            continue

        print("Analyzing cravings...")
        print("Almost there...")
        print(f"Tonight's dinner: {recipe}\n")

main() 




    


