import requests

def get_pokemon(name: str):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        print(f"Name: {data['name'].title()}")
        print(f"ID: {data['id']}")
        print("Types:", ", ".join(t['type']['name'] for t in data['types']))
        print("Abilities:")
        for ability in data['abilities']:
            print(f" - {ability['ability']['name']}")
    except requests.exceptions.HTTPError:
        print(f"Pokémon '{name}' not found.")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

if __name__ == "__main__":
    get_pokemon("pikachu")
    get_pokemon("charizard")
