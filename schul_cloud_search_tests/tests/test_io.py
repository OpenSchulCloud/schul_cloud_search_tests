from schul_cloud_resources_api_v1.schema import get_schemas
from pytest import mark
from schul_cloud_search_tests.tests.assertions import (
    assertIsError, ERROR_CLIENT_REQUEST, Q, ERROR_SERVER_RESPONSE)
from pprint import pprint


@mark.parametrize("response", get_schemas()["search-response"].get_valid_examples())
def test_valid_query_is_returned(search_engine, response):
    result = search_engine.host(response, {Q:"test"}).request()
    data = result.json()
    pprint(data)
    assert data == response


@mark.parametrize("invalid_response", ["{", "", b"asd", "{}", "[]"])
def test_invalid_return_values_are_handled(search_engine, invalid_response):
    """Test that a invalid responses still create a useful output.
    
    - invalid json
    - valid json but too small
    - bytes
    """
    result = search_engine.host(invalid_response, {Q:"test"}).request()
    assertIsError(result, ERROR_SERVER_RESPONSE)


@mark.skip(reason="TODO")
def test_invalid_return_header_type_is_handled():
    """The header must be correct.
    
    Wrong headers:
    - with parameters
    - application/json
    """


