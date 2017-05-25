#!/usr/bin/env bash
set -o errexit  # exit on first error
set -o nounset  # don't allow use of unset variables
set -o pipefail  # produce a failure return code if any pipeline command errors
set -o xtrace  # echo commands
shopt -s failglob  # cause globs that don't get expanded to cause errors

bash <(curl -s https://codecov.io/bash)
if [ "${TRAVIS_BRANCH}" == "develop" ]; then
    coverage combine
    coverage report
    coverage xml

    if [ ! -z "${CODACY_PROJECT_TOKEN}" ]; then
        python-codacy-coverage -r coverage.xml
    fi
    if [ ! -z "${CODECLIMATE_REPO_TOKEN}" ]; then
       codeclimate-test-reporter
    fi

    coveralls
fi
