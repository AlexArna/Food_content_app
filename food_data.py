"""
Food Data Utilities
This module provides functions to load, clean, and query nutritional data from the USDA FNDDS Excel dataset.
Intended for use by both CLI and web applications.
Usage:
    - Import this module in your CLI or web app.
    - Use load_clean() to obtain a cleaned pandas DataFrame.
    - Use get_nutrients(df, food) to retrieve nutrient info for a specified food.
    - Use get_nutrients(df, food, columns) to retrieve only selected columns (nutrients) for a specified food.
"""
import pandas as pd
import requests
from io import BytesIO

def load_clean():
    """
    Download and clean the USDA FNDDS Nutrient Values Excel dataset.
    - Downloads the Excel file from the official USDA URL.
    - Removes unnecessary columns for streamlined analysis.
    Returns:
        pd.DataFrame: Cleaned data with relevant columns.
    """
    url = 'https://www.ars.usda.gov/ARSUserFiles/80400530/apps/2019-2020%20FNDDS%20At%20A%20Glance%20-%20FNDDS%20Nutrient%20Values.xlsx'
    # Custom HTTP headers for the request:
    # - User-Agent: identifies request as coming from a browser (improves compatibility with some servers)
    # - Accept: specifies expected file format (Excel .xlsx, binary, or anything)
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet, application/octet-stream, */*"
    }
    # Send a GET request to the url with the provided headers and store the server’s response (Excel file) in response
    response = requests.get(url, headers=headers)
    # Raise an error if the download failed
    response.raise_for_status()
    # Read the Excel file from the response's raw bytes, without saving to disk
    df = pd.read_excel(BytesIO(response.content), header=1) # Column names are in the second row
    df.drop(df.iloc[:, 49:68], inplace=True, axis=1)
    df.drop(df.columns[[0, 2]], axis=1, inplace=True)
    return df

def get_nutrients(df, food, columns=None):
    """
    Retrieve nutrient information for the given food.
    Args:
        df (pd.DataFrame): The food dataset.
        food (str): The food name to query.
        columns (list or None): List of column names to return. If None, return all columns.
    Returns:
        pd.DataFrame: Nutrient values for the given food.
                      Returns empty DataFrame if food not found.
    """
    if columns is None:
        result = df.loc[df['Main food description'] == food, :]
    else:
        result = df.loc[df['Main food description'] == food, columns]
    return result