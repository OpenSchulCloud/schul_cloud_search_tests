from pytest import mark
import pytest


@mark.request
def test_request_has_query(params):
    """Test that the query includes a "q"."""
    assert params.get("q") is not None, (
        "Please pass a query string to with q=... to the request.")

@mark.request
@mark.parametrize("parameter", ["page[offset]", "page[limit]"])
def test_integer_parameters(params, parameter):
    """Test that page[offset] and page[limit]."""
    value = params.get(parameter)
    if value is None:
        pytest.skip("parameter {} absent".format(parameter))
    assert value.isdigit(), "The parameter {} must be a positive integer.".format(parameter)
