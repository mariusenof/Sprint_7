import allure
import requests

from urls import GET_ORDERS_URL


@allure.suite("Список заказов")
class TestGetOrders:

    @allure.title("Получение списка заказов")
    def test_get_orders_returns_orders_list(self):
        response = requests.get(GET_ORDERS_URL)

        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)