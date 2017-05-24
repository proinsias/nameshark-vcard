#!/bin/bash

. ci/travis_retry.sh

echo "before_install"
echo "${VIRTUAL_ENV}"
df --human-readable
date --iso-8601=secondspwd
uname --all
git config --global user.email "travis@travis.ci"  # overcommit Author
git config --global user.name "Travis CI"  # overcommit Author
git config --global hooks.copyrightholder "Francis T. O'Donovan"
git --version
git describe --tags
shellcheck --version
ruby --version
gem update --system
gem --version
