import pytest

from model.login import UserData
from pages.application import Application


@pytest.fixture(scope="session")
def app(request):
    base_url = "http://automationpractice.com/"
    headless = request.config.getoption("--headless")
    fixture = Application(base_url, headless)
    fixture.wd.implicitly_wait(10)
    fixture.wd.maximize_window()
    yield fixture
    fixture.wd.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--base-url",
        action="store",
        default="http://automationpractice.com/",
        help="enter base_url",
    ),
    parser.addoption(
        "--username",
        action="store",
        default="orchid345617@gmail.com",
        help="enter username",
    ),
    parser.addoption(
        "--password", action="store", default="Qwerty12345", help="enter password",
    ),
    parser.addoption(
        "--headless",
        action="store",
        default=True,
        help="launching browser without gui",
    ),


@pytest.fixture(scope="session")
def login(app, request):
    app.open_main_page()
    login = request.config.getoption("--username")
    password = request.config.getoption("--password")
    user_data = UserData(login=login, password=password)
    app.login.auth(user_data)
    yield app
    app.wd.quit()
