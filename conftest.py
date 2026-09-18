import time

import pytest
import requests

from constants import API_BASE_URL, BASE_URL
from utils.driver_factory import WebDriverFactory


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests: chrome or firefox",
    )


@pytest.fixture
def browser_name(request):
    return request.config.getoption("--browser")


@pytest.fixture
def driver(browser_name):
    driver = WebDriverFactory.get_driver(browser_name)
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def test_user():
    email = f"testuser_{int(time.time())}@yandex.ru"
    password = "TestPass123"
    name = "TestUser"

    response = requests.post(
        f"{API_BASE_URL}/auth/register",
        json={"email": email, "password": password, "name": name},
    )
    user_data = response.json()

    user_credentials = {
        "email": email,
        "password": password,
        "name": name,
        "access_token": user_data["accessToken"],
        "refresh_token": user_data["refreshToken"],
    }

    yield user_credentials

    requests.delete(
        f"{API_BASE_URL}/auth/user",
        headers={"Authorization": user_credentials["access_token"]},
    )


@pytest.fixture
def logged_in_driver(driver, test_user):
    driver.get(BASE_URL)
    driver.execute_script(
        "window.localStorage.setItem('accessToken', arguments[0]);"
        "window.localStorage.setItem('refreshToken', arguments[1]);",
        test_user["access_token"],
        test_user["refresh_token"],
    )
    driver.refresh()
    return driver