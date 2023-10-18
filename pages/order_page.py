from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators as Opl


class OrderPage(BasePage):
    name_field = Opl.input_field_name
    surname_field = Opl.input_field_surname
    address_field = Opl.input_field_address
    metro_station_field = Opl.input_field_metro_station
    metro_station_dropdown_list = Opl.dropdown_list_station
    phone_number_field = Opl.input_field_phone_number
    start_date_field = Opl.input_field_start_date
    rent_period_field = Opl.input_field_rent_period
    rent_period_dropdown_list = Opl.dropdown_menu_rent_period
    color_choice_checkbox = Opl.color_choice_checkbox

    def __init__(self, driver):
        super().__init__(driver)

    def send_user_name(self, name):
        self.send_user_data(self.name_field, name)

    def send_user_surname(self, surname):
        self.send_user_data(self.surname_field, surname)

    def send_user_address(self, address):
        self.send_user_data(self.address_field, address)

    def send_user_metro_station(self):
        self.click_element(self.metro_station_field)
        self.click_element(self.metro_station_dropdown_list)

    def send_user_phone_number(self, phone_number):
        self.send_user_data(self.phone_number_field, phone_number)

    def send_user_start_date(self, start_date):
        self.send_user_data(self.start_date_field, start_date)
        self.confirm_by_pressing_return(self.start_date_field)

    def send_user_rent_period(self):
        self.click_element(self.rent_period_field)
        self.click_element(self.rent_period_dropdown_list)

    def choose_color(self):
        self.click_element(self.color_choice_checkbox)

    def fill_user_data_form(self, name, surname, address, phone_number):
        self.send_user_name(name)
        self.send_user_surname(surname)
        self.send_user_address(address)
        self.send_user_metro_station()
        self.send_user_phone_number(phone_number)

    def fill_rent_data_form(self, start_date):
        self.send_user_start_date(start_date)
        self.send_user_rent_period()
        self.choose_color()
