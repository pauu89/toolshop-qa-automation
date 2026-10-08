from playwright.sync_api import Page


class ProductPage:

    def __init__(self, page: Page):
        self.page = page
        self.add_to_cart_button = page.locator('[data-test="add-to-cart"]')
        self.cart_button = page.locator('[data-test="nav-cart"]')
        self.cart_quantity = page.locator('[data-test="cart-quantity"]')
        self.remove_button = page.locator('a.btn.btn-danger')
        self.product_quantity = page.locator('[data-test="product-quantity"]')
        self.product_price = page.locator('[data-test="product-price"]')
        self.cart_total = page.locator('[data-test="cart-total"]')

    def add_to_cart(self):
        self.add_to_cart_button.click()

    def go_to_cart(self):
        self.cart_button.click()

    def remove_product(self):
        self.remove_button.click()

    def set_quantity(self, quantity: int):
        self.product_quantity.fill(str(quantity))
        self.product_quantity.press("Enter")