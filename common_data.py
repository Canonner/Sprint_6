import datetime as dt
from datetime import date as d
from locators.home_page_locators import HomePageLocators as Hpl
from locators.base_page_locators import BasePageLocators as Bpl


class Urls:
    main_url = 'https://qa-scooter.praktikum-services.ru/'
    dzen_url = 'https://dzen.ru/?yredirect=true'


class FaqAnswers:
    test_data = [
        (Hpl.question_0, Hpl.answer_0, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
        (Hpl.question_1, Hpl.answer_1, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
        (Hpl.question_2, Hpl.answer_2, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
        (Hpl.question_3, Hpl.answer_3, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
        (Hpl.question_4, Hpl.answer_4, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
        (Hpl.question_5, Hpl.answer_5, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
        (Hpl.question_6, Hpl.answer_6, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
        (Hpl.question_7, Hpl.answer_7, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'),
    ]


class OrderData:
    name = 'Гржегорж'
    surname = 'Бженчишчикевич'
    address = 'ул. 1 сентября, д 13, кв 39'
    phone_number = '+79998887766'
    start_date = (d.today() + dt.timedelta(days=1)).strftime("%d.%m.%Y")
    rent_period = 1
    color = 'black'
    order_buttons = [
        (Bpl.order_button_header, "Заказать в шапке страницы"),
        (Hpl.order_button, "Заказать внизу страницы"),
    ]


print(FaqAnswers.test_data[1])