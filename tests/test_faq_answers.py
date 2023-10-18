import pytest
from tests.common_data import FaqAnswers
from pages.home_page import HomePage


class TestFaq:

    @pytest.mark.parametrize('question_locator, answer_locator, expected_answer_text', FaqAnswers.test_data)
    def test_question_and_answer(self, driver, question_locator, answer_locator, expected_answer_text):
        home_page = HomePage(driver)
        answer_text = home_page.get_answer_text(question_locator, answer_locator)
        assert answer_text == expected_answer_text
