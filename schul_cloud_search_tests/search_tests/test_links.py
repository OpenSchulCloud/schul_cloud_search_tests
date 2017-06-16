"""
Each test function here covers a part of the specification.
They are run when the server returns a request.
If they fail, the client gets feedback.

About the test functions:
Please provide
- A short description of what is tested
- Links to the specification, where this is specified.

These test functions all relate to the "links" attribute of the search response.
- https://github.com/schul-cloud/resources-api-v1/tree/master/schemas/search-response#search-reponse-1

"""
from pytest import mark


@mark.skip(reason="TODO")
def test_count():
    """
    count is the actual number of objects retrieved.
    """


@mark.skip(reason="TODO")
def test_():
    """
    offset is the start index in the list of objects.
    """


@mark.skip(reason="TODO")
def test_():
    """
    limit is the requested number of objects.
    """


@mark.skip(reason="TODO")
def test_():
    """
    If the end of the resource list is reached, count may be less than limit.
    """


@mark.skip(reason="TODO")
def test_():
    """
    If the limit is higher than the maximum limit the server has internally, the server sets the limit to the maximum available limit.
    """


@mark.skip(reason="TODO")
def test_():
    """
    If there are no resources, first, last, prev and next MUST be null.
    """


@mark.skip(reason="TODO")
def test_():
    """
    If the last page is reached, next MUST be null.
    """


@mark.skip(reason="TODO")
def test_():
    """
    If last is given, next must be given.
    """


@mark.skip(reason="TODO")
def test_():
    """
    If first is given, prev must be given.
    """

@mark.skip(reason="TODO")
def test_():
    """
    If count is less than limit, the next link MUST not skip objects.
    """


@mark.skip(reason="TODO")
def test_():
    """
    If the object has a self link, it can be retrieved.
    """


@mark.skip(reason="TODO")
def test_():
    """
    If links are present, they return a valid object.
    """


@mark.skip(reason="TODO")
def test_():
    """
    All links are absolute links using the host header field.
    """


@mark.skip(reason="TODO")
def test_():
    """
    
    """

