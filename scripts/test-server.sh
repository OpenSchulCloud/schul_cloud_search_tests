#!/bin/bash

set -e

echo "Starting server."
python -m schul_cloud_search_tests.search.server &
PID=$!
echo "..."

echo "Running tests."
python -m schul_cloud_search_tests.search --url=http://localhost:8080/v1

echo "Killing server..."
kill $PID
echo "Done"
