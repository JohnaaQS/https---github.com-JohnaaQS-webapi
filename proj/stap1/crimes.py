import requests, json

url= f"https://data.police.uk/api/crimes-street/all-crime?date=2024-01&lat=52.629729&lng=-1.131592"
response_json = requests.get(url).json()

with open(r"proj\stap1\crimes.json", "w") as fp:
    json.dump(response_json, fp)