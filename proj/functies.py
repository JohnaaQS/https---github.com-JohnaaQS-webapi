import requests


def neighbourhoods(hood: str) -> dict:
    url= f"https://data.police.uk/api/{hood}/neighbourhoods"
    response_json = requests.get(url).json()
    return response_json

def forces() -> dict:
    " Geef de verschillende forces. "
    url= f"https://data.police.uk/api/forces"
    response_json = requests.get(url).json()
    return response_json

def specificneighbourhood(hood: str ,code: str) -> dict:
    " Geef de verschillende wijken. "
    url= f"https://data.police.uk/api/{hood}/{code}"
    response_json = requests.get(url).json()
    return response_json


def crimes_no_loc(hood: str) -> list:
    "geef de criminele activiteiten."
    url = f"https://data.police.uk/api/crimes-no-location?category=all-crime&date=2024-01&force={hood}"
    response_json = requests.get(url).json()
    return response_json

"""
zonder date 
url = f"https://data.police.uk/api/crimes-no-location?category=all-crime&force={hood}"

# def stopandsearch() -> dict:
#     " Geef de verschillende forces. "
#     url= f"https://data.police.uk/api/stops-street?date=2024-01&lat=52.629729&lng=-1.131592"
#     response_json = requests.get(url).json()
#     return response_json

def street_crimes() -> dict:
    " Geef een criminele activiteit in de wijk. "
    url= f"https://data.police.uk/api/crimes-street/all-crime?date=2024-01&poly=52.268,0.543:52.794,0.238:52.130,0.478"
    response_json = requests.get(url).json()
    return response_json
"""
