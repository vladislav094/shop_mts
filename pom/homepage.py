from typing import List
from selenium.webdriver.remote.webelement import WebElement
from base.seleniumbase import SeleniumBase

class Homepage(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def find_elt(self, find_by: str, locator: str) -> WebElement:
        return self.find_if_visible(find_by, locator)

    def find_elts(self, find_by, locator) -> List[WebElement]:
        # return self.finds_is_visible("xpath", self.xpath)
        return self.find_are_visible(find_by, locator)

    def present_elt(self, find_by: str, locator: str) -> WebElement:
        return self.find_if_present(find_by, locator)

    def not_present_elt(self, find_by: str, locator: str) -> WebElement:
        return self.find_if_not_present(find_by, locator)

    def hover(self, element: WebElement) -> WebElement:
        return self.hover_cursor(element)

    def get_nav_links_text(self, links) -> str:
        '''Return all nav links text. Return format is a String with comma separated values'''
        nav_links_text = self.get_text_from_webelements(links)
        return ','.join(nav_links_text)

    def scroll(self, width: int, height: int):
        '''The function scrolls the page to the specified height'''
        return self.window_scroll_To(width, height)