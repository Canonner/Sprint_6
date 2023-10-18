from selenium.webdriver.common.by import By


class BasePageLocators:
    yandex_logo_header = [By.XPATH, ".//img[@alt = 'Yandex']"]   # логотип "Яндекс" в шапке главной страницы
    samokat_logo_header = [By.XPATH, ".//img[@alt = 'Scooter']"]  # логотип "Самокат" в шапке главной страницы
    order_button_header = [By.XPATH, ".//div[@class = 'Header_Nav__AGCXC']/button[text() = 'Заказать']"]  # кнопка "Заказать" в шапке главной страницы
    cookie_confirm_button = [By.XPATH, ".//button[@id='rcc-confirm-button']"]   # кнопка "да все привыкли"