from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class CheckoutPickupInfoPage(Base):
    # Locators
    someone_else_btn = ("//div[@class='rc-segmented-control-item'][.//button[@aria-checked='false']][//*[contains("
                        "text(), 'Someone else will pick it up')]]")  # Complex locator to ensure button is unchecked
    # by default
    fname_fld = "//*[@id='checkout.pickupContact.thirdPartyPickupContact.thirdPartyContact.address.firstName']"
    lname_fld = "//*[@id='checkout.pickupContact.thirdPartyPickupContact.thirdPartyContact.address.lastName']"
    someones_email_fld = ("//*[@id='checkout.pickupContact.thirdPartyPickupContact.thirdPartyContact.address"
                          ".emailAddress']")
    someones_phone_fld = ("//*[@id='checkout.pickupContact.thirdPartyPickupContact.thirdPartyContact.address"
                          ".fullDaytimePhone']")
    main_customer_email_fld = ("//*[@id='checkout.pickupContact.thirdPartyPickupContact.billingContact.address"
                               ".emailAddress']")
    main_customer_phone_fld = ("//*[@id='checkout.pickupContact.thirdPartyPickupContact.billingContact.address"
                               ".fullDaytimePhone']")
    continue_to_payment_btn = "//*[@id='rs-checkout-continue-button-bottom']"

    # Getters
    def get_someone_else_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.someone_else_btn)))

    def get_fname_fld(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.fname_fld)))

    def get_lname_fld(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.lname_fld)))

    def get_someones_email_fld(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.someones_email_fld)))

    def get_someones_phone_fld(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.someones_phone_fld)))

    def get_main_customer_email_fld(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.main_customer_email_fld)))

    def get_main_customer_phone_fld(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.main_customer_phone_fld)))

    def get_continue_to_payment_btn(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.continue_to_payment_btn)))

    # Actions
    def click_someone_else_btn(self):
        self.get_someone_else_btn().click()

    def fill_fname_fld(self):
        self.get_fname_fld().send_keys(self.some_user_fname)

    def fill_lname_fld(self):
        self.get_lname_fld().send_keys(self.some_user_lname)

    def fill_someones_email_fld(self):
        self.get_someones_email_fld().send_keys(self.some_user_email)

    def fill_someones_phone_fld(self):  # number is not pasting. We have to enter it num by num
        for num in self.some_user_phone:
            self.get_someones_phone_fld().send_keys(num)

    def fill_main_customer_email_fld(self):
        self.get_main_customer_email_fld().send_keys(self.main_user_email)

    def fill_main_customer_phone_fld(self):  # number is not pasting. We have to enter it num by num
        for num in self.main_user_phone:
            self.get_main_customer_phone_fld().send_keys(num)

    def click_continue_to_payment_btn(self):
        self.get_continue_to_payment_btn().click()

    # Methods
    def go_to_payment(self):
        before_url = self.driver.current_url
        self.click_someone_else_btn()
        self.fill_fname_fld()
        self.fill_lname_fld()
        self.fill_someones_email_fld()
        self.fill_someones_phone_fld()
        self.fill_main_customer_email_fld()
        self.fill_main_customer_phone_fld()
        self.click_continue_to_payment_btn()
        self.wait_for_url_change(before_url)
