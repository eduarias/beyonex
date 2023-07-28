import time

from robot.libraries.BuiltIn import BuiltIn

from page_objects.BasicPageObject import BasicPageObject, \
    capture_screen_on_failure, all_methods


@all_methods(capture_screen_on_failure)
class ConfirmationPage(BasicPageObject):
    """
    Page object for confirmation page.
    """

    _PAYMENT_SUCCESS_LOCATOR = r'xpath://h2'
    _PAYMENT_PAGE_TITLE = r'xpath://title[text()="Confirmation"]'

    def get_payment_status(self):
        self._webdriver.wait_until_page_contains_element(self._PAYMENT_PAGE_TITLE)
        return self._webdriver.get_text(self._PAYMENT_SUCCESS_LOCATOR)
