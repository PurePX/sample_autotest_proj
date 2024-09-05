import time
from os import times
from xml.dom.minidom import Element

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait


from base.base_class import Base

class CartPage(Base): #Probably can be universal cart page
#https://www.apple.com/shop/product/MX572ZM/A/apple-mac-pro-wheels-kit

    # Locators
    item_name = "//a[@data-autom='bag-item-name']"
    item_price = "//div[@class='rs-iteminfo-price']"
    checkout_btn = "//*[@id='shoppingCart.actions.navCheckout']"




    # Getters
    def get_item_name(self) -> str:
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.item_name))).text

    def get_item_price(self) -> float:
        return float(self.driver.find_element(By.XPATH, self.item_price).text[1:])

    def get_checkout_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.checkout_btn)))


    # Actions
    def click_checkout_btn(self):
        self.get_checkout_btn().click()



    # Methods

    def go_to_checkout(self):
        self.click_checkout_btn()

    def assert_price_with_catalog(self, catalog_price):
        assert catalog_price == self.get_item_price()
        print('Price assertion successful')

    def assert_name_with_catalog(self, catalog_name):
        assert catalog_name == self.get_item_name()
        print('Name assertion successful')