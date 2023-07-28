import logging

from robot.api.deco import keyword, library
from robot.libraries.BuiltIn import BuiltIn
from operator import itemgetter
from faker import Faker

from page_objects.HomePage import HomePage
from page_objects.ProductPage import ProductPage
from page_objects.CartPage import CartPage
from page_objects.ConfirmationPage import ConfirmationPage


@library(scope='GLOBAL')
class Service(object):
    """
    Class that contains functional keywords .
    """

    def __init__(self):
        self._homepage = HomePage()
        self._product = ProductPage()
        self._cart = CartPage()
        self._confirmation = ConfirmationPage()
        self.temperature = None
        self.products_to_cart = {}

    @keyword("Open Home Page On Browser and Get Temperature")
    def open_home_page_and_read_temp(self):
        self._homepage.open_home_page()
        self.temperature = self._homepage.read_temperature()
        logging.info(f'Current temperature value: {self.temperature}')

    @keyword('Select Moisturizers If Weather Is Below ${temp} Degrees Otherwise Skip')
    def select_moisturizers_by_weather(self, temp):
        if self.temperature > int(temp):
            BuiltIn().skip(msg=f'Skipping due to temperature of {temp} or above.')
        else:
            self._homepage.click_on_buy_moisturizers()

    @keyword('Select Sunscreens If Weather Is Above ${temp} Degrees Otherwise Skip')
    def select_sunscreens_by_weather(self, temp):
        if self.temperature < int(temp):
            BuiltIn().skip(msg=f'Skipping due to temperature of {temp} or lower.')
        else:
            self._homepage.click_on_buy_sunscreens()

    @keyword('A Cart Selecting The Least Expensive Product That Contains "${ingredient}"')
    def add_least_expensive_that_contains_element(self, ingredient):
        products = self._product.get_items_content()
        logging.info(f'Products list: {products}')
        selected_products = {name: price for name, price in products.items() if ingredient.lower() in name.lower()}
        logging.info(f'Selected products with {ingredient}: {selected_products}')
        cheaper_products = sorted(selected_products.items(), key=itemgetter(1))[:1]
        logging.info(f'Cheaper products with {ingredient}: {cheaper_products}')
        for product in cheaper_products:
            self._product.add_product_to_chart(product[0])
            self.products_to_cart[product[0]] = product[1]
            logging.info(f'Product added: {product[0]} with price {product[1]}')

    @keyword('Checking Out The Right Products On The Cart')
    def checking_out_products(self):
        self._product.click_on_cart()
        logging.info(f'Products that should be on cart: {self.products_to_cart}')
        products_in_cart = self._cart.get_cart_products()
        logging.info(f'Products in cart: {products_in_cart}')
        BuiltIn().should_be_equal(self.products_to_cart, products_in_cart,
                                  msg='Product in cart different than should be')

        page_total_price = int(self._cart.get_total_price())
        logging.info(f'Cart total price: {page_total_price}')
        product_total_price = sum(self.products_to_cart.values())
        BuiltIn().should_be_equal(page_total_price, product_total_price, msg='Total price do not match')

    @keyword('Paying With A Valid Test Card')
    def paying_with_valid_test_card(self):
        fake = Faker()
        self._cart.click_on_pay_with_card()
        self._cart.select_card_payment_frame()
        self._cart.input_email(fake.email())
        self._cart.input_card_number(fake.credit_card_number('visa'))
        self._cart.input_card_expiration_date(fake.credit_card_expire())
        self._cart.input_card_cvv(fake.credit_card_security_code())
        self._cart.input_zip_code_if_needed(fake.postcode())
        self._cart.click_on_card_pay_button()

    @keyword('Payment Should Be Successful')
    def payment_should_be_successful(self):
        BuiltIn().should_be_equal(self._confirmation.get_payment_status(), "PAYMENT SUCCESS",
                                  msg="Confirmation message not correct")
        self._confirmation.capture_screenshot_with_random_name()
