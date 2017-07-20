#!/bin/bash

set -e

cd "`dirname \"$0\"`"

dir="../dist"
if ! [ -d "$dir" ]; then
  echo "Directory $dir does not exist but is expected to exist."
  exit 1
fi

twine upload "$dir"/*
