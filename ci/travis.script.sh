#!/bin/bash

echo "script"
ruby --version
overcommit --sign
overcommit --sign pre-commit
overcommit --run
python -m pytest  # In production, use pyenv python to launch pytest
coverage run --source nameshark_vcard -m py.test
