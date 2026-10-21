import sqlite3

def get_connection():
    connexion = sqlite3.connect("pokedex.db")
    connexion.row_factory = sqlite3.Row
    try:
        yield connexion
        connexion.commit()
    except Exception:
        connexion.rollback()
        raise
    finally:
        connexion.close()