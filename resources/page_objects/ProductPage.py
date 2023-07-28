from robot.libraries.BuiltIn import BuiltIn

from page_objects.BasicPageObject import BasicPageObject, \
    capture_screen_on_failure, all_methods


@all_methods(capture_screen_on_failure)
class ProductPage(BasicPageObject):
    """
    Page object for product page.
    """

    _CART_LOCATOR = r'xpath://button[contains(@onclick, "goToCart")]'
    _ITEMS_LOCATOR = r'xpath://div[contains(@class, "text-center")]'
    _ITEM_CHART_BUTTON_LOCATOR = r'xpath://button[contains(@onclick, "%")]'

    def get_items_content(self):
        items = [self._webdriver.get_text(item) for item in self._webdriver.get_webelements(self._ITEMS_LOCATOR)]
        return {item.splitlines()[0]: int(self._clean_numbers(item.splitlines()[1])) for item in items}

    def add_product_to_chart(self, product_name):
        self._webdriver.click_button(self._ITEM_CHART_BUTTON_LOCATOR.replace('%', product_name))

    def click_on_cart(self):
        self._webdriver.click_button(self._CART_LOCATOR)