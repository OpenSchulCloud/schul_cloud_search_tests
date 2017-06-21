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


def test_the_first_response_must_have_the_offest_0(linked_search):
    """The first request is done without specifying an offset.
    The offset 0 is implied."""
    linked_search[0].response["links"]["self"]["meta"]["offset"] = 1
    assertServerReplyIsWrong(linked_search[0].request())


def test_the_limit_may_be_reduced_by_the_server(first_search):
    """The server can reduce the limit."""
    response = first_search.response
    response["links"]["self"]["meta"]["limit"] -= 1
    result = first_search.request().json()
    assert result == response


def test_the_limit_can_not_be_increased_by_the_server(second_search):
    """The server may not increase the limit."""
    second_search.response["links"]["self"]["meta"]["limit"] += 1
    assertServerReplyIsWrong(second_search.request())
    

def test_count_does_not_match(first_search):
    """count must be equal t the number of objects."""
    first_search.response["links"]["self"]["meta"]["count"] += 1
    assertServerReplyIsWrong(first_search.request())


