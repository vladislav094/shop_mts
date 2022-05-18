from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.remote.webelement import WebElement
from typing import List

class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 15, 0.3)

    def __get_selenium_by(self, find_by: str) -> dict:
        find_by = find_by.lower()
        locating = {'css': By.CSS_SELECTOR,
                   'xpath': By.XPATH,
                   'class_name': By.CLASS_NAME,
                   'id': By.ID,
                   'link_text': By.LINK_TEXT,
                   'name': By.NAME,
                   'partial_link_text': By.PARTIAL_LINK_TEXT,
                   'tag_name': By.TAG_NAME}
        return locating[find_by]