import allure
import requests

from urls import LOGIN_COURIER_URL


@allure.suite("Логин курьера")
class TestLoginCourier:

    @allure.title("Успешная авторизация курьера")
    def test_login_courier_success(self, courier):
        payload = {
            "login": courier[0],
            "password": courier[1]
        }

        response = requests.post(
            LOGIN_COURIER_URL,
            data=payload
        )

        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Авторизация без логина")
    def test_login_courier_without_login_returns_error(self, courier):
        payload = {
            "password": courier[1]
        }

        response = requests.post(
            LOGIN_COURIER_URL,
            data=payload
        )

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Авторизация без пароля")
    def test_login_courier_without_password_returns_error(self, courier):
        payload = {
            "login": courier[0]
        }

        response = requests.post(
            LOGIN_COURIER_URL,
            data=payload
        )

        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Авторизация с неверным логином")
    def test_login_courier_with_wrong_login_returns_error(self, courier):
        payload = {
            "login": courier[0] + "wrong",
            "password": courier[1]
        }

        response = requests.post(
            LOGIN_COURIER_URL,
            data=payload
        )

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Авторизация с неверным паролем")
    def test_login_courier_with_wrong_password_returns_error(self, courier):
        payload = {
            "login": courier[0],
            "password": courier[1] + "wrong"
        }

        response = requests.post(
            LOGIN_COURIER_URL,
            data=payload
        )

        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"