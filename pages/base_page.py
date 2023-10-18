import time
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def check_element_is_visible(self, locator):
        return Wait(self.driver, 10).until(ec.visibility_of_element_located(locator))

    def click_element(self, locator):
        Wait(self.driver, timeout=10).until(ec.visibility_of_element_located(locator)).click()

    def send_user_data(self, locator, data):
        Wait(self.driver, timeout=10).until(ec.visibility_of_element_located(locator)).send_keys(data)

    def confirm_by_pressing_return(self, locator):
        Wait(self.driver, timeout=10).until(ec.visibility_of_element_located(locator)).send_keys(Keys.RETURN)

    def get_text_element(self, locator):
        return Wait(self.driver, timeout=10).until(ec.visibility_of_element_located(locator)).text

    def go_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def switch_to_tab(self):
        handles = self.driver.window_handles
        current_handle = self.driver.current_window_handle
        next_handle = handles[(handles.index(current_handle) + 1) % len(handles)]
        self.driver.switch_to.window(next_handle)
        time.sleep(10)

    def get_current_page_url(self):
        return self.driver.current_url
