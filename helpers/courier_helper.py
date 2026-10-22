import pytest
import requests
import allure
from .constants import CREATE_COURIER_URL, LOGIN_COURIER_URL


@allure.step('Регистрируем курьера {courier_body}')
def register_new_courier(courier_body):
    return requests.post(CREATE_COURIER_URL, data=courier_body)


@allure.step('Логиним курьера {payload}')
def login_courier(payload):
    return requests.post(LOGIN_COURIER_URL, data=payload)
