from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage): 
    def add_product_to_basket(self):
        add_product_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_product_button.click()
    
    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return product_name.text
    
    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price.text

    def product_name_matches_product_added_message(self):
        product_added_message = self.browser.find_element(*ProductPageLocators.PRODUCT_IS_ADDED_TO_BASKET)
        assert self.get_product_name() == product_added_message.text, "Added product message doesn't match name of the product"

    def product_price_match_basket_summ(self):
        basket_summ = self.browser.find_element(*ProductPageLocators.BASKET_SUMM)
        assert self.get_product_price() == basket_summ.text, "Basket summ doesn't match product price"