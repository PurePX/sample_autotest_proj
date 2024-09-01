import time

import selenium.webdriver.chrome.webdriver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Base():
    def __init__(self, driver=None):
        if driver:
            self.driver = driver
        else:
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
            self.driver.maximize_window()
            self.driver.implicitly_wait(10)
            self.driver.get('https://www.apple.com/')
            self.actions = ActionChains(self.driver)

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
        self.click_navigation_bar_accessories()

    def open_main_page(self):
        self.driver.get('https://www.apple.com')


    # Tools

    @staticmethod
    def assert_url(driver, url):
        assert driver.current_url == url, f'Asserted url is {driver.current_url}'
        print('Url assertion success')

    @staticmethod
    def assert_text(element, text):
        assert text == element.text
        print('Text assertion success')






