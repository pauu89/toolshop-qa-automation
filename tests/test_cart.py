from playwright.sync_api import Page, expect

from pages.search_page import SearchPage
from pages.product_page import ProductPage


def test_add_product_to_cart(page: Page):
    search_page = SearchPage(page)
    product_page = ProductPage(page)

    search_page.open()
    search_page.search("Hammer")
    search_page.open_product("Hammer")

    product_page.add_to_cart()

    expect(product_page.cart_quantity).to_have_text("1")


def test_remove_product_from_cart(page: Page):
    search_page = SearchPage(page)
    product_page = ProductPage(page)

    search_page.open()
    search_page.search("Hammer")
    search_page.open_product("Hammer")

    product_page.add_to_cart()
    product_page.go_to_cart()

    expect(product_page.cart_quantity).to_have_text("1")

    product_page.remove_product()

    expect(product_page.cart_quantity).not_to_be_visible()

def test_change_product_quantity(page: Page):
    search_page = SearchPage(page)
    product_page = ProductPage(page)

    search_page.open()
    search_page.search("Hammer")
    search_page.open_product("Hammer")

    product_page.add_to_cart()
    product_page.go_to_cart()

    expect(product_page.product_quantity).to_have_value("1")

    product_page.set_quantity(2)

    expect(product_page.product_quantity).to_have_value("2")

def test_cart_total_updates_with_quantity(page: Page):
    search_page = SearchPage(page)
    product_page = ProductPage(page)

    search_page.open()
    search_page.search("Hammer")
    search_page.open_product("Hammer")

    product_page.add_to_cart()
    product_page.go_to_cart()

    price_text = product_page.product_price.inner_text()
    price = float(price_text.replace("$", ""))

    product_page.set_quantity(2)

    expected_total = f"${price * 2:.2f}"

    expect(product_page.cart_total).to_have_text(expected_total)