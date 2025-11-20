"""
FakeStoreAPI Client with domain-specific methods
"""
from typing import Optional, Dict, List, Any
from clients.base_client import BaseClient


class FakeStoreAPI:
    """Client for FakeStoreAPI with domain-specific methods"""
    
    def __init__(self, client: Optional[BaseClient] = None):
        """
        Initialize FakeStoreAPI client
        
        Args:
            client: BaseClient instance. If None, creates a new one.
        """
        self.client = client or BaseClient()
    
    # Products section
    
    def get_all_products(self, limit: Optional[int] = None, sort: Optional[str] = None):
        """
        Get all products
        
        Args:
            limit: Limit number of results
            sort: Sort order ('asc' or 'desc')
            
        Returns:
            Response object
        """
        params = {}
        if limit:
            params['limit'] = limit
        if sort:
            params['sort'] = sort
        
        return self.client.get("/products", params=params)
    
    def get_product(self, product_id: int):
        """
        Get a single product by ID
        
        Args:
            product_id: Product ID
            
        Returns:
            Response object
        """
        return self.client.get(f"/products/{product_id}")
    
    def create_product(self, title: str, price: float, description: str, 
                      category: str, image: str):
        """
        Create a new product
        
        Args:
            title: Product title
            price: Product price
            description: Product description
            category: Product category
            image: Product image URL
            
        Returns:
            Response object
        """
        payload = {
            "title": title,
            "price": price,
            "description": description,
            "category": category,
            "image": image
        }
        return self.client.post("/products", json=payload)
    
    def update_product(self, product_id: int, **kwargs):
        """
        Update a product
        
        Args:
            product_id: Product ID
            **kwargs: Fields to update (title, price, description, category, image)
            
        Returns:
            Response object
        """
        return self.client.put(f"/products/{product_id}", json=kwargs)
    
    def delete_product(self, product_id: int):
        """
        Delete a product
        
        Args:
            product_id: Product ID
            
        Returns:
            Response object
        """
        return self.client.delete(f"/products/{product_id}")
    
    def get_product_categories(self):
        """
        Get all product categories
        
        Returns:
            Response object
        """
        return self.client.get("/products/categories")
    
    def get_products_by_category(self, category: str):
        """
        Get products in a specific category
        
        Args:
            category: Category name
            
        Returns:
            Response object
        """
        return self.client.get(f"/products/category/{category}")
    
    def close(self):
        """Close the underlying client session"""
        self.client.close()
