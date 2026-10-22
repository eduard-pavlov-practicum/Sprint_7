import pytest
import allure
from helpers.courier_helper import register_new_courier, login_courier
from helpers.constants import LOGIN_COURIER_URL


class TestCourierLogin:
    @allure.story("Авторизация курьера")
    @allure.title("Успешная авторизация курьера с валидными учетными данными")
    def test_login_valid_credentials_returns_status_200_and_courier_id(self, courier_data):
        register_new_courier(courier_data)

        payload = {"login": courier_data["login"],
                   "password": courier_data["password"]}
        response = login_courier(payload)

        assert response.status_code == 200
        assert "id" in response.json()
        assert isinstance(response.json()["id"], int)

    @allure.story("Авторизация курьера")
    @allure.title("Ошибка авторизации при отсутствии обязательного поля в запросе")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_login_missing_required_field_returns_status_400_and_error_message(self, courier_data, missing_field):
        register_new_courier(courier_data)

        payload = {"login": courier_data["login"],
                   "password": courier_data["password"]}
        del payload[missing_field]
        response = login_courier(payload)

        assert response.status_code == 400
        assert "Недостаточно данных для входа" in response.json().get("message", "")

    @allure.story("Авторизация курьера")
    @allure.title("Ошибка авторизации при указании неверного логина или пароля")
    @pytest.mark.parametrize("wrong_field", ["login", "password"])
    def test_login_wrong_credential_returns_status_404_and_error_message(self, courier_data, wrong_field):
        register_new_courier(courier_data)

        payload = {"login": courier_data["login"],
                   "password": courier_data["password"]}
        payload[wrong_field] += "_invalid"
        response = login_courier(payload)

        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.json().get("message", "")

    @allure.story("Авторизация курьера")
    @allure.title("Ошибка авторизации под полностью несуществующим пользователем")
    def test_login_non_existent_courier_returns_status_404_and_error_message(self, generate_random_string):
        payload = {
            "login": generate_random_string(12),
            "password": generate_random_string(12)
        }
        response = login_courier(payload)

        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.json().get("message", "")
