from faker import Faker

from robot.libraries.BuiltIn import BuiltIn


def capture_screen_on_failure(instance, method):
    def handle_screen_capture(*args, **kwargs):
        try:
            return method(*args, **kwargs)
        except Exception as err:
            BasicPageObject.capture_screenshot_with_random_name(instance)
            raise err

    return handle_screen_capture


def all_methods(decorator):
    def decorate(cls):
        for attr in cls.__dict__:
            if callable(getattr(cls, attr)):
                setattr(cls, attr, decorator(cls(), getattr(cls, attr)))
        return cls

    return decorate


class BasicPageObject:
    """Basic Page Object to be inherited from"""

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    def __init__(self):
        self._fake = Faker()
        self._selenium_driver = None

    @property
    def _webdriver(self):
        if not self._selenium_driver:
            self._selenium_driver = BuiltIn().get_library_instance('SeleniumLibrary')
        return self._selenium_driver

    def capture_screenshot_with_random_name(self):
        self._webdriver.capture_page_screenshot(filename=f'selenium-screenshot-{self._fake.pystr(max_chars=40)}.png')

    @staticmethod
    def _clean_numbers(text):
        return ''.join(char for char in text if char.isdigit())
