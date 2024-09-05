from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class Scratch(Base):

    def address(self):
        print(self.fake.zipcode())

a = Scratch()
a.address()
