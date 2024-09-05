import time

from pages.accessories_page import AcessoriesPage
from pages.cart_page import CartPage
from pages.checkout_fullfilment_page import CheckoutFulfillmentPage
from pages.mac_accessories_page import MacAcessoriesPage
from pages.mac_display_mounts_page import MacDisplayMountsPage
from pages.mac_wheels_page import ItemPage
from pages.main_page import MainPage
from base import base_class
from pages.sign_in_checkout_page import SignInCheckoutPage


def test_buy_flow():
    base = base_class.Base()
    driver = base.driver
    mp = MainPage(driver)
    ap = AcessoriesPage(driver)
    macap = MacAcessoriesPage(driver)
    mdmp = MacDisplayMountsPage(driver)
    ip = ItemPage(driver)
    cartp = CartPage(driver)
    sicp = SignInCheckoutPage(driver)
    cfp = CheckoutFulfillmentPage(driver)

    mp.open_main_page()
    time.sleep(5)
    mp.click_navigation_bar_accessories()
    base.assert_url(driver, 'https://www.apple.com/shop/accessories/all')
    print('Accessories catalog is opened')

    ap.go_to_shop_by_product_mac()
    base.assert_url(driver, 'https://www.apple.com/shop/mac/accessories')
    print('Mac accessories catalog is opened')

    macap.go_to_display_mounts()
    base.assert_url(driver, 'https://www.apple.com/shop/mac/accessories/displays-mounts')
    print('Mac Displays and mounts catalog is opened')

    catalog_price = mdmp.get_mac_wheels_price()
    catalog_name = mdmp.get_mac_wheels_name()

    mdmp.go_to_mac_wheels_page()
    time.sleep(2)
    base.assert_url_contains(driver, 'apple-mac-pro-wheels-kit')

    time.sleep(2)
    ip.assert_price_with_catalog(catalog_price)
    ip.assert_name_with_catalog(catalog_name)

    ip.add_item_to_cart()
    time.sleep(2)

    base.assert_url(driver, 'https://www.apple.com/shop/bag')
    cartp.assert_price_with_catalog(catalog_price)
    cartp.assert_name_with_catalog(catalog_name)

    cartp.go_to_checkout()
    time.sleep(2)
    base.assert_url_contains(driver, '/shop/signIn')

    sicp.continue_as_guest()
    time.sleep(5)
    base.assert_url_contains(driver, 'shop/checkout?_s=Fulfillment-init')

    cfp.go_to_payment()

test_buy_flow()




