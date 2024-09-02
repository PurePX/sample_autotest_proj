import time
from xml.dom.minidom import Element

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait


from base.base_class import Base

class MacDisplayMountsPage(Base):


    # Locators
    stands_filter_btn = "//label[@for='facet-17998']"
    mac_compatibility_dropdown = "//button[@id='title-:r2:-1']"
    mac_compatibility_dropdown_mac_pro_option = "//label[@for='facet-13929028']"
    brand_dropdown = "//button[@id='title-:r2:-2']"
    brand_dropdown_apple_option = "//label[@for='facet-12820']"
    mac_wheels_link = "//a[text() = 'Apple Mac Pro Wheels Kit']"

    


    # Getters
    def get_stands_filter_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.stands_filter_btn)))
    
    def get_mac_compatibility_dropdown(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.mac_compatibility_dropdown)))
    
    def get_mac_compatibility_dropdown_mac_pro_option(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.mac_compatibility_dropdown_mac_pro_option)))
    
    def get_brand_dropdown(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.brand_dropdown)))

    def get_brand_dropdown_mac_pro_option(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.brand_dropdown_apple_option)))

    def get_mac_wheels_link(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.mac_wheels_link)))
    


    # Actions
    def click_stands_filter_btn(self):
        self.get_stands_filter_btn().click()
        self.assert_url(self.driver, 'https://www.apple.com/shop/mac/accessories/displays-mounts?f=stand&fh=4593%2B464e&page=1')
    
    def click_mac_compatibility_dropdown(self):
        self.get_mac_compatibility_dropdown().click()
        
    def click_mac_compatibility_dropdown_mac_pro_option(self):
        self.get_mac_compatibility_dropdown_mac_pro_option().click()
        
    def click_brand_dropdown(self):
        self.get_brand_dropdown().click()

    def click_brand_dropdown_apple_option(self):
        self.get_brand_dropdown_mac_pro_option().click()

    def click_mac_wheels_link(self):
        self.get_mac_wheels_link().click()


    # Methods

    def go_to_mac_wheels_page(self):
        self.click_stands_filter_btn()
        self.click_mac_compatibility_dropdown()
        self.click_mac_compatibility_dropdown_mac_pro_option()
        self.click_brand_dropdown()
        self.click_brand_dropdown_apple_option()
        time.sleep(2)
        self.click_mac_wheels_link()
