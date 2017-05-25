#!/usr/bin/env bash
set -o errexit  # exit on first error
set -o nounset  # don't allow use of unset variables
set -o pipefail  # produce a failure return code if any pipeline command errors
set -o xtrace  # echo commands
shopt -s failglob  # cause globs that don't get expanded to cause errors

echo "script"

if [ "${TRAVIS_BRANCH}" == "production" ]; then
    export PATH="/home/travis/.pyenv/bin:/Users/travis/.pyenv/shims:${PATH}"
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
    # shellcheck disable=SC1091
    source activate venv
fi

ruby --version
overcommit --sign
overcommit --sign pre-commit
overcommit --run
python -m pytest  # In production, use pyenv python to launch pytest
coverage run --source nameshark_vcard -m py.test
