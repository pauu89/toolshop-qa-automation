# Toolshop QA Automation

Automated UI testing project for [Practice Software Testing](https://practicesoftwaretesting.com/) using **Playwright + Pytest + Python**.

The project focuses on validating key user flows related to product search and shopping cart functionality, using the **Page Object Model (POM)** design pattern.

## Technologies

- Python 3.10
- Pytest
- Playwright
- pytest-playwright
- pytest-html
- Page Object Model (POM)

## Project Structure

```text
toolshop-qa-automation/
│
├── pages/
│   ├── search_page.py
│   └── product_page.py
│
├── tests/
│   ├── test_search.py
│   └── test_cart.py
│
├── reports/
│   └── report.html
│
├── pytest.ini
├── requirements.txt
└── README.md
```

## Automated Test Coverage

### Product Search

- Search products by keyword
- Search for a nonexistent product
- Search using an empty term

### Shopping Cart

- Add a product to the cart
- Remove a product from the cart
- Change product quantity
- Validate that the cart total is updated according to the selected quantity

**Current test suite: 7 automated tests.**

## Test Design

The project uses the **Page Object Model (POM)** to separate test logic from page interactions.

For example:

```python
search_page.search("Hammer")
search_page.open_product("Hammer")

product_page.add_to_cart()
product_page.go_to_cart()
```

This approach improves:

- Maintainability
- Reusability
- Readability
- Separation of concerns

## Assertions

Playwright's built-in assertions are used to validate expected application behavior.

Examples include:

```python
expect(search_page.products).not_to_have_count(0)
```

```python
expect(product_page.cart_quantity).to_have_text("1")
```

```python
expect(product_page.cart_total).to_have_text(expected_total)
```

The cart total test calculates the expected value dynamically based on the product price:

```python
expected_total = f"${price * 2:.2f}"
```

## Installation

Clone the repository and navigate to the project directory:

```bash
git clone <repository-url>
cd toolshop-qa-automation
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

## Running the Tests

Run the complete test suite:

```bash
pytest -v
```

Expected result:

```text
7 passed
```

## HTML Test Report

The project uses `pytest-html` to generate an execution report.

Run:

```bash
pytest -v --html=reports/report.html --self-contained-html
```

The report contains:

- Test results
- Test duration
- Pass/fail status
- Environment information
- Execution details

The generated report is available at:

```text
reports/report.html
```

## QA Approach

The automated tests cover representative positive and negative scenarios for the application's search and shopping cart functionality.

The project was built as a QA automation practice project with emphasis on:

- Functional testing
- UI automation
- Regression coverage
- Maintainable test architecture
- Clear assertions
- Test execution reporting

## Future Improvements

Potential future additions include:

- API test automation
- Additional negative test cases
- Cross-browser execution
- CI/CD integration
- Screenshots and traces for failed tests
- Gherkin scenarios
- Automated test execution through GitHub Actions

### Estado de ejecución en CI/CD

Los 7 tests automatizados se ejecutan correctamente en el entorno local.

La ejecución mediante GitHub Actions puede verse afectada por la protección anti-bot (Cloudflare) del sitio de práctica [Practice Software Testing](https://practicesoftwaretesting.com), que puede bloquear las solicitudes provenientes de los runners de CI.

Esta restricción corresponde al entorno externo de pruebas y no implica necesariamente un error en los tests automatizados.

- **Entorno local:** 7 tests ejecutados correctamente.
- **GitHub Actions:** la ejecución puede verse afectada por las restricciones de acceso del sitio externo.
