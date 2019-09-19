from .pages.product_page import ProductPage
import pytest

@pytest.mark.parametrize('num', ["0", "1", "2", "3", "4", "5", "6",
                                    pytest.param("7", marks=pytest.mark.xfail), "8", "9"])
def  test_guest_can_add_product_to_basket(browser, num):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
 #   page.browser.implicitly_wait(5)
    page.product_name_matches_product_added_message()
    page.product_price_match_basket_summ()