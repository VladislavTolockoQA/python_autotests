import requests

# Базовые данные
URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "ТокенСюда"  # токен
HEADERS = {
    "Content-Type": "application/json",
    "trainer_token": TOKEN
}

# 1. Создание покемона
create_data = {
    "name": "Бульбазавр",
    "photo_id": 12
}
response_create = requests.post(f"{URL}/pokemons", headers=HEADERS, json=create_data)
print("Создание покемона:")
print(response_create.json())

pokemon_id = response_create.json().get("id")  #ID для следующих шагов

# 2. Изменение имени покемона
edit_data = {
    "pokemon_id": pokemon_id,
    "name": "Иви",
    "photo_id": 12
}
response_edit = requests.put(f"{URL}/pokemons", headers=HEADERS, json=edit_data)
print("\nИзменение имени покемона:")
print(response_edit.json())

# 3. Поймать покемона в покебол
pokeball_data = {
    "pokemon_id": pokemon_id
}
response_pokeball = requests.post(f"{URL}/trainers/add_pokeball", headers=HEADERS, json=pokeball_data)
print("\nПоймать покемона в покебол:")
print(response_pokeball.json())
