import allure

from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper

BASE_URL = 'https://auth.truvisibility.net/en?ReturnUrl=https%3A%2F%2Fecommerce.truvisibility.net'
EMAIL_TEXT = 'evgeniyfadeev310322@gmail.com'
PASSWORD_TEXT = ':tyzAflttd22'

@allure.suite('Проверка формы авторизации')
@allure.title('Проверка авторизации при заполненной формы')
def test_empty_login_and_password(browser):
    BasePageHelper(browser).get_url(BASE_URL)
    LoginPage = LoginPageHelper(browser)
    LoginPage.input_email_field(EMAIL_TEXT)
    LoginPage.input_password_field(PASSWORD_TEXT)
    LoginPage.click_login()
