#!/bin/bash

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
