import pytest

from helpers import (
    register_new_courier_and_return_login_password,
    get_courier_id,
    delete_courier
)


@pytest.fixture
def courier():
    courier_data = register_new_courier_and_return_login_password()

    yield courier_data

    courier_id = get_courier_id(
        courier_data[0],
        courier_data[1]
    )

    delete_courier(courier_id)