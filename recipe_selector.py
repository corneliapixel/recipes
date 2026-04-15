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
            break

        elif preference == '2':
            break

        elif preference == '3':
            break

        elif preference == '4':
            break 

        elif preference == '5':
            break

        else: 
            print("Sorry, I can't help you...\n")

main() 




    


