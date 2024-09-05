from faker.proxy import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base_class import Base


class CheckoutFulfillmentPage(Base):

    # Locators
    pick_up_btn = "//button[@aria-checked='false'][//*[text() = 'I’ll pick it up']]"
    address_fld = "//*[@id='checkout.fulfillment.pickupTab.pickup.storeLocator.searchInput']"
    city_locator_dropdown_option_0 = "//*[@id='checkout.fulfillment.pickupTab.pickup.storeLocator.searchInput_listbox_option_0']"
    select_your_pickup_store_title = "//h2[@class='rs-fulfillment-grouplabel typography-label'][contains(text(), 'Select your pickup store')]"

    # Getters
    def get_pick_up_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.pick_up_btn)))

    def get_address_fld(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.address_fld)))

    def get_city_locator_dropdown_option_0(self):
        return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.city_locator_dropdown_option_0)))

    # Actions
    def click_pick_up_btn(self):
        self.get_pick_up_btn().click()

    def fill_address_fld(self):
        self.get_address_fld().send_keys('new york')
        print('Address filled')

    def click_city_locator_dropdown_option_0(self):
        self.get_city_locator_dropdown_option_0().click()
        print('City locator option clicked')

    # Methods
    def go_to_payment(self):
        self.click_pick_up_btn()
        self.fill_address_fld()

