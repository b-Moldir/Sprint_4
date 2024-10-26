from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page.base_page import BasePage
from locators.logo_page_locators import LogoPageLocators
import allure


class LogoPage(BasePage):

    allure.step("Пройти по логотипу Яндекс")
    def click_to_yandex(self):
        self.click_to_element(LogoPageLocators.LOGO_YANDEX)

    @allure.step('Проверяем, что прошли на страницу Дзен')
    def verification_yandex(self):
        expected_url = 'https://dzen.ru/?yredirect=true'
        WebDriverWait(self.driver, 20).until(expected_conditions.url_to_be(expected_url))  # Увеличиваем время ожидания
        current_url = self.driver.current_url
        assert current_url == expected_url, f"Ожидался URL: {expected_url}, получен: {current_url}"
# Не могу понять в чем ошибка, открывается страница дзен. Там открывается реклама, пробовала закрыть ее через popup
    # все равно не получается



    allure.step("Пройти по логотипу Самокат")
    def click_to_scooter(self):
        self.click_to_element(LogoPageLocators.LOGO_SCOOTER)

    @allure.step('Проверяем, что на главной странице')
    def verification_scooter(self):
        return self.get_text_from_element(LogoPageLocators.ORDER_BUTTON_TOP)

