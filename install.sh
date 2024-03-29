#!/bin/bash
set -x
PIP=""

if [[ "$(which python3)" != "" ]]; then
    PIP="$(which python3) -m pip"
elif [[ "$(which python)" != "" ]]; then
    PIP="$(which python) -m pip"
elif [[ "$(which pip3)" != "" ]]; then
    PIP="$(which pip3)"
elif [[ "$(which pip)" != "" ]]; then
    PIP="$(which pip)"
else
    echo "Could not find pyhton/pip"
    exit 1
fi

$PIP install -U pdm

pdm install

pdm run pre-commit install
pdm run pre-commit install -t commit-msg

ASK_TOKEN=1
if [[ -f ".env" ]]; then
    . .env
    set +x
    if [[ "$DISCORD_TOKEN" != "" ]]; then
	echo "DISCORD_TOKEN env var already set"
	set -x
	ASK_TOKEN=0
    fi
    set -x
fi
if [[ "$ASK_TOKEN" == "1" ]]; then
    set +x
    echo "Discord token: "
    read DISCORD_TOKEN
    set -x
    echo "DISCORD_TOKEN=$DISCORD_TOKEN" >> .env
fi

echo "OK"
