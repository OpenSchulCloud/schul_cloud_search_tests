"""These tests test the links which are available.

"""
from pytest import mark
import copy
from schul_cloud_search_tests.tests.assertions import (
    assertIsError, ERROR_SERVER_RESPONSE)
from pprint import pprint


def test_correct_self_link_is_passed_through(linked_search):
    """Test that the linked search passes through the search engine."""
    for search in linked_search:
        result = search.request().json()
        #print("result:", result)
        response = search.response
        #print("response:", response)
        assert result == response
