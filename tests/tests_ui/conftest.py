import time
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as firefox_options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.firefox.service import Service


"""Service используется в новыйх версиях Selenium 4+. Ранее путь прописывался в executable_path=geckodriver"""
# geckodriver = Service('/home/vladislav/Projects/shop_mts/geckodriver')
"""Путь где лежит драйвер для Firefox (устаревшее применение)"""
# geckodriver = '/home/vladislav/Projects/shop_mts/geckodriver'

@pytest.fixture
def get_firefox_options():
    options = firefox_options()
    """Отключил опцию --headless для отладки процесса"""
    # options.add_argument('--headless')
    # options.add_argument('firefox')
    return options

@pytest.fixture
def get_webdriver(get_firefox_options):
    options = get_firefox_options
    geckodriver = Service('/home/vladislav/Projects/shop_mts/geckodriver')
    driver = webdriver.Firefox(service=geckodriver, options=options)
    driver.set_window_rect(x=None, y=None, width=1920, height=1080)
    driver.implicitly_wait(5)
    return driver

@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://shop.mts.by/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()

@pytest.fixture
def get_actions(get_webdriver):
    actions = webdriver.ActionChains(get_webdriver)
    return actions

