import pytest
import allure
from common_data import FaqAnswers
from pages.home_page import HomePage


class TestFaq:

    @allure.title('Parameterized test of FAQ answers on the home page')
    @allure.description('Checking that after clicking on a specific question a correct answer is displayed')
    @pytest.mark.parametrize('question_locator, answer_locator, expected_answer_text', FaqAnswers.test_data)
    def test_question_and_answer(self, driver, question_locator, answer_locator, expected_answer_text):
        home_page = HomePage(driver)
        answer_text = home_page.get_answer_text(question_locator, answer_locator)
        assert answer_text == expected_answer_text, f"Failed to compare the answer text for {question_locator}"
