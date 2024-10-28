import allure

from page.logo_page import LogoPage


class TestLogoPage:
    @allure.description(
        'Проверяем, что при на логотип Яндекс попадаем на страницу Дзен')
    def test_logo_page(self,driver):
        logo_page = LogoPage(driver)
        logo_page.click_to_yandex()
        assert logo_page.verification_yandex() == "Найти"

    @allure.description(
        'Проверяем, что при на логотип Самокат попадаем на главную страницу')
    def test_logo_page1(self,driver):
        logo_page = LogoPage(driver)
        assert logo_page.verification_scooter() == "Заказать"



