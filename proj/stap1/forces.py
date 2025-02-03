import requests, json

url= f"https://data.police.uk/api/forces"
response_json = requests.get(url).json()

with open(r"proj\stap1\forces.json", "w") as fp:
    json.dump(response_json, fp)