from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By

import allure

class AccountPageLocators:
    ECOMMERCE_LINKS = (By.XPATH, '//body//app-root//a[12]')

class AccountPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверка загруженной страницы'):
            self.attach_screenshot()
        self.find_element(AccountPageLocators.ECOMMERCE_LINKS)


    @allure.step('Нажимаем кнопку "Войти"')
    def click_ecommerce(self):
        self.attach_screenshot()
        self.find_element(AccountPageLocators.ECOMMERCE_LINKS).click()