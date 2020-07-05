import pytest

from model.login import UserData
from pages.application import Application


@pytest.fixture(scope='session')
def app():
    base_url = 'http://automationpractice.com/'
    fixture = Application(base_url)
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
        default="fobiw39468@homedepinst.com",
        help="enter username",
    ),
    parser.addoption(
        "--password",
        action="store",
        default="Password11",
        help="enter password",
    ),


@pytest.fixture()
def login(app, request):
    app.open_main_page()
    login = request.config.getoption("--username")
    password = request.config.getoption("--password")
    user_data = UserData(login=login, password=password)
    app.login.auth(user_data)
