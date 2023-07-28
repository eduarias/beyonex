import logging

from robot.libraries.BuiltIn import BuiltIn
from selenium.common import ElementNotInteractableException

from page_objects.BasicPageObject import BasicPageObject, \
    capture_screen_on_failure, all_methods


@all_methods(capture_screen_on_failure)
class CartPage(BasicPageObject):
    """
    Page object for cart page.
    """

    _CART_TABLE_CELLS_LOCATOR = r'xpath://table//td'
    _CART_TOTAL_PRICE_LOCATOR = r'id:total'
    _PAYMENT_LOCATOR = r'xpath://button[@type="submit"]'
    _PAYMENT_IFRAME_LOCATOR = r'xpath://iframe[contains(@src, "stripe.com")]'
    _PAYMENT_EMAIL_LOCATOR = r'id:email'
    _PAYMENT_CARD_NUMBER_LOCATOR = r'id:card_number'
    _PAYMENTS_CARD_EXPIRATION_DATES_LOCATOR =r'id:cc-exp'
    _PAYMENT_CARD_CVV_LOCATOR = r'id:cc-csc'
    _PAYMENT_CARD_PAY_BUTTON_LOCATOR = r'id:submitButton'
    _PAYMENT_CARD_BILLING_ZIP_LOCATOR = r'id:billing-zip'

    def click_on_pay_with_card(self):
        self._webdriver.click_button(self._PAYMENT_LOCATOR)

    def get_cart_products(self):
        cells = self._webdriver.get_webelements(self._CART_TABLE_CELLS_LOCATOR)
        cells_grouped = [cells[n:n+2] for n in range(0, len(cells), 2)]
        products = {}
        for cell_group in cells_grouped:
            products[self._webdriver.get_text(cell_group[0])] = int(self._webdriver.get_text(cell_group[1]))
        return products

    def get_total_price(self):
        return self._clean_numbers(self._webdriver.get_text(self._CART_TOTAL_PRICE_LOCATOR))

    def select_card_payment_frame(self):
        self._webdriver.select_frame(self._PAYMENT_IFRAME_LOCATOR)

    def unselect_card_payment_iframe(self):
        self._webdriver.unselect_frame(self._PAYMENT_IFRAME_LOCATOR)

    def input_email(self, email_address):
        self._webdriver.wait_until_element_is_visible(self._PAYMENT_EMAIL_LOCATOR)
        self._webdriver.input_text(self._PAYMENT_EMAIL_LOCATOR, email_address)

    def input_card_number(self, card_number):
        logging.info(f'Card number: {card_number}')
        written_number = None
        retry = 0
        while written_number != card_number and retry <= 2:
            self.write_credit_card_number(card_number)
            written_number = self._webdriver.get_element_attribute(
                self._PAYMENT_CARD_NUMBER_LOCATOR, 'value').replace(' ', '')
            logging.info(f'Written card number: {written_number}')
            retry += 1

    def write_credit_card_number(self, card_number):
        self._webdriver.click_element(self._PAYMENT_CARD_NUMBER_LOCATOR)
        self._webdriver.press_keys(self._PAYMENT_CARD_NUMBER_LOCATOR, card_number[0:4])
        self._webdriver.press_keys(None, card_number[4:])

    def input_card_expiration_date(self, card_expiration_date):
        logging.info(f'Expiration date: {card_expiration_date}')
        self._webdriver.press_keys(self._PAYMENTS_CARD_EXPIRATION_DATES_LOCATOR, card_expiration_date[0:2])
        self._webdriver.press_keys(None, card_expiration_date[2:])

    def input_card_cvv(self, card_cvv):
        self._webdriver.input_text(self._PAYMENT_CARD_CVV_LOCATOR, card_cvv)

    def input_zip_code_if_needed(self, zip_code):
        self._webdriver.press_keys(self._PAYMENT_CARD_CVV_LOCATOR, "TAB")
        try:
            self._webdriver.input_text(self._PAYMENT_CARD_BILLING_ZIP_LOCATOR, zip_code)
        except ElementNotInteractableException:
            pass

    def click_on_card_pay_button(self):
        self._webdriver.click_button(self._PAYMENT_CARD_PAY_BUTTON_LOCATOR)