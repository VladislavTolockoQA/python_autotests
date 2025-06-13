import requests
import pytest

BASE_URL = "https://api.pokemonbattle.ru/v2"
TRAINER_ID = "IDТренера"  # ID

def test_get_trainers_status_code():
    response = requests.get(f"{BASE_URL}/trainers")
    assert response.status_code == 200, "Статус код не равен 200"

def test_trainer_name_in_response():
    response = requests.get(f"{BASE_URL}/trainers", params={"trainer_id": TRAINER_ID})
    trainer_name = "ИмяТренера"  #имя тренера
    assert trainer_name in response.text, "Имя тренера не найдено в ответе"
