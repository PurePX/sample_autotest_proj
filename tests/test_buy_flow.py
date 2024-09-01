import time

from pages.accessories_page import AcessoriesPage
from pages.mac_accessories_page import MacAcessoriesPage
from pages.main_page import MainPage
from base import base_class

def test_buy_flow():
    base = base_class.Base()
    driver = base.driver
    mp = MainPage(driver)
    ap = AcessoriesPage(driver)
    macap = MacAcessoriesPage(driver)

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











