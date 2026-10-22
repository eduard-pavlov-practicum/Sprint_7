import pytest
import requests
import allure
from helpers.constants import ORDER_URL


@allure.epic("API учебного сервиса Самокат")
class TestOrderList:

    @allure.story("Получение списка заказов")
    @allure.title("Получение полного списка существующих заказов без фильтров")
    def test_orders_empty_params_returns_status_200_and_list_of_orders(self):
        response = requests.get(ORDER_URL)

        assert response.status_code == 200
        assert "orders" in response.json()
        assert isinstance(response.json()["orders"], list)
