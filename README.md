[![Build Status](https://travis-ci.org/berpress/woman_shop_ui_tests.svg?branch=master)](https://travis-ci.org/berpress/woman_shop_ui_tests)
# Автотесты для онлайн магазина

# UI tests

  - Добавлены новые тесты
  - Дата создания проекта 05.07.2020

### Установка

Необходимо установить все зависимости из requirements.txt

```sh
pip install -r requirements.txt
```

 ### Запуск

Необходимо установить все зависимости из requirements.txt
Перед запуском создайте виртуальное окружение

```sh
pip install virtualenv
virtualenv <env_name>
pytest
```
 ### Pre-commit-hooks
 Pre-commit запускается при каждом коммите в ветку.
 Для принудительного запуска используется команда
 ```sh
pre-commit run --all-files
```
Для запуска конкретного hook используется команда
 ```sh
pre-commit run <hook_id>
```
