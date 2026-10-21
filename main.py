import requests
from fastapi import FastAPI, HTTPException, Depends
from clients.pokeapi import get_pokemon_from_api
from db.database import get_connection
from repositories.pokemon_repository import save_pokemon

app = FastAPI()

#Fonction GET Health qui permet d'avoir le status de l'API

@app.get("/health") 
def getHealth ():
    return{"status":"ok"}

#Fonction GET Pokemon qui permet de trouver un pokemon en fonction de son numéro "ID"

@app.get("/pokemons/{number}")
def getPokemon(number: int):
    url = f"https://pokeapi.co/api/v2/pokemon/{number}"     #On vient pointer sur l'url avec le numéro choisit sur Postman
    response = requests.get(url)        #On vient stocker toutes les données dans la variable "response"
    
    if response.status_code != 200:
        raise HTTPException(status_code=404, detail="Pokémon introuvable")

    data = response.json()              #On vient transformer les données en format json
    return {
        "number": data["id"],           #On regarder l'id égal à celui choisit dans Postman
        "name": data["name"],           #Le nom en anglais
        "height": data["height"],       #La taille
        "weight": data["weight"],       #Le poids
    }

#Fonction GET Scan qui récupère un seul pokemon sur PokéAPI et l'enregistre dans la db

@app.get("/pokemons/{number}/scan")
def scanPokemon(number: int, connexion=Depends(get_connection)):
    try:
        data = get_pokemon_from_api(number)
    except requests.HTTPError:
        raise HTTPException(status_code=404, detail="Pokémon introuvable")
    except requests.RequestException:
        raise HTTPException(status_code=502, detail="PokéAPI indisponible")

    pokemon = {
        "number": data["id"],
        "name": data["name"],
        "name_fr": data["name"],
        "types": [t["type"]["name"] for t in data["types"]],
        "image_url": data["sprites"]["front_default"],
        "height": data["height"] * 10,
        "weight": data["weight"] * 100,
        "evolves_from_number": None,
    }

    save_pokemon(connexion, pokemon)
    return pokemon