#!/bin/bash

. ci/travis_retry.sh

echo "install start"

# ruby
rvm --default use 2.3.2
ruby --version
travis_retry bundle install
bundle --version
bundle-audit --version
mdl --version
overcommit --version
reek --version
rubocop --version
ruby-lint --version
travis version --skip-completion-check

# python
if [ "${TRAVIS_BRANCH}" == "production" ]; then
    echo "Install pyenv"
    export PYENV_VERSION="${PYTHON}"
    export PATH="/home/travis/.pyenv/bin:/Users/travis/.pyenv/shims:${PATH}"
    curl --location https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"
    pyenv install "${PYTHON}"
    pyenv virtualenv venv
    # shellcheck disable=SC1091
    source activate venv
fi
python --version
travis_retry python -m pip install --upgrade pip wheel  # In production, use pyenv pip
travis_retry python -m pip install --require-hashes --requirement \
ci/travis.requirements.txt
travis_retry python -m pip install --require-hashes --requirement \
requirements.txt
# python setup.py install
# python setup.py develop

# make all
