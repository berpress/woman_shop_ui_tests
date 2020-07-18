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
 Перед началом работы, необходимо выполнить команду
  ```sh
pre-commit install
```
для того, чтобы pre-commit запускался перед каждым коммитом

Принудительный запуск pre-commit:
 ```sh
pre-commit run --all-files
```
Запуск конкретного hook:
 ```sh
pre-commit run <hook_id>
```
 ### Allure
 #### Установка allure
 Для генерации отчетов необходимо установить Scoop через PowerShell
 https://scoop.sh/
 
 После чего нужно выполнить команду 
  ```sh
 scoop install allure
 ```
 в окне PowerShell
 
 #### Генерация отчетов
 После прохождения тестов сформируется папка allure_result в корневой директории проекта
  
 Для генерации отчета необходимо ввести команду в окне PowerShell
 ```sh
 allure serve ${path}\woman_shop_ui_tests\allure_result
 ```
