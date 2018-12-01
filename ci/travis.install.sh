#!/usr/bin/env bash
set -o errexit  # exit on first error
set -o nounset  # don't allow use of unset variables
set -o pipefail  # produce a failure return code if any pipeline command errors
set -o xtrace  # echo commands
shopt -s failglob  # cause globs that don't get expanded to cause errors

. ci/travis_retry.sh

echo "install start"

# shellcheck
curl https://storage.googleapis.com/shellcheck/shellcheck-stable.linux.x86_64.tar.xz --output shellcheck-stable.tar.xz
tar --xz --extract --file shellcheck-stable.tar.xz
mv shellcheck-stable/shellcheck "${HOME}/bin/
rm --recursive --force shellcheck-stable shellcheck-stable.tar.xz
"${HOME}/bin/shellcheck --version

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

# npm
npm --version

# python
python --version
travis_retry python -m pip install --upgrade pip wheel
travis_retry python -m pip install --require-hashes --requirement \
requirements.txt
travis_retry python -m pip install --require-hashes --requirement \
dev-requirements.txt
# make all
