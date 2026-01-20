from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By

import allure

class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, 'inputEmail')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="sign-in-local"]/a')
    LOGIN_PASSWORD = (By.ID, 'inputPassword')

class LoginPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверка загруженной страницы'):
            self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_EMAIL)
        self.find_element(LoginPageLocators.LOGIN_PASSWORD)
        self.find_element(LoginPageLocators.LOGIN_BUTTON)

    @allure.step('Нажимаем кнопку "Войти"')
    def click_login(self):
        self.attach_screenshot()
        self.find_element(LoginPageLocators.LOGIN_BUTTON).click()

    @allure.step('Заполняем поле "Email"')
    def input_email_field(self, email):
        self.find_element(LoginPageLocators.LOGIN_EMAIL).send_keys(email)
        self.attach_screenshot()

    @allure.step('Заполняем поле "Password"')
    def input_password_field(self, password):
        self.find_element(LoginPageLocators.LOGIN_PASSWORD).send_keys(password)
        self.attach_screenshot()