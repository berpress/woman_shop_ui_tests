import os
from datetime import datetime

import allure
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


@pytest.fixture(scope="module")
def login(app, request):
    app.open_main_page()
    login = request.config.getoption("--username")
    password = request.config.getoption("--password")
    user_data = UserData(login=login, password=password)
    app.login.auth(user_data)
    yield app
    app.open_main_page()
    app.login.logout_button_click()


PATH=lambda p:os.path.abspath(
        os.path.join(os.path.dirname(__file__),'..',p)
        )


@pytest.mark.hookwrapper(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call':
        if 'app' in item.fixturenames:
            driver = item.funcargs['app']
        xfail = hasattr(report, 'wasxfail')
        # create file
        add_name = '{}_{}'.format(report.nodeid.split("::")[1],
                                  datetime.now().strftime("%Y-%m-%d_%H.%M.%S"))
        file_name = PATH(os.path.abspath(os.curdir) + '/' + add_name + '.png')
        driver.wd.get_screenshot_as_file(file_name)
        if (report.skipped and xfail) or (report.failed and not xfail):
            cp_file_name = add_name + ".png"
            # only add additional html on failure
            html = '<div><img src=' + cp_file_name + ' alt="screenshot" style="width:304px;height:228px;" '
            extra.append(pytest_html.extras.html(html))
        report.extra = extra


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'app' in item.fixturenames:
                    web_driver = item.funcargs['app']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.wd.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'app' in item.fixturenames:
                    web_driver = item.funcargs['app']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.wd.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))
