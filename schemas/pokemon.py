from typing import List
from pydantic import BaseModel

#Modèle Pydantic pour données Pokémon

class Pokemon(BaseModel):
    number: int
    name: str
    name_fr: str
    types: List[str]
    image_url: str
    heigth: int
    weigth: int
    evolves_from_number: int | None

