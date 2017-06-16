"""
Run tests for the requests and responses.

If you mark your test with
@pytest.mark.request
your test is executed when the request arrives.

"""

from pytest import fixture
from schul_cloud_search_tests.search_tests import get_response


@fixture
def search():
    """The request to the server.
    
    The request from the client
    - http://bottlepy.org/docs/dev/api.html#bottle.BaseRequest
    """
    from bottle import request
    return request


@fixture
def response():
    """The response of the query.
    
    The response from the server.
    - http://docs.python-requests.org/en/master/api/#requests.Response
    """
    return get_response()


@fixture
def params(search):
    """The query parameters.
    
    The search request parameters:
    - http://bottlepy.org/docs/dev/api.html#bottle.FormsDict
    
    You can use params.get("q") to get the "q" parameter.
    """
    return search.query
