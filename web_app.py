"""
This module provides a Flask web application for interactive lookup of nutritional information for foods.
Features:
- Home page with a searchable drop-down menu of foods and a decorative header image.
- Dynamic selection and display of nutrient data for chosen foods.
- User-friendly handling of missing foods and invalid responses.
- Loads and processes the food dataset once at startup for efficiency.
Endpoints:
- '/' or '/index': Homepage with search interface.
- '/food_content': Displays nutrient table for selected food (GET/POST).
- '/food_not_found': Handles user navigation after a search miss.
Usage:
    python3 web_app.py
"""
import pandas as pd
from flask import Flask, render_template, request
from food_data import load_clean, get_nutrients

# Load dataset once at startup for efficiency
df = load_clean()
entries = df['Main food description'].to_list()

# Dynamically create nutrient columns list (excluding food and category columns)
nutrient_columns = [
    col for col in df.columns
    if col not in ['Main food description', 'WWEIA Category description']
]

app2 = Flask(__name__)

@app2.route('/')
@app2.route('/index')
def index():
    """
    Render the homepage with interactive selection options for both food items and nutrients.
    Features:
    - A searchable drop-down menu allowing users to quickly find and select a food by typing its name. 
    - A dynamic multi-select list of available nutrient types, enabling users to customize which nutritional 
    values they wish to view for the chosen food.
    - A decorative header image for improved user experience.
    Returns:
    str: Rendered HTML template for the homepage with both food and nutrient selection capabilities.
    """
    image = 'fruitsvegg.jpg'
    # Pass nutrient_columns to template for dynamic dropdown
    return render_template('index.html', image=image, entries=entries, nutrient_columns=nutrient_columns)

@app2.route('/food_content', methods=['GET', 'POST'])
def get_content():
    """
    Lookup nutritional content for a requested food. If not found, show a friendly error page.
    GET/POST Params:
        food (str): Name of the food to look up.
        nutrients (list): List of nutrient columns to display.
    Returns:
        Rendered template with food details or 'not found' message.
    """
    food = request.args.get('food')
    nutrients = request.args.getlist('nutrients')

    # Display error message if food not found
    if food not in entries:
        image = 'celery3.png'
        return render_template('food_not_found.html', image=image, entries=entries, nutrient_columns=nutrient_columns)

    # Filter nutrients to only valid columns to prevent KeyError
    valid_nutrients = [n for n in nutrients if n in nutrient_columns]

    # If no valid nutrients selected, use defaults
    if not valid_nutrients:
        valid_nutrients = [
            'Protein (g)', 'Carbohydrate (g)', 'Sugars, total\n(g)',
            'Calcium (mg)', 'Magnesium (mg)', 'Iron\n(mg)', 'Vitamin C (mg)'
        ]

    # Use get_nutrients to filter columns
    result = get_nutrients(df, food, valid_nutrients)
    return render_template(
        'food_content.html',
        food=food,
        entries=entries,
        nutrient_columns=nutrient_columns,
        tables=[result.to_html(classes='data', header="true", index=False)]
    )

@app2.route('/food_not_found')
def get_content2():
    """
    Handle user responses when a food is not found.
    If user says 'No', show goodbye. If 'Yes', return to homepage.
    Otherwise, show invalid answer page.
    GET Params:
        yes_no (str): User's yes/no response.
    Returns:
        Rendered template based on user response.
    """
    yes_no = request.args.get('yes_no')
    if yes_no not in ('Yes', 'yes', 'YES', 'No', 'no', 'NO'):
        image = 'bye3.png'
        return render_template('invalid_answer.html', image=image)
    elif yes_no in ('No', 'no', 'NO'):
        image = 'bye3.png'
        return render_template('good_bye.html', image=image)
    else:
        image = 'fruitsvegg.jpg'
        return render_template('index.html', image=image, entries=entries, nutrient_columns=nutrient_columns)

if __name__ == "__main__":
    # -- Running Flask app --
    # Option 1: For development (default Flask server, use debug mode if needed)
    # app2.run(debug=True, port=5001)
    
    # Option 2: For production deployment, use waitress
    # from waitress import serve
    # serve(app2, host="0.0.0.0", port=8000)
    
    # Default run for this script:
    app2.run(debug=False)
