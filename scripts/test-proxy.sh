#!/bin/bash
#
# Run the tests for the search eingine proxy
#
set -e

cd "`dirname \"$0\"`"

cd ..
pytest schul_cloud_search_tests/tests


