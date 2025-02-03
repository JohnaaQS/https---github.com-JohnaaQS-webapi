import requests, json

url= f"https://data.police.uk/api/leicestershire/neighbourhoods"
response_json = requests.get(url).json()

with open(r"proj\stap1\neighbourhoods.json", "w") as fp:
    json.dump(response_json, fp)