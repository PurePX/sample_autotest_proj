from base import base_class
from pages.accessories_page import AcessoriesPage
from pages.cart_page import CartPage
from pages.checkout_fullfilment_page import CheckoutFulfillmentPage
from pages.checkout_pickup_info_page import CheckoutPickupInfoPage
from pages.final_confirmation_checkout_page import FinalConfirmationCheckoutPage
from pages.mac_accessories_page import MacAccessoriesPage
from pages.mac_display_mounts_page import MacDisplayMountsPage
from pages.mac_wheels_page import ItemPage
from pages.payment_method_checkout_page import PaymentMethodCheckoutPage
from pages.sign_in_checkout_page import SignInCheckoutPage

"""This test validates main purchase flow. From visiting main page to paying for item as a guest with credit card"""


# ====== 12 failed, 88 passed in 10490.94s (2:54:50) ======
def test_buy_flow():
    base = base_class.Base()
    driver = base.driver
    try:
        ap = AcessoriesPage(driver)
        macap = MacAccessoriesPage(driver)
        mdmp = MacDisplayMountsPage(driver)
        ip = ItemPage(driver)
        cartp = CartPage(driver)
        sicp = SignInCheckoutPage(driver)
        cfp = CheckoutFulfillmentPage(driver)
        cpip = CheckoutPickupInfoPage(driver)
        pmcp = PaymentMethodCheckoutPage(driver)
        fccp = FinalConfirmationCheckoutPage(driver)

        base.open_main_page()

        base.go_to_accessories()
        base.assert_url(driver, 'https://www.apple.com/shop/accessories/all')
        print('Accessories catalog is opened')

        ap.go_to_shop_by_product_mac()
        base.assert_url(driver, 'https://www.apple.com/shop/mac/accessories')
        print('Mac accessories catalog is opened')

        macap.go_to_display_mounts()
        assert mdmp.get_page_title_text() == 'Displays & Mounts'
        base.assert_url(driver, 'https://www.apple.com/shop/mac/accessories/displays-mounts')
        print('Mac Displays and mounts catalog is opened')

        catalog_price = mdmp.get_mac_wheels_price()
        catalog_name = mdmp.get_mac_wheels_name()

        mdmp.go_to_mac_wheels_page()
        base.assert_url_contains(driver, 'apple-mac-pro-wheels-kit')
        base.assert_price(ip.get_item_price(), catalog_price)
        base.assert_text(ip.get_item_name().text, catalog_name)

        """Shortcut for testing purposes"""
        # catalog_price = 699.00
        # catalog_name = 'Apple Mac Pro Wheels Kit
        # driver.get('https://www.apple.com/shop/product/MX572ZM/A/apple-mac-pro-wheels-kit')
        # time.sleep(4)

        ip.add_item_to_cart()
        base.assert_url(driver, 'https://www.apple.com/shop/bag')
        base.assert_price(cartp.get_item_price(), catalog_price)
        base.assert_text(cartp.get_item_name().text, catalog_name)

        cartp.go_to_checkout()
        base.assert_url_contains(driver, '/shop/signIn')

        sicp.continue_as_guest()
        base.assert_url_contains(driver, 'shop/checkout?_s=Fulfillment-init')

        cfp.go_to_details()
        base.assert_url_contains(driver, 'shop/checkout?_s=PickupContact-init')

        cpip.go_to_payment()
        base.assert_url_contains(driver, 'shop/checkout?_s=Billing-init')
        base.assert_text(pmcp.get_header().text, "How do you want to pay?")

        pmcp.continue_to_payment()
        base.assert_url_contains(driver, 'shop/checkout?_s=Review')
        base.assert_text(fccp.get_header().text, "Ready to place your order?")

        fccp.verify_info(catalog_name, catalog_price, pmcp.gained_zip_city_info)
        fccp.continue_to_payment()

        pmcp.check_error_msg_card_payment_failed()
        base.take_screenshot()

        print('Test completed successfully')


    except Exception as e:
        base.test_failure_protocol(e)

# test_buy_flow()