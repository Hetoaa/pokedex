from fastapi import FastAPI
import requests

app = FastAPI()

#Fonction GET Health qui permet d'avoir le status de l'API

@app.get("/health") 
def getHealth ():
    return{"status":"ok"}

#Fonction GET Pokemon qui permet de trouver un pokemon en fonction de son numéro "ID"

@app.get("/pokemon/{number}")           #Attention il y a un "s" à la fin de pokemon dans le sujet ce qui mène à un "not found" 
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

