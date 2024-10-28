import allure

from page.logo_page import LogoPage


class TestLogoPage:
    @allure.title('Проверка при клике на логотип "Яндекс"')
    @allure.description(
        'Проверяем, что при на логотип Яндекс попадаем на страницу Дзен')
    def test_logo_page(self, driver, expected_url):
        logo_page = LogoPage(driver)
        logo_page.click_to_yandex()
        assert logo_page.verification_yandex(expected_url) == "Найти"

    @allure.title('Проверка при клике на логотип "Самокат"')
    @allure.description(
        'Проверяем, что при на логотип Самокат попадаем на главную страницу')
    def test_logo_page1(self,driver):
        logo_page = LogoPage(driver)
        assert logo_page.verification_scooter() == "Заказать"



