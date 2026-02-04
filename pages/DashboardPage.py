from pages.BasePage import BasePageHelper
from selenium.webdriver.common.by import By

import allure

class DashboardPageLocators:
    DASHBOARD_TITLE = (By.XPATH, '//*[@title="Dashboard"]')
    DASHBOARD_CHART = (By.XPATH, '(//*[@class="container ng-star-inserted"])[1]')
    DASHBOARD_STATISTICS = (By.XPATH, '(//*[@class="container ng-star-inserted"])[2]')
    DASHBOARD_PRODUCT = (By.XPATH, '//*[@class="top-product-container ng-star-inserted"]')
    DASHBOARD_CUSTOMER = (By.XPATH, '//*[@class="top-customer-container ng-star-inserted"]')
    DASHBOARD_FAILED_TRANSACTIONS = (By.XPATH, '//*[@class="failed-payments-container ng-star-inserted"]')


class DashboardPageHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def check_page(self):
        with allure.step('Проверка загруженной страницы'):
            self.attach_screenshot()
        self.find_element(DashboardPageLocators.DASHBOARD_CHART)
        self.find_element(DashboardPageLocators.DASHBOARD_PRODUCT)
        self.find_element(DashboardPageLocators.DASHBOARD_TITLE)
        self.find_element(DashboardPageLocators.DASHBOARD_CUSTOMER)
        self.find_element(DashboardPageLocators.DASHBOARD_STATISTICS)
        self.find_element(DashboardPageLocators.DASHBOARD_FAILED_TRANSACTIONS)

    @allure.step('Проверка отображения заголовка')
    def display_title(self):
        self.attach_screenshot()
        self.find_element(DashboardPageLocators.DASHBOARD_TITLE).is_displayed()

    @allure.step('Проверка отображения графика')
    def display_chart(self):
        self.attach_screenshot()
        self.find_element(DashboardPageLocators.DASHBOARD_CHART).is_displayed()

    @allure.step('Проверка отображения статистики')
    def display_statistics(self):
        self.attach_screenshot()
        self.find_element(DashboardPageLocators.DASHBOARD_STATISTICS).is_displayed()

    @allure.step('Проверка отображения топа продуктов')
    def display_products(self):
        self.attach_screenshot()
        self.find_element(DashboardPageLocators.DASHBOARD_PRODUCT).is_displayed()

    @allure.step('Проверка отображения топа кастомеров')
    def display_customers(self):
        self.attach_screenshot()
        self.find_element(DashboardPageLocators.DASHBOARD_CUSTOMER).is_displayed()

    @allure.step('Проверка отображения упавших транзакций')
    def display_failed_transactions(self):
        self.attach_screenshot()
        self.find_element(DashboardPageLocators.DASHBOARD_FAILED_TRANSACTIONS).is_displayed()
