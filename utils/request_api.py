import requests

url = f"https://rickandmortyapi.com/api/character?page=1"
r = requests.get(url)
data = r.json()

character_total = data['results'] # lista - total personajes

