import requests

POKEAPI_URL = "https://pokeapi.co/api/v2"


def get_pokemon_from_api(number):
    url = f"{POKEAPI_URL}/pokemon/{number}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()