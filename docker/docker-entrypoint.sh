#!/bin/sh

set -e

params="$@"

rm -rf /test/output/*

while ! curl -sSL "http://${GRID}:4444/wd/hub/status" 2>&1 | jq -r '.value.ready' 2>&1 | grep "true" >/dev/null; do
  echo 'Waiting for the Grid'
  sleep 1
done
echo "Selenium Grid is up - executing tests"

robot --outputdir /test/output test/tests || exit_code=$?
#robot --help
echo "Robot exit code ${exit_code}"