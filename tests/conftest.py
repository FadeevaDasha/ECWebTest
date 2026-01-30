import pytest

from core.Links import Links
from core.BaseTest import browser
from pages.BasePage import BasePageHelper
from pages.LoginPage import LoginPageHelper
from pages.AccountPage import AccountPageHelper

EMAIL_TEXT = 'evgeniyfadeev310322@gmail.com'
PASSWORD_TEXT = ':tyzAflttd22'

@pytest.fixture(scope='session')
def authorization(browser):
    BasePageHelper(browser).get_url(Links.AUTH)
    LoginPage = LoginPageHelper(browser)
    LoginPage.input_email_field(EMAIL_TEXT)
    LoginPage.input_password_field(PASSWORD_TEXT)
    LoginPage.click_login()
    AccountPage = AccountPageHelper(browser)
    AccountPage.click_ecommerce()
