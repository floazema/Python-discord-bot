import asyncio
import os
import sys

from discord import Intents
from discord.ext.commands import Bot
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ.get("DISCORD_TOKEN")
if TOKEN is None:
    print(
        "DISCORD_TOKEN env variable need to be set (in .env file)",
        file=sys.stderr,
    )
    sys.exit(1)
COGS_PATH = os.environ.get("COGS_PATH", "cogs")
os.chdir(os.path.dirname(__file__))


async def main():
    intents = Intents.default()
    intents.message_content = True
    bot = Bot("+", intents=intents)

    for file in os.listdir(COGS_PATH):
        if file.endswith(".py"):
            await bot.load_extension(f"{COGS_PATH}.{file[:-3]}")
    bot.run(TOKEN)


if __name__ == "__main__":
    asyncio.run(main())
