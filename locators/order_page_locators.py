from selenium.webdriver.common.by import By



class OrderPageLocators:
    ORDER_BUTTON_TOP = (By.XPATH, '//button[1][contains(text(),"Заказать")][@class="Button_Button__ra12g"]')
    ORDER_BUTTON_MIDDLE = (By.XPATH, '//button[1][contains(text(),"Заказать")][@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    ORDER_BUTTON = (By.CLASS_NAME, 'Button_Button__ra12g Button_Middle__1CSJM')
    NAME_LOCATOR = (By.XPATH, '//input[@placeholder = "* Имя"]')
    LAST_NAME_LOCATOR = (By.XPATH, '//input[@placeholder = "* Фамилия"]')
    ADDRESS_LOCATOR = (By.XPATH, '//input[@placeholder = "* Адрес: куда привезти заказ"]')
    STATION_LOCATOR = By.XPATH, "//input[@placeholder='* Станция метро']"
    SELECTED_STATION_LOCATOR = By.XPATH, "//*[text()='Бульвар Рокоссовского']"
    NUMBER_LOCATOR = (By.XPATH, '//input[@placeholder = "* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, '//*[text()="Далее"]')
    ORDER_HEADER_2 = (By.XPATH, '//*[text()="Про аренду"]')
    WHEN_TO_BRING = (By.XPATH, '//input[@placeholder = "* Когда привезти самокат"]')
    WHEN_TO_BRING_DATA = (By.XPATH, '//*[@aria-label="Choose суббота, 26-е октября 2024 г."]')
    RENTAL_TIME = (By.XPATH, '//*[text()="* Срок аренды"]')
    RENTAL_PERIOD = (By.XPATH, '//*[text()="двое суток"]')
    COLOUR_SCOOTER = (By.XPATH, '//*[text()="Цвет самоката"]')
    SELECTED_CHECKBOX = (By.XPATH, '//*[@for="black"]')
    COMMENTS_FOR_COURIER = (By.XPATH, '//input[@placeholder = "Комментарий для курьера"]')
    ORDER_BUTTON2 = (By.XPATH, '//*[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Заказать"]')
    ORDER_PLACE = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')
    YES_BUTTON = (By.XPATH, '//button[2][contains(text(),"Да")]')
    ORDER_CREATED = (By.XPATH, '//*[(text()="Посмотреть статус")]')



