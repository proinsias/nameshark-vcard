#!/bin/bash

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
