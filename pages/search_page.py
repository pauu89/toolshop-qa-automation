from playwright.sync_api import Page


class SearchPage:

    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.locator('[data-test="search-query"]')
        self.search_button = page.locator('[data-test="search-submit"]')
        self.products = page.locator('[data-test="product-name"]')

    def open(self):
        self.page.goto("https://practicesoftwaretesting.com/")

    def search(self, term: str):
        self.search_input.fill(term)
        self.search_button.click()

    def open_product(self, product_name: str):
        product = self.page.locator(
            'a:has([data-test="product-name"])',
            has_text=product_name
        ).first

        product.click()