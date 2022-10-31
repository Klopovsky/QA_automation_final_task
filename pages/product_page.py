from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_add_to_basket_button(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button_add_to_basket.click()
        self.solve_quiz_and_get_code()
        assert self.browser.find_element(*ProductPageLocators.CHECK_MESSAGE_ADD_TO_BASKET).text == self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        
        