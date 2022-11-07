import requests

req = "https://api.chucknorris.io/jokes/random"
ans = requests.get(req).json()

print(ans["value"])
