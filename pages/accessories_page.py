from xml.dom.minidom import Element

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait


from base.base_class import Base

class MainPage(Base):
    pass

    # Locators
    accessories_title = "//a[@class='localnav-title']"

    # Getters
    def get_accessories_title(self):

        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.accessories_title)))
    # Actions


    # Methods



