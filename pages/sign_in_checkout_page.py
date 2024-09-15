from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class SignInCheckoutPage(Base):  # Probably can be universal cart page
    # https://www.apple.com/shop/product/MX572ZM/A/apple-mac-pro-wheels-kit

    # Locators
    continue_as_guest_btn = "//*[@id='signIn.guestLogin.guestLogin']"

    # Getters
    def get_continue_as_guest_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.continue_as_guest_btn)))

    # Actions
    def click_continue_as_guest_btn(self):
        self.get_continue_as_guest_btn().click()

    # Methods

    def continue_as_guest(self):
        before_url = self.driver.current_url
        self.click_continue_as_guest_btn()
        self.wait_for_url_change(before_url)
