#!/bin/bash
set -e

echo "Starting server."
python -m schul_cloud_search_tests.proxy 8081 /endpoint/ http://localhost:8080/v1/search/ &
PID=$!
echo "..."
sleep 1

echo "Requesting stop."
python -m schul_cloud_search_tests.stop 8081
echo "..."
sleep 1

echo "Waiting for server..."
! wait $PID
echo "Done"
