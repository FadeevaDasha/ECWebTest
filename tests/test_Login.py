import allure

from core.Links import Links
from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.AccountPage import AccountPageHelper

EMAIL_TEXT = 'evgeniyfadeev310322@gmail.com'
PASSWORD_TEXT = ':tyzAflttd22'

@allure.suite('Проверка формы авторизации')
@allure.title('Проверка авторизации при заполненной формы')
def test_valid_login_and_password(browser):
    BasePageHelper(browser).get_url(Links.AUTH)
    LoginPage = LoginPageHelper(browser)
    LoginPage.input_email_field(EMAIL_TEXT)
    LoginPage.input_password_field(PASSWORD_TEXT)
    LoginPage.click_login()


@allure.suite('Проверка формы авторизации')
@allure.title('Проверка авторизации при заполненной формы и открытие страницы Аккаунта')
def test_login_password_and_open_account(authorization):
    pass