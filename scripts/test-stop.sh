#!/bin/bash
set -e

python -m schul_cloud_search_tests.proxy 8081 /endpoint/ http://localhost:8080/v1/search/ & PID=$!
sleep 1; python -m schul_cloud_search_tests.stop 8081; sleep 1
! wait $PID
