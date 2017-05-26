#!/usr/bin/env bash
set -o errexit  # exit on first error
set -o nounset  # don't allow use of unset variables
set -o pipefail  # produce a failure return code if any pipeline command errors
set -o xtrace  # echo commands
shopt -s failglob  # cause globs that don't get expanded to cause errors

echo "script"

ruby --version
overcommit --sign
overcommit --sign pre-commit
overcommit --run
python -m pytest
coverage run --source nameshark_vcard -m py.test
