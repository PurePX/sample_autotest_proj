import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class CheckoutFulfillmentPage(Base):
    city = 'new york'
    # Locators
    pick_up_btn = "//button[@aria-checked='false'][//*[text() = 'I’ll pick it up']]"
    address_fld = "//*[@id='checkout.fulfillment.pickupTab.pickup.storeLocator.searchInput']"
    city_locator_dropdown_option_0 = (
        "//*[@id='checkout.fulfillment.pickupTab.pickup.storeLocator.searchInput_listbox_option_0']")
    select_your_pickup_store_title = ("//h2[@class='rs-fulfillment-grouplabel typography-label'][contains(text(), "
                                      "'Select your pickup store')]")
    show_more_stores_btn = "//button[@data-autom='show-more-stores-button']"
    show_more_stores_btn_alternative = "//button[@class='as-buttonlink rt-storelocator-store-showmore']"
    apple_fifth_ave_btn = "//li[.//*[contains(text(), 'Apple Fifth Avenue')]]"
    apple_fifth_ave_btn_store_name = apple_fifth_ave_btn + "//*[@class='form-selector-title']"
    apple_fifth_ave_details_store_name = "//h3[contains(@class, 'typography-body')]"
    continue_to_pickup_btn = "//*[@id='rs-checkout-continue-button-bottom']"

    # Getters
    def get_pick_up_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.pick_up_btn)))

    def get_address_fld(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.address_fld)))

    def get_city_locator_dropdown_option_0(self):
        try:
            element = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, self.city_locator_dropdown_option_0)))
            return element
        except:
            print('Element not found, retrying...')

    def get_show_more_stores_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.show_more_stores_btn)))

    def get_show_more_stores_btn_alternative(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.show_more_stores_btn_alternative)))

    def get_apple_fifth_ave_btn(self):
        return WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, self.apple_fifth_ave_btn)))

    def get_apple_fifth_ave_btn_store_name(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.apple_fifth_ave_btn_store_name)))

    def get_apple_fifth_ave_details_store_name(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.apple_fifth_ave_details_store_name)))

    def get_continue_to_pickup_btn(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.continue_to_pickup_btn)))

    # Actions
    def click_pick_up_btn(self):
        self.get_pick_up_btn().click()

    def fill_address_fld(self):
        address_field = self.get_address_fld()
        address_field.click()

        for c in self.city:
            address_field.send_keys(c)
            time.sleep(0.2)
        address_field.send_keys(Keys.SPACE)
        time.sleep(2)

    def click_city_locator_dropdown_option_0(self):
        self.get_city_locator_dropdown_option_0().click()
        print('City locator option clicked')

    def click_show_more_stores_btn(self):
        self.get_show_more_stores_btn().click()

    def click_show_more_stores_btn_alternative(self):
        self.get_show_more_stores_btn_alternative().click()

    def click_apple_fifth_ave_btn(self):
        self.get_apple_fifth_ave_btn().click()

    def click_continue_to_pickup_btn(self):
        self.get_continue_to_pickup_btn().click()

    def assert_store_name_with_details(self):
        assert self.get_apple_fifth_ave_btn_store_name().text == self.get_apple_fifth_ave_details_store_name().text

    # Methods
    def go_to_details(self):
        before_url = self.driver.current_url
        self.click_pick_up_btn()
        dropdown_found_flag = False
        retries = 0
        while dropdown_found_flag == False and retries != 5:  # Sometimes dropdown is not showing no matter what.
            # Trying multiple times. UPD Still failing. CONSIDERING AS A BUG
            self.fill_address_fld()
            if self.get_city_locator_dropdown_option_0() and self.get_city_locator_dropdown_option_0().text == (
            'New York, NY'):
                dropdown_found_flag = True
                break
            else:
                for _ in self.city:
                    time.sleep(0.2)
                    self.get_address_fld().send_keys(Keys.BACKSPACE)
                    if (
                            self.get_city_locator_dropdown_option_0() and self.get_city_locator_dropdown_option_0(

                    ).text == 'New York, NY'):
                        dropdown_found_flag = True
                        break
                    retries += 1
                self.get_address_fld().send_keys(Keys.BACKSPACE)
        self.click_city_locator_dropdown_option_0()

        # def clear_address_fld(self):
        #     for _ in self.city:
        #         time.sleep(0.2)
        #         self.get_address_fld().send_keys(Keys.BACKSPACE)
        # self.get_address_fld().send_keys(Keys.BACKSPACE)

        """All operations below aimed to remove magic from the element"""
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        try:
            self.click_show_more_stores_btn()
        except:
            self.click_show_more_stores_btn_alternative() # alternative way if 1st one *magically* won't work

        self.click_apple_fifth_ave_btn()
        self.assert_store_name_with_details()
        self.click_continue_to_pickup_btn()
        self.wait_for_url_change(before_url)
