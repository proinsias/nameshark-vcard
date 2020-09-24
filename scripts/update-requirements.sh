#!/usr/bin/env bash
set -o errexit  # exit on first error
set -o noclobber  # don't allow overwriting files
set -o nounset  # don't allow use of unset variables
set -o pipefail  # produce a failure return code if any pipeline command errors
shopt -s failglob  # cause globs that don't get expanded to cause errors

pip-compile --annotate --generate-hashes --header --reuse-hashes --upgrade --verbose \
    --output-file requirements.txt setup.py

safety check --file requirements.txt

pip-compile --annotate --generate-hashes --header --reuse-hashes --upgrade --verbose \
    --output-file dev-requirements.txt dev-requirements.in

safety check --file dev-requirements.txt
