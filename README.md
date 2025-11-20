# Python API Testing with Pytest

## Summary

A professional API testing framework built with pytest to validate the [FakeStoreAPI](https://fakestoreapi.com) product endpoints. The project demonstrates industry best practices including client abstraction layers, reusable validation utilities, parametrized testing, JSON schema validation, and centralized test data management. Designed with maintainability and scalability in mind, following composition patterns and separation of concerns.

## Test Cases

| Test Name | Purpose | Validation |
|-----------|---------|------------|
| `test_get_all_products` | Retrieve all products from the API | Status 200, list response, schema compliance, positive prices |
| `test_get_single_product` | Retrieve individual products by ID (parametrized: 1, 2, 3, 5, 10) | Status 200, schema compliance, correct product ID |
| `test_get_products_with_limit` | Test limit parameter functionality (parametrized: 1, 3, 5, 10) | Status 200, exact count matches limit |
| `test_get_products_by_category` | Retrieve products filtered by category (parametrized: electronics, jewelery, men's clothing, women's clothing) | Status 200, all products match category |
| `test_create_product` | Create a new product via POST | Status 201, schema compliance, data integrity |
| `test_update_product` | Update existing product via PUT | Status 200, schema compliance, updated fields |
| `test_delete_product` | Delete a product via DELETE | Status 200 |

**Total Test Cases**: 7 test functions generating 17 individual test executions (due to parametrization)

## Conclusions

- **Composition Pattern**: Global validation function (`assert_valid_response`) composes smaller assertion functions for flexibility
- **Schema Validation**: JSON schema ensures API contract compliance across all responses
- **SSL Handling**: Properly disables SSL verification with warning suppression for local/testing environments
- **Mock API Limitations**: FakeStoreAPI doesn't persist data, which impacts testing:
  - Tests include commented sections showing real-world validation patterns (verifying CRUD operations, data persistence)
  - Negative tests (non-existent resources, invalid data, 404 scenarios) were not implemented due to mock API behavior

## How to Run

1. **Install dependencies**

   Using pyproject.toml:
   ```powershell
   pip install -e .
   ```
   Or using requirements.txt:
   ```powershell
   pip install -r requirements.txt
   ```

2. **Run all tests**:
   ```powershell
   pytest
   ```

3. **Run with detailed output**:
   ```powershell
   pytest -v
   ```

4. **Run specific markers**:
   ```powershell
   pytest -m smoke
   pytest -m products
   ```

5. **Generate HTML report** (auto-generated in reports/ by default):
   ```powershell
   pytest
   ```

## Project Structure

```
python-api-testing/
├── clients/                    # API client wrappers
│   ├── base_client.py         # Low-level HTTP client
│   ├── fake_store.py          # FakeStoreAPI domain client
│   └── __init__.py
├── config/                     # Configuration and settings
│   ├── settings.py            # Environment config & constants
│   └── __init__.py
├── data/                       # Test data constants
│   ├── products.py            # Product test data
│   └── __init__.py
├── schemas/                    # JSON schemas for validation
│   └── product_schema.json
├── tests/                      # Test suites and fixtures
│   ├── conftest.py            # Pytest fixtures
│   ├── test_products.py       # Product endpoint tests
│   └── __init__.py
├── utils/                      # Reusable assertion utilities
│   ├── assertions.py          # Validation functions
│   └── __init__.py
├── reports/                    # Test execution reports
│   └── report.html            # HTML test report
├── .env.example                # Environment variables template
├── .gitignore
├── pyproject.toml              # Project metadata & dependencies
├── requirements.txt            # Alternative dependency file
└── README.md
```