"""
This file contains the test configuration like fixtures.
"""
from pytest import fixture
from schul_cloud_resources_server_tests.tests.fixtures import ParallelBottleServer
from bottle import Bottle
import sys
import os
import requests
HERE = os.path.dirname(__file__)
MODULE_ROOT = os.path.join(HERE, "..", "..")
try:
    import schul_cloud_search_tests
except ImportError:
    sys.path.append(MODULE_ROOT)
from schul_cloud_search_tests.proxy import get_app


class Requester(object):
    """Shortcut to request a hosted resource."""
    
    def __init__(self, url):
        """Create a requester."""
        self._url = url
    
    def request(self):
        """Request the resource."""
        return requests.get(self._url)


class SearchEngine(object):
    """The search engine adapter.
    
    This includes:
    - the running search tests server
    - a bottle server returning the registeres responses
    """

    def __init__(self):
        """Create a search engine object."""
        self._queries = {}
        self._app = Bottle()
        self._reset_servers()
    
    def start(self):
        """Start the search engine tests and the search engine mock."""
        assert not self.is_started()
        self._server = ParallelBottleServer(self._app)
        self._search_app = get_app(target_url=self.search_engine_url)
        self._search_server = ParallelBottleServer(self._search_app)
        
    @property
    def search_engine_url(self):
        """Return the URL of the search engine."""
        assert self.is_started()
        url = self._server.url
        if not url.endswith("/"):
            url = url + "/"
        return url
        
    def stop(self):
        """Stop the search engine tests and the mock server."""
        assert self.is_started()
        self._server.shutdown()
        self._search_server.shutdown()
        self._reset_servers()

    def _reset_servers(self):
        """Create the starting condition"""
        self._server = None
        self._search_server = None
        self._search_app = None

    def is_started(self):
        """Return whether the server is started."""
        return self._server is not None
        
    def host(self, response, q=""):
        """Host the response given by the query."""
        assert q not in self._queries
        self._queries[q] = response
        request_url = self.search_engine_url + "?q=" + q
        return Requester(request_url)
    
    def clear(self):
        """Remove all hosted responses."""
        self._queries = {}


@fixture(scope="session")
def search_engine_session():
    """Return the server to store resources."""
    server = SearchEngine()
    server.start()
    yield server
    server.stop()


@fixture
def search_engine(search_engine_session):
    """Return a fresh server object with no resources."""
    search_engine_session.clear()
    yield search_engine_session
    search_engine_session.clear()
