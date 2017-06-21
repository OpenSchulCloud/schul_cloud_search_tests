"""These tests test the links which are available.

"""
from pytest import mark
import copy
from schul_cloud_search_tests.tests.assertions import (
    assertServerReplyIsWrong)
from pprint import pprint


def test_correct_self_link_is_passed_through(linked_search):
    """Test that the linked search passes through the search engine."""
    for search in linked_search:
        result = search.request().json()
        response = search.response
        assert result == response

@mark.current
def test_the_first_response_must_have_the_offest_0(linked_search):
    """The first request is done without specifying an offset.
    The offset 0 is implied."""
    linked_search[0].response["links"]["self"]["meta"]["offset"] = 1
    assertServerReplyIsWrong(linked_search[0].request())
