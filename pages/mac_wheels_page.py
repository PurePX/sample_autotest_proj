import time
from os import times
from xml.dom.minidom import Element

from faker.contrib.pytest.plugin import faker
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait


from base.base_class import Base

class ItemPage(Base): #Probably can be universal item page
#https://www.apple.com/shop/product/MX572ZM/A/apple-mac-pro-wheels-kit

    # Locators
    item_name = "//h1[@data-autom='productTitle']"
    item_price = "//span[@data-autom='full-price']"
    add_to_cart_btn = "//*[@id='add-to-cart']"




    # Getters
    def get_item_name(self) -> str:
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.item_name))).text

    def get_item_price(self) -> float:
        return float(self.driver.find_element(By.XPATH, self.item_price).text[1:])

    def get_add_to_cart_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_btn)))


    # Actions
    def click_add_to_cart_btn(self):
        self.get_add_to_cart_btn().click()



    # Methods

    def add_item_to_cart(self):
        self.click_add_to_cart_btn()

    def assert_price_with_catalog(self, catalog_price):
        assert catalog_price == self.get_item_price()
        print('Price assertion successful')

    def assert_name_with_catalog(self, catalog_name):
        assert catalog_name == self.get_item_name()
        print('Name assertion successful')

