from robot.libraries.BuiltIn import BuiltIn

from page_objects.BasicPageObject import BasicPageObject, \
    capture_screen_on_failure, all_methods


@all_methods(capture_screen_on_failure)
class HomePage(BasicPageObject):
    """
    Page object for home page.
    """
    _HOME_PAGE_URL = BuiltIn().get_variable_value('${SERVER}')
    _BROWSER = BuiltIn().get_variable_value('${BROWSER}')
    _REMOTE_BROWSER_URL = BuiltIn().get_variable_value('${REMOTE_BROWSER_URL}')
    _CURRENT_TEMPERATURE_LOCATOR = r'id: temperature'
    _BUY_MOISTURIZERS_BTN_LOCATOR = r'xpath://button[text()="Buy moisturizers"]'
    _BUY_SUNSCREENS_BTN_LOCATOR = r'xpath://button[text()="Buy sunscreens"]'

    def open_home_page(self):
        self._webdriver.open_browser(url=self._HOME_PAGE_URL,
                                     browser=self._BROWSER,
                                     remote_url=self._REMOTE_BROWSER_URL,
                                     options='add_argument("--disable-dev-shm-usage")')

    def read_temperature(self):
        temp_text = self._webdriver.get_text(self._CURRENT_TEMPERATURE_LOCATOR)
        temp = self._clean_numbers(temp_text)
        return int(temp)

    def click_on_buy_moisturizers(self):
        self._webdriver.click_button(self._BUY_MOISTURIZERS_BTN_LOCATOR)

    def click_on_buy_sunscreens(self):
        self._webdriver.click_button(self._BUY_SUNSCREENS_BTN_LOCATOR)
