# discord bot

## install requirements

**you need to have python -v >= 3.9**

exec one of this

- no devs

```bash
pip install pdm
pdm install --prod
echo "DISCORD_TOKEN=$TOKEN" >> .env # replace $TOKEN with your discord bot token
```

- for devs

```bash
pdm install --dev
echo "DISCORD_TOKEN=$TOKEN" >> .env # replace $TOKEN with your discord bot token
pdm run pre-commit install
pdm run pre-commit install -t commit-msg
```

- lazy people (for devs)

```bash
./install.sh
```

## run

```bash
# this will run python in the virtualenv
# and python will run ./bot/__main__.py
pdm run python bot
```

- if you are lazy to add pdm in front of python each time

run:
```bash
source .venv/bin/activate # bash /zsh ... (but not powershell bouh bad bouh)
```
