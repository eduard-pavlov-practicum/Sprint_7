import pytest
import requests
import allure
from helpers.constants import ORDER_URL


@allure.epic("API учебного сервиса Самокат")
class TestOrderCreation:

    @allure.story("Создание заказа")
    @allure.title("Успешное создание заказа с различными опциями цвета")
    @allure.description("Проверяется создание заказа с одним цветом (BLACK или GREY), с обоими цветами сразу, либо вообще без указания цвета. Ожидается статус 201 и числовой трек заказа")
    @pytest.mark.parametrize("colors", [["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
    def test_orders_various_color_options_returns_status_201_and_order_track(self, dynamic_order_body, colors):
        order_body = dynamic_order_body.copy()
        order_body["color"] = colors

        response = requests.post(ORDER_URL, json=order_body)

        assert response.status_code == 201
        assert "track" in response.json()
        assert isinstance(response.json()["track"], int)
