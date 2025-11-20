"""
Pytest configuration and shared fixtures
"""
import pytest
import json
import urllib3
import warnings
from pathlib import Path
from clients.fake_store import FakeStoreAPI
from data.products import SAMPLE_PRODUCT, UPDATED_PRODUCT

@pytest.fixture(scope="session")
def api():
    """
    Create a FakeStoreAPI instance for the test session
    
    Yields:
        FakeStoreAPI: High-level API wrapper
    """
    fake_store = FakeStoreAPI()
    yield fake_store
    fake_store.close()


@pytest.fixture(autouse=True)
def disable_ssl_warnings():
    warnings.filterwarnings("ignore", category=urllib3.exceptions.InsecureRequestWarning)
    

@pytest.fixture(scope="function")
def product_schema():
    """
    Load product JSON schema for validation
    
    Returns:
        dict: Product schema
    """
    schema_path = Path(__file__).parent.parent / "schemas" / "product_schema.json"
    with open(schema_path, "r") as f:
        return json.load(f)


@pytest.fixture(scope="function")
def sample_product_data():
    """
    Provide sample product data for testing
    
    Returns:
        dict: Sample product data from centralized data/products.py
    """
    return SAMPLE_PRODUCT


@pytest.fixture(scope="function")
def updated_product_data():
    """
    Provide updated product data for testing
    
    Returns:
        dict: Updated product data from centralized data/products.py
    """
    return UPDATED_PRODUCT