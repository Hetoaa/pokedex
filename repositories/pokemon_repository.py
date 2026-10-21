import json

def get_pokemon_by_number(connexion, number):
    cursor = connexion.cursor()
    cursor.execute("SELECT * FROM pokemon WHERE number = ?", (number,))
    return cursor.fetchone()

def save_pokemon(connexion, pokemon):
    cursor = connexion.cursor()
    cursor.execute(
        """
        INSERT OR REPLACE INTO pokemon
        (number, name, name_fr, types, image_url, height, weight, evolves_from_number)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            pokemon["number"],
            pokemon["name"],
            pokemon["name_fr"],
            json.dumps(pokemon["types"], ensure_ascii=False), #Permet de mettre le type sous forme de texte et ascii pour les caractères
            pokemon["image_url"],
            pokemon["height"],
            pokemon["weight"],
            pokemon["evolves_from_number"],
        ),
    )