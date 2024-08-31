import time
from pages.main_page import MainPage
from base import base_class

def test_buy_flow():
    base = base_class.Base()
    driver = base.driver
    mp = MainPage()

    mp.open_main_page()
    mp.click_navigation_bar_accessories()
    base.assert_url(driver, 'https://www.apple.com/shop/accessories/all')
    print('Accessories catalog is opened')








