from fastapi import FastAPI
import requests
from schemas.pokemon import Pokemon
from db.database import get_connection

app = FastAPI()

#Fonction GET Health qui permet d'avoir le status de l'API

@app.get("/health") 
def getHealth ():
    return{"status":"ok"}

#Fonction GET Pokemon qui permet de trouver un pokemon en fonction de son numéro "ID"

@app.get("/pokemons/{number}", response_model=Pokemon)           
def getPokemon (number: int):
    url = f"https://pokeapi.co/api/v2/pokemon/{number}" #On vient pointer sur l'url avec le numéro choisit sur Postman
    response = requests.get(url)        #On vient stocker toutes les données dans la variable "response"
    data = response.json()              #On vient transformer les données en format json
    return {
        "id": data["id"],               #On regarder l'id égal à celui choisit dans Postman
        "name": data["name"],           #Le nom en anglais
        "height": data["height"],       #La taille
        "weight": data["weight"],       #Le poids
    }

