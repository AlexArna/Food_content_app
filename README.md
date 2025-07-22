# Food Content App

## Overview

Food Content App is a dual-interface tool for searching and viewing nutrition information for foods from the [USDA FNDDS Nutrient Values dataset](https://www.ars.usda.gov/ARSUserFiles/80400530/apps/2019-2020%20FNDDS%20At%20A%20Glance%20-%20FNDDS%20Nutrient%20Values.xlsx).  
It features both a modern web application (with autocomplete and customizable nutrient selection) and an autocomplete-enabled command-line interface.  
Both interfaces share a unified data engine that automatically downloads and processes the official USDA Excel dataset, ensuring up-to-date and reliable information.

This project demonstrates practical skills in Python programming, web development with Flask, data processing with pandas, user interface design (both CLI and web), RESTful architecture, and integration of live external data sources.

---

## Tools and Technologies Used

- **Python 3** — Core programming language
- **Flask** — Web application framework for routing and template rendering
- **Jinja2** — HTML templating for dynamic content
- **pandas** — Data loading, cleaning, and manipulation
- **prompt_toolkit** — Rich CLI input with autocomplete
- **requests** — For downloading the USDA dataset
- **openpyxl** — Excel file support for pandas
- **HTML5 & CSS3** — Custom templates and responsive design
- **JavaScript (jQuery & jQuery UI)** — Autocomplete in the web interface

---

## Features

- **Web Application**
  - Search for foods with type-ahead autocomplete.
  - Select multiple nutrients to display for each food.
  - Responsive, accessible layout with custom CSS.
  - Friendly error and retry flow if a food is not found.
  - Efficient: downloads and processes the dataset only once per run.

- **Command-Line Interface**
  - Autocomplete for food names with `prompt_toolkit`.
  - Displays selected nutrients in a readable table.
  - Friendly prompts, graceful handling of unknown foods, and retry support.

- **Shared Utilities**
  - Unified data loading, cleaning, and querying code (`food_data.py` or `get_food_info.ipynb`).
  - Downloads and processes the USDA FNDDS Excel dataset automatically.

---

## Installation

From your project directory, run:
```bash
pip install -r requirements.txt
```

---

## Usage

### Web Application

1. **Run the Flask server:**
    ```bash
    python web_app.py
    ```
2. **Open your browser at:**  
   [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

3. **How it works:**
    - Start typing a food name and select from autocomplete suggestions.
    - Pick any nutrients to display.
    - Click "Submit" to view nutrient data in a table.
    - If your food is not found, follow prompts to try again or exit.

### Command-Line Interface

1. **Run the CLI app:**
    ```bash
    python cli_app.py
    ```
2. **How it works:**
    - Type a food name (autocomplete enabled).
    - If found, nutrient info is displayed.
    - If not, you're prompted to try again or exit.

---

## Jupyter Notebooks

This project also includes Jupyter notebooks used for prototyping, experimentation, and interactive data exploration:

- **notebooks/server.ipynb**  
  A version of the Flask web application designed to be run directly from a Jupyter environment. It demonstrates how to build and serve the food content web app from a notebook cell, useful for rapid prototyping and iterative development.

- **notebooks/get_food_info.ipynb**  
  Provides functions to load, clean, and query food nutrition data from the USDA FNDDS dataset.  
  - Includes both programmatic data utilities (for loading and querying food data) and interactive command-line functions (such as `check_food` and `try_again`).  
  - Originally used for exploration and early development; core logic was migrated to `food_data.py` for use in the main apps, but the notebook remains as a reference and for reproducibility.
 
**Note:** The main (production-ready) web and CLI apps do not depend on these notebooks, but the code in them is compatible and reusable.

---

## Project Structure

```
food-content-app/
│
├── web_app.py
├── cli_app.py
├── food_data.py
├── requirements.txt
├── static/
│   ├── styles/
│   │   └── style.css
│   ├── bye3.png
│   ├── celery3.png
│   └── fruitsvegg.jpg
├── templates/
│   ├── index.html
│   ├── food_content.html
│   ├── food_not_found.html
│   ├── good_bye.html
│   └── invalid_answer.html
├── notebooks/
│   ├── server.ipynb
│   └── get_food_info.ipynb
├── LICENSE
└── README.md
```

---

## License

MIT License
