import requests, json

url= f"https://data.police.uk/api/crimes-no-location?category=all-crime&date=2024-01&force=leicestershire"
response_json = requests.get(url).json()

with open(r"proj\stap1\crimesnoloc.json", "w") as fp:
    json.dump(response_json, fp)