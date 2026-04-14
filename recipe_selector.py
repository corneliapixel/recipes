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


recipes = ["Tacos", "Chili sin carne", "Bolognese", "Korvstroganoff"]
recipe_name = (random.choice(recipes))

print(f"Idag blir det {recipe_name} till middag!")




    


