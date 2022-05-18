import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.firefox.service import Service


@pytest.mark.usefixtures('setup')
class TestMakeOrder:
    def test_make_order_one_click(self, get_webdriver, get_actions):
        driver = get_webdriver
        actions = get_actions
        driver.implicitly_wait(10)
        wait = WebDriverWait(driver, 15, 1)
        nav_bar_phones = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@href='/phones/']")))
        actions.move_to_element(nav_bar_phones).perform()
        nav_bar_phones_xiaomi = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@href='/phones/Xiaomi/']")))
        actions.move_to_element(nav_bar_phones_xiaomi).perform()
        actions.move_to_element(nav_bar_phones_xiaomi).click().perform()
        time.sleep(1.5)
        driver.execute_script("window.scrollTo(0, 700)")
        item_for_order = wait.until(ec.visibility_of_element_located((By.XPATH, "(//div[@class='products__unit__title']//a)[2]")))
        actions.move_to_element(item_for_order).perform()
        actions.move_to_element(item_for_order).click().perform()
        time.sleep(1)
        color_phone = wait.until(ec.element_to_be_clickable((By.XPATH, "(//input[@type='radio']/following-sibling::span)[3]")))
        actions.move_to_element(color_phone).click().perform()
        time.sleep(2)
        tab_for_subscribes = wait.until(ec.element_to_be_clickable((By.XPATH, "//span[text()='Для абонентов']")))
        actions.move_to_element(tab_for_subscribes).click().perform()
        drop_list_price = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@data-default='12']")))
        actions.move_to_element(drop_list_price).click().perform()
        single_payment = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[text()[normalize-space()='Единый платеж']]")))
        actions.move_to_element(single_payment).click().perform()
        time.sleep(0.5)
        buy_one_click_button = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='buy_tabs']/div[1]/div[2]/div[1]/div[1]/div[4]/div[2]/a[1]")))
        actions.move_to_element(buy_one_click_button).click().perform()
        time.sleep(1)
        field_input_name = wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@data-field-name='Ваше имя']")))
        field_input_name.send_keys("Иванов Иван Иванович")
        field_input_phone = wait.until(ec.visibility_of_element_located((By.XPATH, "(//input[@class='js-number-inputmask2'])[2]")))
        field_input_phone.send_keys("291112233")

        # order_button = wait.until(ec.visibility_of_element_located((By.XPATH, "(//button[contains(@class,'btn btn--red')]//span)[2]")))
        # """Кнопка [Заказать]. Не применяется для отладки """
        # actions.move_to_element(order_button).click().perform()
        # driver.quit()

