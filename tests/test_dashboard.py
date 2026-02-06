import allure

from core.BaseTest import browser
from pages.DashboardPage import DashboardPageHelper

@allure.feature('Проверка отображения страницы Dashboard')
class TestDashboard:


    @allure.title('Проверка отображения графика')
    def test_checking_graph_display(self, authorization, browser):
        dashboard_page = DashboardPageHelper(browser)
        dashboard_page.display_chart()

    @allure.title('Проверка отображения заголовка')
    def test_checking_title_display(self, authorization, browser):
        dashboard_page = DashboardPageHelper(browser)
        dashboard_page.display_title()

    @allure.title('Проверка отображения статистики')
    def test_checking_statistics_display(self, authorization, browser):
        dashboard_page = DashboardPageHelper(browser)
        dashboard_page.display_statistics()

    @allure.title('Проверка отображения топа продуктов')
    def test_checking_products_display(self, authorization, browser):
        dashboard_page = DashboardPageHelper(browser)
        dashboard_page.display_products()

    @allure.title('Проверка отображения топа кастомеров')
    def test_checking_customers_display(self, authorization, browser):
        dashboard_page = DashboardPageHelper(browser)
        dashboard_page.display_customers()

    @allure.title('Проверка отображения упавших транзакций')
    def test_checking_failed_transactions_display(self, authorization, browser):
        dashboard_page = DashboardPageHelper(browser)
        dashboard_page.display_failed_transactions()