"""
Base HTTP Client for making API requests
"""
import requests
import urllib3
from typing import Optional, Dict, Any
from config.settings import settings


class BaseClient:
    """Base HTTP client for making API requests"""
    
    def __init__(self, base_url: Optional[str] = None):
        """
        Initialize API client
        
        Args:
            base_url: Base URL for API requests. Defaults to settings.BASE_URL
        """
        self.base_url = base_url or settings.BASE_URL
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })
    
    def get(self, endpoint: str, params: Optional[Dict] = None, **kwargs) -> requests.Response:
        """
        Make a GET request
        
        Args:
            endpoint: API endpoint (will be appended to base_url)
            params: Query parameters
            **kwargs: Additional arguments to pass to requests
            
        Returns:
            Response object
        """
        url = f"{self.base_url}{endpoint}"
        response = self.session.get(url, params=params, timeout=settings.REQUEST_TIMEOUT, verify=False, **kwargs)
        return response
    
    def post(self, endpoint: str, data: Optional[Dict] = None, json: Optional[Dict] = None, **kwargs) -> requests.Response:
        """
        Make a POST request
        
        Args:
            endpoint: API endpoint
            data: Form data
            json: JSON payload
            **kwargs: Additional arguments to pass to requests
            
        Returns:
            Response object
        """
        url = f"{self.base_url}{endpoint}"
        response = self.session.post(url, data=data, json=json, timeout=settings.REQUEST_TIMEOUT, verify=False, **kwargs)
        return response
    
    def put(self, endpoint: str, data: Optional[Dict] = None, json: Optional[Dict] = None, **kwargs) -> requests.Response:
        """
        Make a PUT request
        
        Args:
            endpoint: API endpoint
            data: Form data
            json: JSON payload
            **kwargs: Additional arguments to pass to requests
            
        Returns:
            Response object
        """
        url = f"{self.base_url}{endpoint}"
        response = self.session.put(url, data=data, json=json, timeout=settings.REQUEST_TIMEOUT, verify=False, **kwargs)
        return response
    
    def delete(self, endpoint: str, **kwargs) -> requests.Response:
        """
        Make a DELETE request
        
        Args:
            endpoint: API endpoint
            **kwargs: Additional arguments to pass to requests
            
        Returns:
            Response object
        """
        url = f"{self.base_url}{endpoint}"
        response = self.session.delete(url, timeout=settings.REQUEST_TIMEOUT, verify=False, **kwargs)
        return response
    
    def set_auth_token(self, token: str):
        """
        Set authorization token in session headers
        
        Args:
            token: Bearer token
        """
        self.session.headers.update({"Authorization": f"Bearer {token}"})
    
    def close(self):
        """Close the session"""
        self.session.close()
