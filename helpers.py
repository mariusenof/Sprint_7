import random
import string

import requests

from urls import (
    CREATE_COURIER_URL,
    LOGIN_COURIER_URL,
    DELETE_COURIER_URL
)


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def register_new_courier_and_return_login_password():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(
        CREATE_COURIER_URL,
        data=payload
    )

    if response.status_code == 201:
        return [login, password, first_name]

    return []


def get_courier_id(login, password):
    payload = {
        "login": login,
        "password": password
    }

    response = requests.post(
        LOGIN_COURIER_URL,
        data=payload
    )

    if response.status_code == 200:
        return response.json()["id"]

    return None


def delete_courier(courier_id):
    if courier_id is not None:
        return requests.delete(
            f"{DELETE_COURIER_URL}/{courier_id}"
        )

    return None