#!/bin/bash
set -e

echo "Starting server."
python -m schul_cloud_search_tests.proxy
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
