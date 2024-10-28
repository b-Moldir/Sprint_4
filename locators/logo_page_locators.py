from selenium.webdriver.common.by import By


class LogoPageLocators:

    LOGO_YANDEX = (By.XPATH, '//img[@alt="Yandex"]')
    TEXT_NEWS = (By.CLASS_NAME, '//*[text()="Новости"]')
    BUTTON_FIND = (By.XPATH, '//button[text()="Найти"]')
    LOGO_SCOOTER = (By.XPATH, '//img[@alt="Scooter"]')
    ORDER_BUTTON_TOP = (By.XPATH, '//button[contains(@class, "Button_Button__ra12g") and text()="Заказать"]')