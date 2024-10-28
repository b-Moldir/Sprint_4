

from locators.order_page_locators import OrderPageLocators
from page.base_page import BasePage
import allure


class OrderPage(BasePage):

    @allure.step("Заполняем окно Для кого Самокат")
    @allure.step("Кликнуть по кнопке Заказать")
    @allure.step("Заполнить поле Имя")
    @allure.step("Заполнить поле Фамилия")
    @allure.step("Заполнить поле Адрес")
    @allure.step("Заполнить поле Выбрать станцию")
    @allure.step("Заполнить поле Телефон")
    @allure.step("Кликнуть по кнопке Далее")
    @allure.step("Заполняем окно Про аренду")
    @allure.step("Заполнить поле Когда привезти самокат")
    @allure.step("Заполнить поле Срок аренды")
    @allure.step("Заполнить поле Цвет самоката")
    @allure.step("Заполнить поле Комментарий для курьера")
    @allure.step("Кликнуть по кнопке Заказать")
    @allure.step("Кликнуть по кнопке Да")
    def create_order(self, name, last_name, address, telephone_number, comment, click_button):
        self.click_order_button(click_button=click_button)
        self.add_text_to_element(OrderPageLocators.NAME_LOCATOR, name)
        self.add_text_to_element(OrderPageLocators.LAST_NAME_LOCATOR, last_name)
        self.add_text_to_element(OrderPageLocators.ADDRESS_LOCATOR, address)
        self.click_to_element(OrderPageLocators.STATION_LOCATOR)
        self.click_to_element(OrderPageLocators.SELECTED_STATION_LOCATOR)
        self.add_text_to_element(OrderPageLocators.NUMBER_LOCATOR, telephone_number)
        self.click(OrderPageLocators.NEXT_BUTTON)
        self.find_element_with_wait(OrderPageLocators.ORDER_HEADER_2)
        self.click_to_element(OrderPageLocators.WHEN_TO_BRING)
        self.find_element_with_wait(OrderPageLocators.WHEN_TO_BRING)
        self.click_to_element(OrderPageLocators.WHEN_TO_BRING_DATA)
        self.click_to_element(OrderPageLocators.RENTAL_TIME)
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD)
        self.click_to_element(OrderPageLocators.COLOUR_SCOOTER)
        self.click_to_element(OrderPageLocators.SELECTED_CHECKBOX)
        self.add_text_to_element(OrderPageLocators.COMMENTS_FOR_COURIER, comment)
        self.click(OrderPageLocators.ORDER_BUTTON2)
        self.click_to_element(OrderPageLocators.YES_BUTTON)

    @allure.step("Клик по верхней кнопки Заказать ")
    def click_top_order_button(self):
        self.click_to_element(OrderPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Прокрутка к нижней кнопке Заказать")
    def scroll_middle_order_button(self):
        middle_button = self.find_element_with_wait(OrderPageLocators.ORDER_BUTTON_MIDDLE)
        self.scroll_until_the_last(middle_button)

    @allure.step("Клик по кнопке Заказать")
    def click_order_button(self, click_button):
        if click_button == 'top':
            self.click_top_order_button()
        elif click_button == 'middle':
            self.scroll_middle_order_button()
            self.click_to_element(OrderPageLocators.ORDER_BUTTON_MIDDLE)

    @allure.step("Проверяем, что заказ создался")
    def verification_order(self):
        text = self.get_text_from_element(OrderPageLocators.ORDER_CREATED)
        return text



#


