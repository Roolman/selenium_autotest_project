from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = ""

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD1_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2_REGISTRATION = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, "button[value='Register']")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form button")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_IS_ADDED_TO_BASKET = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) strong")
    BASKET_SUMM = (By.CSS_SELECTOR, "#messages .alert-info strong")

class BasketPageLocators():
    BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")
    BASKET_FORMSET = (By.CSS_SELECTOR, "#basket_formset")