# Randomized Recipe Generator 

## Description

A Python program that helps you decide what to eat by generating a random recipe based on your preferences. You can also skip setting preferences and get a random recipe picked out for you from all existing categories.

The program also logs generated recipes to a file.

## Features

* Interactive menu in the terminal
* Choose betweeen multiple recipe categories:
    * Vegetarian
    * Healthy
    * Fast food
    * Cheap food
* Generate random recipes
* Charming output messages
* Log generated recipes to `show_history.log` 
* All generated recipes are saved with date and time
* View recipe history from previous sessions

## How it works

1. The user selects preference (category) or random
2. A recipe is generated
3. The result (category & recipe) is displayed in the terminal
4. The recipe is saved to a log file with timestamp
5. The user can choose to generate another recipe

## Logging

The program uses Python's built-in `logging` module.

Each generated recipe is saved in: 
` show_history.log`


## Requirements

* Python 3


## Installation

1. Clone the repository: 
``` git clone https://github.com/corneliapixel/recipes.git ```

2. Python environment setup:
- Open the terminal and run the following command to double-check Python 3 installation:
(This command shows your current installed Python 3 version)
``` python --version ```
- If not installed: run following command for installation: 
``` sudo apt install python3 ```

## How to Run
1. Open the terminal
2. Navigate to project folder 
3. Run:
``` python3 recipe_generator.py ```


## Project structure
recipes/  
├── recipe_generator.py 
├── show_history.log
└── README.md 




