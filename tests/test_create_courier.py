import allure
import pytest
import requests

from helpers import (
    generate_random_string,
    register_new_courier_and_return_login_password,
    get_courier_id,
    delete_courier
)
from urls import CREATE_COURIER_URL


@allure.suite("Создание курьера")
class TestCreateCourier:

    @allure.title("Успешное создание курьера")
    def test_create_courier_success(self):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }

        response = requests.post(
            CREATE_COURIER_URL,
            data=payload
        )

        assert response.status_code == 201
        assert response.json() == {"ok": True}

        courier_id = get_courier_id(
            payload["login"],
            payload["password"]
        )
        delete_courier(courier_id)

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier_returns_error(self):
        courier_data = register_new_courier_and_return_login_password()

        payload = {
            "login": courier_data[0],
            "password": courier_data[1],
            "firstName": courier_data[2]
        }

        response = requests.post(
            CREATE_COURIER_URL,
            data=payload
        )

        assert response.status_code == 409
        assert response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

        courier_id = get_courier_id(
            courier_data[0],
            courier_data[1]
        )
        delete_courier(courier_id)

    @allure.title("Создание курьера без обязательного поля: {missing_field}")
    @pytest.mark.parametrize(
        "missing_field",
        [
            "login",
            "password"
        ]
    )
    def test_create_courier_without_required_field_returns_error(self, missing_field):
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }

        del payload[missing_field]

        response = requests.post(
            CREATE_COURIER_URL,
            data=payload
        )

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для создания учетной записи"