from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in str(self.url), "Incorrect url, no 'login' word"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not on a page"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not on a page"
    
    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_REGISTRATION)
        password1_field = self.browser.find_element(*LoginPageLocators.PASSWORD1_REGISTRATION)
        password2_field = self.browser.find_element(*LoginPageLocators.PASSWORD2_REGISTRATION)
        email_field.send_keys(email)
        password1_field.send_keys(password)
        password2_field.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION)
        button.click()

