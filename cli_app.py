"""
This module provides a command-line interface for users to look up nutrient information for foods.
Features:
- Autocomplete suggestions for food names (start typing and use TAB/arrow keys)
- Option to search multiple foods per session
- Friendly prompts and error handling
Usage:
    python3 cli_app.py
"""
from food_data import load_clean, get_nutrients
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

def is_food_in_food_list(food_list, food):
    """Return True if the food is in the food list."""
    return food in food_list

def get_input_with_autocomplete(food_list):
    """Prompt the user for a food name with autocomplete and return it."""
    completer = WordCompleter(food_list, ignore_case=True, sentence=True)
    return prompt("\nPlease enter a food name: ", completer=completer).strip()

def try_again():
    """Prompt the user to try again and return True/False."""
    ans = input("\nDo you want to try again? (yes/no): ").strip().lower()
    if ans not in ("yes", "no"):
        print("\nSorry, that was not the answer I expected.")
        return False
    return ans == "yes"

def display_nutrients(df, food, columns=None):
    """Display selected nutrients for the food."""
    result = get_nutrients(df, food, columns)
    print(result.to_string(index=False))

def main():
    print("\nWelcome to the Nutrition CLI!")
    print("\nLoading food database, please wait...")
    df = load_clean()
    food_list = list(df['Main food description'].unique())
    columns = [
        'Protein (g)', 'Carbohydrate (g)', 'Sugars, total\n(g)', 
        'Calcium (mg)', 'Magnesium (mg)', 'Iron\n(mg)', 'Vitamin C (mg)'
    ]
    while True:
        print("\nTip: Start typing a food name and press TAB or use arrow keys to navigate. Press ENTER to select.")
        food = get_input_with_autocomplete(food_list)
        if is_food_in_food_list(food_list, food):
            print("\nOk! Here are the nutrient details about", food,":\n")
            display_nutrients(df, food, columns)
        else:
            print("\nSorry, this food name is not in the database.")
        if not try_again():
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()