# weather_utils.py

import requests

def fetch_weather_data(api_key, city):
    """
    Fetch weather data from the weather API.
    
    Args:
        api_key (str): API key for accessing the weather API.
        city (str): Name of the city for which weather data is requested.
        
    Returns:
        dict: Weather data for the specified city.
    """
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        raise ValueError("City not found. Please enter a valid city name.")
    else:
        # Handle other API errors
        response.raise_for_status()
