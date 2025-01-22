from amadeus import Client, ResponseError
from dotenv import load_dotenv
import os

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
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode='MAD',
            destinationLocationCode='ATH',
            departureDate='2025-02-01',
            adults=1)
        # print(response.body) #=> The raw response, as a string
        # print(response.result) #=> The body parsed as JSON, if the result was parsable
        print(response.data) #=> The list of locations, extracted from the JSON
    except ResponseError as error:
        print(error)

if __name__ == '__main__':
    main()