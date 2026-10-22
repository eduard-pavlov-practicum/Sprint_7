import pytest
import allure
from helpers.courier_helper import register_new_courier


class TestCourierCreation:

    @allure.story("Создание курьера")
    @allure.title("Успешное создание курьера со всеми обязательными и уникальными полями")
    @allure.description("Проверка того, что при отправке валидных данных курьер успешно регистрируется")
    def test_courier_valid_fields_returns_status_201_and_ok_true(self, courier_data):
        response = register_new_courier(courier_data)

        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.story("Создание курьера")
    @allure.title("Невозможность создания курьера с дублирующимся логином")
    @allure.description("Вызываем создание курьера дважды с одинаковыми данными. Второй запрос должен вернуть 409")
    def test_courier_duplicate_login_returns_status_409_and_error_message(self, courier_data):
        register_new_courier(courier_data)

        response = register_new_courier(courier_data)

        assert response.status_code == 409
        assert "Этот логин уже используется" in response.json().get("message", "")

    @allure.story("Создание курьера")
    @allure.title("Ошибка создания курьера при отсутствии обязательного поля")
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_courier_missing_required_field_returns_status_400_and_error_message(self, courier_data, missing_field):
        del courier_data[missing_field]
        response = register_new_courier(courier_data)

        assert response.status_code == 400
        assert "Недостаточно данных для создания учетной записи" in response.json().get("message", "")
