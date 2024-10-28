from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page.base_page import BasePage
from locators.logo_page_locators import LogoPageLocators
import allure


class LogoPage(BasePage):

    @allure.step('Пройти по логотипу Яндекс')
    def click_to_yandex(self):
        self.click_to_element(LogoPageLocators.LOGO_YANDEX)
        self.window_handles()

    @allure.step('Проверяем, что прошли на страницу Дзен')
    def verification_yandex(self, expected_url):
        self.go_to_another_page(expected_url)
        return self.get_text_from_element(LogoPageLocators.BUTTON_FIND)

    @allure.step('Пройти по логотипу Самокат')
    def click_to_scooter(self):
        self.click_to_element(LogoPageLocators.LOGO_SCOOTER)

    @allure.step('Проверяем, что на главной странице')
    def verification_scooter(self):
        return self.get_text_from_element(LogoPageLocators.ORDER_BUTTON_TOP)

