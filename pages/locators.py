from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR,".btn-add-to-basket")
    CHECK_MESSAGE_ADD_TO_BASKET = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")
    NAME_PRODUCT = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/h1")