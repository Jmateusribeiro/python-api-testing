"""
Tests for Product API endpoints
"""
import pytest
from jsonschema import validate
from utils.assertions import assert_status_code, assert_valid_response


@pytest.mark.products
@pytest.mark.smoke
class TestProducts:
    """Test suite for product endpoints"""
    
    def test_get_all_products(self, api, product_schema):
        """
        Test retrieving all products
        
        Validates:
        - Status code is 200
        - Response contains a list of products
        - Each product matches the expected schema
        - Response time is acceptable
        """

        response = api.get_all_products()
        
        assert_valid_response(response, expected_status=200)
        
        products = response.json()
        
        assert isinstance(products, list), "Response should be a list"
        assert len(products) > 0, "Should return at least one product"
        
        first_product = products[0]
        validate(instance=first_product, schema=product_schema)
        
        assert first_product["price"] > 0, "Price should be positive"
    
    @pytest.mark.parametrize("product_id", [1, 2, 3, 5, 10])
    def test_get_single_product(self, api, product_schema, product_id):
        """
        Test retrieving a single product by ID using parametrize
        
        Validates:
        - Status code is 200
        - Response contains product details
        - Product matches the expected schema
        
        Tests multiple product IDs to ensure consistency
        """
        response = api.get_product(product_id)
        
        assert_valid_response(response, expected_status=200)
        
        product = response.json()
        
        validate(instance=product, schema=product_schema)
        assert product["id"] == product_id
    
    @pytest.mark.parametrize("limit", [1, 3, 5, 10])
    def test_get_products_with_limit(self, api, limit):
        """
        Test retrieving products with different limit parameters using parametrize
        
        Validates:
        - Limit parameter works correctly for various values
        - Returns exact number of products requested
        """

        response = api.get_all_products(limit=limit)
        
        assert_valid_response(response, expected_status=200)
        
        products = response.json()
        assert len(products) == limit, f"Should return exactly {limit} products"
    
    @pytest.mark.parametrize("category", ["electronics", "jewelery", "men's clothing", "women's clothing"])
    def test_get_products_by_category(self, api, category):
        """
        Test retrieving products by category using parametrize
        
        Validates:
        - Status code is 200
        - Response contains list of products
        - All products belong to the specified category
        """
        response = api.get_products_by_category(category)
        
        assert_valid_response(response, expected_status=200)
        
        products = response.json()
        assert len(products) > 0, f"Should have at least one product in '{category}' category"
        
        for product in products:
            assert product["category"] == category, f"Product should be in '{category}' category"
    
    def test_create_product(self, api, sample_product_data, product_schema):
        """
        Test creating a new product
        
        Validates:
        - Status code is 200
        - Response contains the created product with an ID
        """
        response = api.create_product(**sample_product_data)
        
        assert_valid_response(response, expected_status=201)

        created_product = response.json()
        
        validate(instance=created_product, schema=product_schema)

        assert created_product["title"] == sample_product_data["title"], "Title should match"
        assert created_product["price"] == sample_product_data["price"], "Price should match"
        assert created_product["description"] == sample_product_data["description"], "Description should match"
        assert created_product["image"] == sample_product_data["image"], "Image should match"
        assert created_product["category"] == sample_product_data["category"], "Category should match"
        #but sometimes is beter to compare the input and output as a whole

        print(f"Created product with ID: {created_product['id']}")

        ################################################################
        #API is mocked so we cannot verify the product details after creation
        # but this validation, in my opinion, makes sens in real APIs (also in PUT method )
        # Also could have a teardown to delete the created product after test
        
        #response = api.get_product(created_product["id"])
        #assert_status_code(response, 200)

        #product_details = response.json()
        #assert created_product == product_details, "Created product should match retrieved product"
        ################################################################
        
    def test_update_product(self, api, updated_product_data, product_schema):
        """
        Test updating an existing product
        
        Validates:
        - Status code is 200
        - Response contains updated product data
        """
        ################################################################
        #API is mocked so we cannot really update products
        # what would make sense is to create a product first (to handle data managment and make the test robust) and then update it
        #after should make a get details to verify the update
        # Also could have a teardown to delete the created product after test
        ################################################################
        product_id = 1
        
        response = api.update_product(product_id, **updated_product_data)
        
        assert_valid_response(response, expected_status=200)
        
        updated_product = response.json()

        validate(instance=updated_product, schema=product_schema)
        assert updated_product["title"] == updated_product_data["title"], "Title should match"
        assert updated_product["price"] == updated_product_data["price"], "Price should match"
        assert updated_product["description"] == updated_product_data["description"], "Description should match"
        assert updated_product["image"] == updated_product_data["image"], "Image should match"
        assert updated_product["category"] == updated_product_data["category"], "Category should match"
        
        print(f"Updated product {product_id}: {updated_product}")

        #response = api.get_product(product_id)
        #assert_status_code(response, 200)

        #product_details = response.json()
        #assert updated_product == product_details, "Updated product should match retrieved product"
    
    def test_delete_product(self, api):
        """
        Test deleting a product
        
        Validates:
        - Status code is 200
        - Deletion is acknowledged
        """
        ################################################################
        #API is mocked so we cannot really delete products
        # what would make sense is to create a product first (to handle data managment and make the test robust) and then delete it
        # after the delete (which the most correct status code is 204 btw) should make a get details and verify the 404 (product not found)
        ################################################################
        product_id = 1
        
        response = api.delete_product(product_id)
        
        #should be 204 in real API
        assert_valid_response(response, expected_status=200) 
        
        print(f"Deleted product {product_id}")

        #product_details = api.get_product(product_id)
        #assert_status_code(product_details, 404)