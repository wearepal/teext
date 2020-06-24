#!/bin/bash

echo "Begin check..." \
&& black -l 100 -t py36 . \
&& python -m pytest -vv tests/ \
&& mypy tests \
&& echo "Check all complete!"
