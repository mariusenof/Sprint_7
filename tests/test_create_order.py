import allure
import pytest
import requests

from data import ORDER_DATA
from urls import CREATE_ORDER_URL


@allure.suite("Создание заказа")
class TestCreateOrder:

    @allure.title("Создание заказа с цветом: {color}")
    @pytest.mark.parametrize(
        "color",
        [
            ["BLACK"],
            ["GREY"],
            ["BLACK", "GREY"]
        ]
    )
    def test_create_order_with_color_returns_track(self, color):
        payload = ORDER_DATA.copy()
        payload["color"] = color

        response = requests.post(
            CREATE_ORDER_URL,
            json=payload
        )

        assert response.status_code == 201
        assert "track" in response.json()

    @allure.title("Создание заказа без указания цвета")
    def test_create_order_without_color_returns_track(self):
        payload = ORDER_DATA.copy()

        response = requests.post(
            CREATE_ORDER_URL,
            json=payload
        )

        assert response.status_code == 201
        assert "track" in response.json()