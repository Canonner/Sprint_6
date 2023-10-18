from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_answer_text(self, question_locator, answer_locator):
        self.go_to_element(question_locator)
        self.click_element(question_locator)
        return self.get_text_element(answer_locator)
