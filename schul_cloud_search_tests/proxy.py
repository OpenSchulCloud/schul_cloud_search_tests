from bottle import Bottle, request, response
import sys
import os
import requests
from schul_cloud_resources_server_tests.tests.fixtures import StoppableWSGIRefServerAdapter
if "" in sys.path:
    sys.path.append(".")
from schul_cloud_search_tests.search_tests import run_request_tests, run_response_tests

ENDPOINT_STOP = "/stop"
REDIRECT_TO = "http://localhost:8080"


def pytest_errors():
    """Return the formatted pytest errors, jsonapi compatible."""
    return {
              "errors":[
                {
                  "status": 409,
                  "title": "Conflict",
                  "detail": "The request or response contained some errors."
                }
              ],
              "jsonapi": {
                "version": "1.0",
                "meta": {
                  "name": "shcul_cloud/schul_cloud_search_tests", 
                  "source": 
                    "https://github.com/schul-cloud/schul_cloud_search_tests",
                  "description":
                    "These are the tests for the search engines."
                }
              }
            }


def test_response(target_url):
    """Test the request and the response to the search engine."""
    print("query string:", request.query_string)
    exit_code = run_request_tests()
    if exit_code != 0:
        # http://bottlepy.org/docs/dev/api.html?highlight=status#bottle.BaseResponse.status_code
        response.status = 409
        return pytest_errors()
    answer = requests.get(target_url + "?" + request.query_string)
    run_response_tests(answer)
    return answer.json()


def get_app(endpoint="/", target_url="http://localhost:8080"):
    """Return a bottle app that tests the request and the response."""
    app = Bottle()
    app.get(endpoint, callback=lambda: test_response(target_url))
    return app


def run(app, host="0.0.0.0", port=8081):
    """Run a stoppable bottle app."""
    server = StoppableWSGIRefServerAdapter(host=host, port=port)
    app.get(ENDPOINT_STOP, callback=lambda: server.shutdown(blocking=False))
    app.run(debug=True, server=server)
    


def main(host="0.0.0.0", port=8081, endpoint="/", target_url="http://localhost:8080"):
    """Start the server."""
    app = get_app(endpoint=endpoint, target_url=target_url)
    run(app, host=host, port=port)


__all__ = ["main", "app"]

if __name__ == "__main__":
    main()
