from schul_cloud_resources_api_v1.schema import get_schemas
from pytest import mark
from schul_cloud_search_tests.tests.assertions import assertIsError, ERROR_CLIENT_REQUEST
from pprint import pprint


@mark.parametrize("param", ["page[offset]", "page[limit]"])
@mark.parametrize("value", ["", "asd", "-1"])
def test_parameter_must_be_positive_integer(search_engine, param, value):
    """
    According to
    - https://github.com/schul-cloud/resources-api-v1#search-api
    - http://jsonapi.org/format/#fetching-pagination
    page[offset] and page[limit] must be positive integers.
    
    This is an invalid request, according to
    - https://github.com/schul-cloud/schul_cloud_search_tests#specification
    the return code must be ERROR_CLIENT_REQUEST.
    """
    result = search_engine.request(params={param:value, "q":"test"})
    assert result.status_code == ERROR_CLIENT_REQUEST
    assertIsError(result.json(), ERROR_CLIENT_REQUEST)
    
    
def test_q_is_a_required_query(search_engine):
    """
    According to the Search API https://github.com/schul-cloud/resources-api-v1#search-api
    q is required
    """
    result = search_engine.request(params={})
    assert result.status_code == ERROR_CLIENT_REQUEST
    data = result.json()
    assertIsError(data, ERROR_CLIENT_REQUEST)
    errors = [error for error in data["errors"]
             if error["meta"].get("test_function") == "test_request_has_query"]
    assert errors, "There should be such an error function"
    meta = errors[0]["meta"]
    url_start = search_engine.proxy_url + "code/search_tests/test_request.py#"
    assert meta["source"].startswith(url_start)
    from schul_cloud_search_tests.search_tests.test_request import test_request_has_query
    assert meta["source-line"] == test_request_has_query.__code__.co_firstlineno


@mark.parametrize("parameter,parameter_is_correct", [
        ("asd", False),
        ("start- _abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", True),
        ("", True),
        ("asdA", True),
        ("asd-a", True),
        ("asd a", True),
        ("asd_a", True),
        ("asd-", False),
        ("asd ", False),
        ("asd_", False),
        ("page[offset]", True),
        ("page[limit]", True),
        ("page[asdas]", False),
        ("sort", True),
        ("filter[asdsa]", True),
        ("filter[]", False),
        ("filter[a.b]", True),
        ("filter[", False),
        ("родина", True),
        ("родина", True),
    ])
def test_all_parameter_names_are_jsonapi_compatible(
        search_engine, parameter, parameter_is_correct):
    """make sure the valid and invalid parameters are fed back."""
    response = search_engine.request({parameter:"4", "q":"test"})
    json = response.json()
    if parameter_is_correct:
        assert json == search_engine.last_response
    else:
        assertIsError(json, ERROR_CLIENT_REQUEST)

