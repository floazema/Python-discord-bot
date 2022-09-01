# discord bot

## install requirements

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
