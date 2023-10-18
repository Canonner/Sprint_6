import pytest
from pages.home_page import HomePage
from pages.order_page import OrderPage
from locators.base_page_locators import BasePageLocators as Bpl
from locators.order_page_locators import OrderPageLocators as Opl
from tests.common_data import OrderData


class TestOrderPlacement:

    @pytest.mark.parametrize("order_button_locator, button_description", OrderData.order_buttons)
    def test_order_placement(self, driver, order_button_locator, button_description):
        home_page = HomePage(driver)
        home_page.click_element(Bpl.cookie_confirm_button)
        home_page.click_element(order_button_locator)
        order_page = OrderPage(driver)
        order_page.fill_user_data_form(OrderData.name, OrderData.surname, OrderData.address, OrderData.phone_number)
        order_page.click_element(Opl.next_button)
        order_page.fill_rent_data_form(OrderData.start_date)
        order_page.click_element(Opl.order_button_finish)
        order_page.check_element_is_visible(Opl.confirm_order_header)
        order_page.click_element(Opl.confirm_order_button)
        assert order_page.check_element_is_visible(Opl.confirmation_header), f"Failed to place order using {button_description}"
