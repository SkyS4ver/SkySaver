# Find the cheapest destinations where you can fly to from a given location

from amadeus import Client, ResponseError
from dotenv import load_dotenv
import os
import json

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer les clés API
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

# Initialize using parameters
amadeus = Client(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET
)

def main():
    try:
        response = amadeus.shopping.flight_destinations.get(origin='LON')
        
        data = response.result

        with open('Data/Files/cheapest_flight_with_origin.json', 'w', encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        print("Données sauvegardées dans 'cheapest_flight_with_origin.json'.")

    except ResponseError as error:
        print(f"Erreur : {error}")

if __name__ == '__main__':
    main()