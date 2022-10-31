import pytest
from .pages.product_page import ProductPage

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(10)]

 

@pytest.mark.parametrize('link', urls)
@pytest.mark.xfail
def test_guest_can_add_product_to_basket(browser,link):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket_button()