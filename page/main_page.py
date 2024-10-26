from page.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure


class MainPage(BasePage):

    @allure.step("Прокрутить страницу до Вопросы о важном")
    def scroll_until_the_questions(self):
        locator_7 = self.change_locators(MainPageLocators.QUESTION_LOCATOR, 7)
        self.scroll_until_the_last(locator_7)

    @allure.step("Кликаем на вопроc")
    def click_question_element(self, locator_q):
        self.click(locator_q)

    @allure.step('Получаем текст с ответа')
    def get_answer_text_1(self, locator_a):
        return self.get_text_from_element(locator_a)

    def get_answer_text(self, num):
        locator_q = self.change_locators(MainPageLocators.QUESTION_LOCATOR, num)
        locator_a = self.change_locators(MainPageLocators.ANSWER_LOCATOR, num + 1)
        self.click(locator_q)
        return self.get_answer_text_1(locator_a)