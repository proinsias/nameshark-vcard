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
