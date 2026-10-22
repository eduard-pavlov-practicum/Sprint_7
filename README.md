# Sprint_7

### Установка зависимостей
```bash
pip install -r ./requirements.txt
```

### Запуск тестов

```bash
pytest tests/* --alluredir=allure_results 
```

### Создание отчета о тестировании (allure)

```bash
allure generate allure_results
```