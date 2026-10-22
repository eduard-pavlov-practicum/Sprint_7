import pytest
import requests
import random
import string
from faker import Faker


fake = Faker(locale="ru_RU")


@pytest.fixture
def generate_random_string():
    def _generate(length=10):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))
    return _generate


@pytest.fixture
def courier_data(generate_random_string):
    """Генерирует валидные и уникальные данные для нового курьера"""
    return {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstName": generate_random_string(10)
    }


@pytest.fixture
def dynamic_order_body():
    """
    Генерирует случайные реалистичные данные для заказа с помощью Faker.
    """
    return {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "address": fake.street_address(),
        "metroStation": random.randint(1, 10),
        "phone": fake.phone_number(),
        "rentTime": random.randint(1, 7),
        "deliveryDate": fake.date_between(start_date="today", end_date="+30d").strftime("%Y-%m-%d"),
        "comment": fake.sentence(nb_words=5)
    }
