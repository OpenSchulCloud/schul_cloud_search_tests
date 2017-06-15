#!/bin/bash
set -e

python -m schul_cloud_search_tests.proxy 8081 /endpoint/ http://localhost:8080/v1/search/ &
echo 1
PID=$!
echo 2
sleep 1
echo 3
python -m schul_cloud_search_tests.stop 8081
echo 4
sleep 1
echo 5
! wait $PID
echo 6
