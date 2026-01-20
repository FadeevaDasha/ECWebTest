import pytest
from selenium import webdriver

@pytest.fixture(scope='session')
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--lang=ru')
    driver = webdriver.Chrome(options=options)
    yield driver
    if driver:
        driver.quit()