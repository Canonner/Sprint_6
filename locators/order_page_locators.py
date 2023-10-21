from selenium.webdriver.common.by import By

from common_data import OrderData


class OrderPageLocators:
    user_form_header = [By.XPATH, ".//div[text()='Для кого самокат']"]   # Заголовок "Для кого самокат"
    input_field_name = [By.XPATH, ".//input[@placeholder='* Имя']"]   # Поле ввода "Имя"
    input_field_surname = [By.XPATH, ".//input[@placeholder='* Фамилия']"]   # Поле ввода "Фамилия"
    input_field_address = [By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']"]   # Поле ввода "Адрес"
    input_field_metro_station = [By.XPATH, ".//input[@placeholder='* Станция метро']"]  # Поле ввода "Станция метро"
    dropdown_list_station = [By.XPATH, ".//div[@class='select-search__select']"]  # Выпадающий список выбора станции
    input_field_phone_number = [By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']"]   # Поле ввода "Телефон"
    next_button = [By.XPATH, ".//button[text()='Далее']"]   # Кнопка "Далее"
    rent_form_header = [By.XPATH, ".//div[text()='Про аренду']"]   # Заголовок "Для кого самокат"
    input_field_start_date = [By.XPATH, ".//input[@placeholder='* Когда привезти самокат']"]   # Поле ввода "Когда привезти самокат"
    input_field_rent_period = [By.XPATH, ".//div[@class='Dropdown-placeholder']"]   # Поле выбора "Срок аренды"
    dropdown_menu_rent_period = [By.XPATH, f".//div[@class='Dropdown-option'][{OrderData.rent_period}]"]   # # Первый пункт в выпадающем списке выбора срока аренды
    color_choice_checkbox = [By.XPATH, f".//input[@id='{OrderData.color}']"]   # Чекбокс выбора цвета
    order_button_finish = [By.XPATH, ".//div[@class='Order_Buttons__1xGrp']//button[text()='Заказать']"]   # кнопка "Заказать" на странице ввода данных об аренде
    confirm_order_header = [By.XPATH, ".//div[@class='Order_Buttons__1xGrp']//button[text()='Заказать']"]   # Заголовок окна подтверждения заказа
    confirm_order_button = [By.XPATH, ".//button[contains(text(), 'Да')]"]   # кнопка "Да" окна подтверждения заказа
    confirmation_header = [By.XPATH, ".//div[text()='Заказ оформлен']"]   # Заголовок всплывающего окна с сообщением об успешном создании заказа.
