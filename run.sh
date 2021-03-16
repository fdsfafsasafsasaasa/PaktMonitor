#!/bin/sh
export PYTHONDONTWRITEBYTECODE=1
export OAUTHLIB_INSECURE_TRANSPORT="true"
python3 -B run.py $1