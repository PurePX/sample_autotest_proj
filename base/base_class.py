import time
import traceback
from datetime import datetime

import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Base:
    def __init__(self, driver=None):
        if driver:
            self.driver = driver
        else:
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)
            self.driver.get('https://www.apple.com/')
            self.actions = ActionChains(self.driver)

    # Random items
    test_start_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    test_postfix = '_test_' + test_start_time

    # Locators
    navigation_bar_accessories = "//div[contains(@class, 'globalnav-item-accessories')]"

    # Getters
    def get_navigation_bar_accessories(self):
        return self.driver.find_element(By.XPATH, self.navigation_bar_accessories)

    # Actions
    def click_navigation_bar_accessories(self):
        self.get_navigation_bar_accessories().click()
        print('Accessories clicked')

    # Methods
    def go_to_accessories(self):
        before_url = self.driver.current_url
        self.click_navigation_bar_accessories()
        self.wait_for_url_change(before_url)

    def open_main_page(self):
        self.driver.get('https://www.apple.com')

    # Tools
    @staticmethod
    def assert_text_contains(element_text: str, text: str):
        assert text in element_text, f'Not found "{text}" in element text "{element_text}"'
        print(f'Element text {element_text} contains {text}')

    @staticmethod
    def assert_text(element_text: str, text: str):
        assert text == element_text, f'Compared {text} and element text "{element_text}". No matching text found'
        print('Text assertion success')

    @staticmethod
    def assert_url(driver, url):
        assert driver.current_url == url, f'Error! Asserted url is {driver.current_url}'
        print('Url assertion success')

    @staticmethod
    def assert_url_contains(driver, text):
        time.sleep(2)
        assert text in driver.current_url, f'Error! Asserted url is {driver.current_url}'
        print(f'Link contains {text}')

    @staticmethod
    def assert_price(price, expected_price):
        assert price == expected_price, f'Error! Expected price {expected_price}, got {price}'
        print('Price assertion success')

    def wait_for_url_change(self, before_url):  # This website have a lot of logic going on before page is changed
        timeout = 0
        changed = False

        while not changed and timeout != 20:
            print(f'Current url: {self.driver.current_url}. Waiting for a change')
            if self.driver.current_url != before_url:
                changed = True
                break
            else:
                time.sleep(1)
                timeout += 1

    def take_screenshot(self):
        self.driver.save_screenshot(f'screenshots/screenshot{self.test_postfix}.png')

    def test_failure_protocol(self, exception):

        timestamp = time.strftime("%Y%m%d-%H%M%S")
        screenshot_name = f"fail_{timestamp}.png"
        stack_trace = traceback.format_exc()

        self.driver.save_screenshot(f'screenshots/{screenshot_name}')

        with open(f'logs/fail_log{self.test_postfix}.log', 'w') as fail_log:
            fail_log.write(f'Test{self.test_postfix} failed\n')
            fail_log.write(f'Failed on url: {self.driver.current_url}\n')
            fail_log.write(f'Exception: {exception}\n')
            fail_log.write(f'Stack Trace: {stack_trace}\n')
        pytest.fail()
