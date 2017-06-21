"""These tests test the links which are available.

"""
from pytest import mark
import copy
from schul_cloud_search_tests.tests.assertions import (
    assertServerReplyIsWrong)
from pprint import pprint
import pytest


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


def test_the_limit_may_be_reduced_by_the_server(
        second_search, search_engine, limit):
    """The server can reduce the limit."""
    response = second_search.response
    second_search.parameters["page[limit]"] = str(limit + 1)
    result = search_engine.host(
         second_search.response, second_search.parameters
         ).request().json()
    assert result == response


def test_the_limit_can_not_be_increased_by_the_server(second_search):
    """The server may not increase the limit."""
    second_search.response["links"]["self"]["meta"]["limit"] += 1
    assertServerReplyIsWrong(second_search.request())
    

def test_count_does_not_match(first_search):
    """count must be equal t the number of objects."""
    first_search.response["links"]["self"]["meta"]["count"] += 1
    assertServerReplyIsWrong(first_search.request())


def test_count_can_not_be_greater_than_the_limit(first_search):
    """We reduce the limit so it is smaller than the count. This must be wrong."""
    first_search.response["links"]["self"]["meta"]["limit"] = \
        first_search.response["links"]["self"]["meta"]["count"] - 1
    assertServerReplyIsWrong(first_search.request())
    

def test_count_must_equal_limit_for_links_in_between(first_search, last_search):
    """If a search is not the last, the count must be equal to the limit.
    
    Test that
    - last last link is self
    """
    if first_search == last_search:
        pytest.skip("I need a request that is not the last.")
    response = first_search.response
    response["data"].pop()
    links = response["links"]
    meta = links["self"]["meta"]
    meta["count"] -= 1
    links["next"] = None
    assert links["self"]["href"] != links["last"], "precondition for the test"
    assertServerReplyIsWrong(first_search.request())


@mark.current
def test_next_link_of_last_request_must_be_null(last_search):
    """If the next link is set in the last request, it is an error."""
    last_search.response["links"]["next"] = \
        last_search.response["links"]["self"]["href"]
    print('last_search.response["links"]:', last_search.response["links"])
    assertServerReplyIsWrong(last_search.request())


