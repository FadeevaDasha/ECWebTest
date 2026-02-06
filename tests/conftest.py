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
    login_page = LoginPageHelper(browser)
    login_page.input_email_field(EMAIL_TEXT)
    login_page.input_password_field(PASSWORD_TEXT)
    login_page.click_login()
    account_page = AccountPageHelper(browser)
    account_page.click_ecommerce()
