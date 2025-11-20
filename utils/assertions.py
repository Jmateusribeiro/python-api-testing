"""
Assertion utilities for API testing
"""
from typing import Optional
from config.settings import settings


def assert_status_code(response, expected_status: int):
    """
    Assert that response has expected status code
    
    Args:
        response: Response object
        expected_status: Expected status code
    """
    assert response.status_code == expected_status, \
        f"Expected status {expected_status}, but got {response.status_code}. Response: {response.text}"


def assert_response_time(response, max_time_ms: int = 2000):
    """
    Assert that response time is below threshold
    
    Args:
        response: Response object
        max_time_ms: Maximum acceptable response time in milliseconds
    """
    response_time_ms = response.elapsed.total_seconds() * 1000
    assert response_time_ms < max_time_ms, \
        f"Response time {response_time_ms}ms exceeded maximum {max_time_ms}ms"


def assert_content_type(response, expected_type: str = "application/json"):
    """
    Assert that response has expected content type
    
    Args:
        response: Response object
        expected_type: Expected content type
    """
    content_type = response.headers.get("Content-Type", "")
    assert expected_type in content_type, \
        f"Expected content type '{expected_type}', but got '{content_type}'"

def assert_valid_response(
    response, 
    expected_status: int = 200,
    max_time_ms: Optional[int] = None,
    expected_content_type: str = "application/json"
):
    """
    Comprehensive response validation combining status code, response time, and content type
    
    Args:
        response: Response object
        expected_status: Expected HTTP status code (default: 200)
        max_time_ms: Maximum acceptable response time in milliseconds 
                     (default: uses settings.MAX_RESPONSE_TIME_MS)
        expected_content_type: Expected content type (default: "application/json")
    """

    if max_time_ms is None:
        max_time_ms = settings.MAX_RESPONSE_TIME_MS
    
    assert_status_code(response, expected_status)
    
    assert_response_time(response, max_time_ms=max_time_ms)
    
    assert_content_type(response, expected_content_type)