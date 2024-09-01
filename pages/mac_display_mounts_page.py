from xml.dom.minidom import Element

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait


from base.base_class import Base

class MacAcessoriesPage(Base):


    # Locators
    stands_filter_btn = "//*[@id='facet-17998']"


    # Getters
    def get_stands_filter_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.stands_filter_btn)))


    # Actions
    def click_stands_filter_btn(self):
        self.get_stands_filter_btn().click()
        self.assert_url(self.driver, 'https://www.apple.com/shop/mac/accessories/displays-mounts?f=stand&fh=4593%2B464e&page=1')


    # Methods
    def go_to_display_mounts(self):

    def button_accordion(self):
        return self.driver.find_element(By.XPATH, "//*[text() = 'Mac Compatibility']")
