#!/bin/bash
isort $1
pylint --rcfile=.pylintrc -f parseable -r n $1
mypy --ignore-missing-imports $1
pydocstyle -e -s -v --count $1
