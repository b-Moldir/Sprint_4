import allure
import pytest


from data import NAME, LAST_NAME, ADDRESS, TELEPHONE_NUMBER, COMMENT
from page.order_page import OrderPage


class TestOrderPage:
    @allure.description('Проверяем, что корректно заполняется '
                        'окно Для кого самокат')
    @pytest.mark.parametrize('name, last_name, address, telephone_number, comment',
                             zip(NAME, LAST_NAME, ADDRESS,TELEPHONE_NUMBER, COMMENT))
    def test_order_page(self, driver, name, last_name, address,telephone_number, comment):
        order_page = OrderPage(driver)

        order_page.create_order(
            click_button='top',
            name=name,
            last_name=last_name,
            address=address,
            telephone_number=telephone_number,
            comment=comment
        )
        assert order_page.verification_order() == "Посмотреть статус"

        #order_page.click_order_button(click_button='middle')
        #assert order_page.verification_order() == "Заказ оформлен"



