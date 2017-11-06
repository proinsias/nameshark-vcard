#!/usr/bin/env bash
set -o errexit  # exit on first error
set -o noclobber  # don't allow overwriting files
set -o nounset  # don't allow use of unset variables
set -o pipefail  # produce a failure return code if any pipeline command errors
shopt -s failglob  # cause globs that don't get expanded to cause errors

pip-compile --verbose --no-annotate --output-file requirements.in setup.py
rm -f requirements.txt
touch requirements.txt
# shellcheck disable=SC2046
hashin --verbose $(grep -v \# requirements.in) -r requirements.txt
rm -f requirements.in

pip-compile --verbose --no-annotate --output-file dev-requirements.in2 dev-requirements.in
rm -f dev-requirements.txt
touch dev-requirements.txt
# shellcheck disable=SC2046
hashin --verbose $(grep -v \# dev-requirements.in2 | cut -f 1 -d ";") -r dev-requirements.txt
rm -f dev-requirements.in2

pip-compile --verbose --no-annotate --output-file ci/travis.requirements.in2 ci/travis.requirements.in
rm -f ci/travis.requirements.txt
touch ci/travis.requirements.txt
# Do coverage manually due to some error.
# shellcheck disable=SC2046
hashin --verbose $(grep -v \# ci/travis.requirements.in2 | grep -v coverage) -r ci/travis.requirements.txt
hashin --verbose coverage -r ci/travis.requirements.txt
rm -f ci/travis.requirements.in2
