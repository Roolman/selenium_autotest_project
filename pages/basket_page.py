from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_elements_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORMSET), "Formset is present, but should not"
        
    def should_be_message_no_elements(self):
        message = self.browser.find_element(*BasketPageLocators.BASKET_MESSAGE)
        assert "empty" in message.text, "No 'empty' in basket message"
