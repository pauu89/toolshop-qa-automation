from playwright.sync_api import Page, expect

from pages.search_page import SearchPage


def test_search_products_by_keyword(page: Page):
    search_page = SearchPage(page)

    search_page.open()
    search_page.search("Hammer")

    expect(search_page.products).not_to_have_count(0)


def test_search_nonexistent_product(page: Page):
    search_page = SearchPage(page)

    search_page.open()
    search_page.search("XYZ-NONEXISTENT-123")

    expect(search_page.products).to_have_count(0)

def test_search_with_empty_term(page: Page):
    search_page = SearchPage(page)

    search_page.open()
    search_page.search("")

    expect(search_page.products).not_to_have_count(0)