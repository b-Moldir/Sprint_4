import pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()


@pytest.fixture()
def expected_url():
    return "https://dzen.ru/?yredirect=true"