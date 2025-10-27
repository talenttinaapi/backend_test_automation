import requests

BASE_URL = "https://restcountries.com/v3.1/all/"

def get_all_countries():
    response = requests.get(BASE_URL)
    response.raise_for_status()
    return response.json()
