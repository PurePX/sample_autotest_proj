from xml.dom.minidom import Element

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait


from base.base_class import Base

class MacAcessoriesPage(Base):


    # Locators
    display_mounts_img = "//img[contains(@src, 'mounts')]"


    # Getters
    def get_display_mounts_img(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.display_mounts_img)))


    # Actions
    def click_display_mounts_btn(self):
        self.get_display_mounts_img().click()


    # Methods
    def go_to_display_mounts(self):
        self.click_display_mounts_btn()




