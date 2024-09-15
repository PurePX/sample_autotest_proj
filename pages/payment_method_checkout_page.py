from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class PaymentMethodCheckoutPage(Base):
    gained_zip_city_info = ''
    # Locators
    header = "//*[@id='rs-checkout-header']"
    credit_card_btn = "//*[@id='checkout.billing.billingoptions.credit_label']"
    credit_card_number_fld = ("//*[@id='checkout.billing.billingOptions.selectedBillingOptions.creditCard.cardInputs"
                              ".cardInput-0.cardNumber']")
    credit_card_expiration_fld = ("//*[@id='checkout.billing.billingOptions.selectedBillingOptions.creditCard"
                                  ".cardInputs.cardInput-0.expiration']")
    credit_card_cvv_fld = ("//*[@id='checkout.billing.billingOptions.selectedBillingOptions.creditCard.cardInputs"
                           ".cardInput-0.securityCode']")
    billing_address_fname_fld = ("//*[@id='checkout.billing.billingOptions.selectedBillingOptions.creditCard"
                                 ".billingAddress.address.firstName']")
    billing_address_lname_fld = ("//*[@id='checkout.billing.billingOptions.selectedBillingOptions.creditCard"
                                 ".billingAddress.address.lastName']")
    billing_address_street1_address = ("//*[@id='checkout.billing.billingOptions.selectedBillingOptions.creditCard"
                                       ".billingAddress.address.street']")
    billing_address_street2_address = ("//*[@id='checkout.billing.billingOptions.selectedBillingOptions.creditCard"
                                       ".billingAddress.address.street2']")
    billing_address_zip = ("//*[@id='checkout.billing.billingOptions.selectedBillingOptions.creditCard.billingAddress"
                           ".address.zipLookup.postalCode']")
    continue_to_review_btn = "//*[@id='rs-checkout-continue-button-bottom']"
    zip_city = "//select[@name='zipLookupCityState']//option"
    error_msg = "//div[@class='rt-messages-text']"

    # Getters
    def get_header(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.header)))

    def get_credit_card_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.credit_card_btn)))

    def get_credit_card_number_fld(self):
        return WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.credit_card_number_fld)))

    def get_credit_card_expiration_fld(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.credit_card_expiration_fld)))

    def get_credit_card_cvv_field(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.credit_card_cvv_fld)))

    def get_billing_address_fname_fld(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.billing_address_fname_fld)))

    def get_billing_address_lname_fld(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.billing_address_lname_fld)))

    def get_billing_address_street1_address(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.billing_address_street1_address)))

    def get_billing_address_street2_address(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.billing_address_street2_address)))

    def get_billing_address_zip(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.billing_address_zip)))

    def get_continue_to_review_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.continue_to_review_btn)))

    def get_zip_city(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.zip_city)))

    def get_error_msg(self):  # after card payment is failed, this error msg appears. (Could be more cases)
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.error_msg)))

    # Actions
    def click_credit_card_btn(self):
        self.get_credit_card_btn().click()

    def fill_credit_card_number(self, credit_card_number):
        self.get_credit_card_number_fld().send_keys(credit_card_number)

    def fill_credit_card_expiration(self, credit_card_expiration):
        self.get_credit_card_expiration_fld().send_keys(credit_card_expiration)

    def fill_credit_card_cvv(self, credit_card_cvv):
        self.get_credit_card_cvv_field().send_keys(credit_card_cvv)

    def fill_billing_address_fname(self, billing_address_fname):
        self.get_billing_address_fname_fld().send_keys(billing_address_fname)

    def fill_billing_address_lname(self, billing_address_lname):
        self.get_billing_address_lname_fld().send_keys(billing_address_lname)

    def fill_billing_address_street1(self, billing_address_street1_address):
        self.get_billing_address_street1_address().send_keys(billing_address_street1_address)

    def fill_billing_address_street2(self, billing_address_street2_address):
        self.get_billing_address_street2_address().send_keys(billing_address_street2_address)

    def fill_billing_address_zip(self, billing_address_zip):
        self.get_billing_address_zip().send_keys(billing_address_zip)

    def get_text_zip_city(self):
        self.gained_zip_city_info = self.get_zip_city().text

    def click_continue_to_review_btn(self):
        self.get_continue_to_review_btn().click()

    # Methods

    def continue_to_payment(self):
        before_url = self.driver.current_url
        self.click_credit_card_btn()
        self.fill_credit_card_number(self.main_user_credit_card_number)
        self.fill_credit_card_expiration(self.main_user_credit_card_expiration)
        self.fill_credit_card_cvv(self.main_user_credit_card_cvv)
        self.fill_billing_address_fname(self.main_user_fname)
        self.fill_billing_address_lname(self.main_user_lname)
        self.fill_billing_address_street1(self.main_user_billing_address_street1_address)
        self.fill_billing_address_street2(self.main_user_billing_address_street2_address)
        self.fill_billing_address_zip(self.main_user_billing_address_zip)
        self.get_text_zip_city()
        self.click_continue_to_review_btn()
        self.wait_for_url_change(before_url)

    def check_error_msg_card_payment_failed(self):
        self.assert_text(element_text=self.get_error_msg().text, text=f'Your payment authorization failed on card •••{self.main_user_credit_card_number[-4:]}. Please verify your information and try again, or try another payment method.')
        # # currently failing this step as the error text is different. Looks like Apple overwhelmed for now. Let's
        # consider this as a bug
