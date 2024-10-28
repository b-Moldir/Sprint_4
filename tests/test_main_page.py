import allure
import pytest

from data import QUESTIONS_AND_ANSWERS
from page.main_page import MainPage


class TestMainPage:
    @allure.title('Проверка выпадающего списка в разделе "Вопросы о важном"')
    @allure.description(
        'Проверяем, что при клике на вопрос ответ правильный')
    @pytest.mark.parametrize('question,answer', QUESTIONS_AND_ANSWERS)
    def test_answer_and_questions(self, driver, question, answer):
        main_page = MainPage(driver)
        assert main_page.get_answer_text(question) == answer