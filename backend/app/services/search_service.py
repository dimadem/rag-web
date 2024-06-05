import requests

def fetch_data_from_internet(url):
    response = requests.get(url)
    return response.json()