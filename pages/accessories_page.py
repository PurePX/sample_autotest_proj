from xml.dom.minidom import Element

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait


from base.base_class import Base

class AcessoriesPage(Base):


    # Locators
    accessories_title = "//a[@class='localnav-title']"
    browse_all_btn = "//div[@class='as-localnav-actions']"
    shop_by_product_mac_btn = "//a[@data-display-name='product=Mac']"


    # Getters
    def get_accessories_title(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.accessories_title)))

    def get_browse_all_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.browse_all_btn)))

    def get_shop_by_product_mac_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.shop_by_product_mac_btn)))




    # Actions
    def click_browse_all_btn(self):
        self.get_browse_all_btn().click()

    def click_shop_by_product_mac_btn(self):
        self.get_shop_by_product_mac_btn().click()


    # Methods
    def go_to_shop_by_product_mac(self):
        self.click_browse_all_btn()
        self.click_shop_by_product_mac_btn()


