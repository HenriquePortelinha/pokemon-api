import requests
from pokemon_app.models import Pokemon

def fetch_and_save_pokemon_data():
    url = "https://pokeapi.co/api/v2/pokemon?limit=10"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        for item in data["results"]:
            # Corrigido: Chamar o método json() corretamente
            details = requests.get(item["url"]).json()
            
            # Certifique-se de que a resposta contenha os dados esperados
            pokemon, created = Pokemon.objects.get_or_create(
                name=details["name"], 
                type=details["types"][0]["type"]["name"], 
                image_url=details["sprites"]["front_default"]
            )
            
            if created:
                print(f"Pokemon {pokemon.name} adicionado ao banco de dados")
    else:
        print("Erro ao obter dados da API")
