import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.firefox.service import Service
from pom.homepage import Homepage
from base.seleniumbase import SeleniumBase


@pytest.mark.usefixtures('setup')
class TestMakeOrder:
    def test_check_order(self):
        elt = Homepage(self.driver)
        nav_bar_phones = elt.find_elt('xpath', "//a[@href='/phones/']")
        elt.hover_cursor(nav_bar_phones)
        nav_bar_phones_xiaomi = elt.find_elt("xpath", "//a[@href='/phones/Xiaomi/']")
        nav_bar_phones_xiaomi.click()
        time.sleep(2)
        elt.scroll(0, 700)
        item_for_order = elt.find_elt("xpath", "(//div[@class='products__unit__title']//a)[2]")
        item_for_order.click()
        change_color_phone = elt.find_elt("xpath", "(//input[@type='radio']/following-sibling::span)[3]")
        change_color_phone.click()
        time.sleep(1)
        tab_for_subscribes = elt.find_elt("xpath", "//span[text()='Для абонентов']")
        tab_for_subscribes.click()
        drop_list_price = elt.find_elt("xpath", "//div[@data-default='12']")
        drop_list_price.click()
        time.sleep(1)
        single_payment = elt.find_elt("xpath", "//div[text()[normalize-space()='Единый платеж']]")
        single_payment.click()
        time.sleep(0.5)
        buy_one_click_btn = elt.find_elt('xpath', "//div[@id='buy_tabs']/div[1]/div[2]/div[1]/div[1]/div[4]/div[2]/a[1]")
        buy_one_click_btn.click()
        field_input_name = elt.find_elt("xpath", "//input[@data-field-name='Ваше имя']")
        field_input_name.send_keys("Иванов Иван Иванович")
        field_input_number = elt.find_elt("xpath", "(//input[@class='js-number-inputmask2'])[2]")
        field_input_number.send_keys("291112233")
        time.sleep(3)


    #     order_button = wait.until(ec.visibility_of_element_located((By.XPATH, "(//button[contains(@class,'btn btn--red')]//span)[2]")))
    #     """Кнопка [Заказать]. Не применяется для отладки """
    #     actions.move_to_element(order_button).click().perform()
    #     driver.quit()

