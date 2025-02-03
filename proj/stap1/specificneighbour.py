import requests, json

url= f"https://data.police.uk/api/leicestershire/NC04"
response_json = requests.get(url).json()

with open(r"proj\stap1\specificneighbourhoods.json", "w") as fp:
    json.dump(response_json, fp)