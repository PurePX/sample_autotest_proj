from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class FinalConfirmationCheckoutPage(Base):
    # Locators
    header = "//span[@class='rs-review-header-text']"
    fulfillment_details = "//*[@id='checkout.review.fulfillmentReview.reviewGroup-1-shipquote']"
    item_name = "//h2[@class='rs-iteminfo-title']"
    item_qty = "//div[@class='rs-quantity-text']//span[2]"
    item_price = "//div[@class='rs-iteminfo-price']"
    pickup_details_container = "//div[@class='row rs-review-details']"
    pickup_contact_fname = pickup_details_container + "//*[@data-autom='form-field-firstName']"
    pickup_contact_lname = pickup_details_container + "//*[@data-autom='form-field-lastName']"
    pickup_contact_email = pickup_details_container + "//span[@data-autom='form-field-emailAddress']"
    pickup_contact_phone = pickup_details_container + "//span[@data-autom='form-field-daytimePhone']"
    payment_card_number = "//span[@class='rs-review-cardnumber']"
    payment_details_container = "//div[@class='row rs-review-details rs-review-billing']"
    billing_fname = payment_details_container + "//*[@data-autom='form-field-firstName']"
    billing_lname = payment_details_container + "//*[@data-autom='form-field-lastName']"
    billing_address_1 = "//span[@data-autom='form-field-street']"
    billing_address_2 = "//span[@data-autom='form-field-street2']"
    billing_city = "//span[@data-autom='form-field-city']"
    billing_state = "//span[@data-autom='form-field-state']"
    billing_zip = "//span[@data-autom='form-field-postalCode']"
    subtotal = "//div[@data-autom='bagrs-summary-subtotalvalue']"
    tax = "//div[@data-autom='bagrs-summary-taxvalue']"
    total = "//div[@data-autom='bagtotalvalue']"
    place_order_btn = "//*[@id='rs-checkout-continue-button-bottom']"

    # Getters
    def get_header(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.header)))

    def get_fulfillment_details(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.fulfillment_details)))

    def get_item_name(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.item_name)))

    def get_item_qty(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.item_qty)))

    def get_item_price(self) -> float:
        return float(
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.item_price))).text[1:])

    def get_pickup_details_container(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.pickup_details_container)))

    def get_pickup_contact_fname(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.pickup_contact_fname)))

    def get_pickup_contact_lname(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.pickup_contact_lname)))

    def get_pickup_contact_email(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.pickup_contact_email)))

    def get_pickup_contact_phone(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.pickup_contact_phone)))

    def get_payment_card_number(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.payment_card_number)))

    def get_payment_details_container(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.payment_details_container)))

    def get_billing_fname(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.billing_fname)))

    def get_billing_lname(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.billing_lname)))

    def get_billing_address_1(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.billing_address_1)))

    def get_billing_address_2(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.billing_address_2)))

    def get_billing_city(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.billing_city)))

    def get_billing_state(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.billing_state)))

    def get_billing_zip(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.billing_zip)))

    def get_subtotal(self) -> float:
        return float(
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.subtotal))).text[1:])

    def get_tax(self) -> float:
        return float(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.tax))).text[1:])

    def get_total(self) -> float:
        return float(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.total))).text[1:])

    def get_place_order_btn(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.place_order_btn)))

    # Actions
    def click_place_order_btn(self):
        self.get_place_order_btn().click()

    # Methods

    def continue_to_payment(self):
        before_url = self.driver.current_url
        self.click_place_order_btn()
        self.wait_for_url_change(before_url)

    def verify_info(self, catalog_name, catalog_price, gained_zip_city_info):
        self.assert_text_contains(self.get_fulfillment_details().text, 'Pickup')
        self.assert_text_contains(self.get_fulfillment_details().text, 'Fifth Avenue')
        self.assert_text(self.get_item_name().text, catalog_name)
        self.assert_text(self.get_item_qty().text, '1')
        self.assert_price(self.get_item_price(), catalog_price)
        self.assert_text(self.get_pickup_contact_fname().text, self.some_user_fname)
        self.assert_text(self.get_pickup_contact_lname().text, self.some_user_lname)
        self.assert_text(self.get_pickup_contact_email().text, self.some_user_hidden_email)
        self.assert_text_contains(self.get_pickup_contact_phone().text, self.some_user_phone[-2:])
        self.assert_text_contains(self.get_payment_card_number().text, self.main_user_credit_card_number[-4:])
        self.assert_text(self.get_billing_fname().text, self.main_user_fname)
        self.assert_text(self.get_billing_lname().text, self.main_user_lname)
        self.assert_text(self.get_billing_address_1().text, self.main_user_billing_address_street1_address)
        self.assert_text(self.get_billing_address_2().text, self.main_user_billing_address_street2_address)
        self.assert_text(f'{self.get_billing_city().text} {self.get_billing_state().text}', gained_zip_city_info)
        self.assert_text(self.get_billing_zip().text, self.main_user_billing_address_zip)
        self.assert_price(self.get_subtotal(), catalog_price)
        assert self.get_tax() < catalog_price and self.get_tax() < self.get_subtotal()
        assert self.get_total() == self.get_subtotal() + self.get_tax()
