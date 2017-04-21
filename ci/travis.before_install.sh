#!/bin/bash

. ci/travis_retry.sh

echo "before_install"
echo "${VIRTUAL_ENV}"
df -h
date
pwd
uname -a
git config --global user.email "travis@travis.ci"  # overcommit Author
git config --global user.name "Travis CI"  # overcommit Author
git config --global hooks.copyrightholder "Francis T. O'Donovan"
git --version
git tag
shellcheck --version
ruby --version
gem update --system
gem --version
