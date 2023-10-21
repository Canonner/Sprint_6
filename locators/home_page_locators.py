from selenium.webdriver.common.by import By

class HomePageLocators:
    order_button = [By.XPATH, ".//div[@class='Home_FinishButton__1_cWm']/button[text() = 'Заказать']"]  # кнопка "Заказать" внизу главной страницы
    question_0 = [By.XPATH, ".//div[@id = 'accordion__heading-0']"]
    answer_0 = [By.XPATH, ".//div[@id = 'accordion__panel-0']"]  # ответ "Сутки — 400 рублей. Оплата курьеру — наличными или картой."
    question_1 = [By.XPATH, ".//div[@id = 'accordion__heading-1']"]
    answer_1 = [By.XPATH, ".//div[@id = 'accordion__panel-1']"]  # ответ "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."
    question_2 = [By.XPATH, ".//div[@id = 'accordion__heading-2']"]
    answer_2 = [By.XPATH, ".//div[@id = 'accordion__panel-2']"]  # ответ "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."
    question_3 = [By.XPATH, ".//div[@id = 'accordion__heading-3']"]
    answer_3 = [By.XPATH, ".//div[@id = 'accordion__panel-3']"]  # ответ "Только начиная с завтрашнего дня. Но скоро станем расторопнее."
    question_4 = [By.XPATH, ".//div[@id = 'accordion__heading-4']"]
    answer_4 = [By.XPATH, ".//div[@id = 'accordion__panel-4']"]  # ответ "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."
    question_5 = [By.XPATH, ".//div[@id = 'accordion__heading-5']"]
    answer_5 = [By.XPATH, ".//div[@id = 'accordion__panel-5']"]  # ответ "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."
    question_6 = [By.XPATH, ".//div[@id = 'accordion__heading-6']"]
    answer_6 = [By.XPATH, ".//div[@id = 'accordion__panel-6']"]  # ответ "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."
    question_7 = [By.XPATH, ".//div[@id = 'accordion__heading-7']"]
    answer_7 = [By.XPATH, ".//div[@id = 'accordion__panel-7']"]  # ответ "Да, обязательно. Всем самокатов! И Москве, и Московской области."
