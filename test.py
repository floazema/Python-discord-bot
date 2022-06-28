from secret import *
from discord.ext import commands
import discord
import random

bot = commands.Bot(command_prefix='+')
client = discord.Client()
juste_prix = -1

@client.event
async def on_ready():
    print("JE SUIS PRET")

@client.event
async def on_message(message):
    global juste_prix
    if message.content.lower() == "-help":
        await message.channel.send("-ratio: ratio someone\n -alea: joue au juste prix\n-alea stop: stop alea game")
    if message.content.lower() == "-ratio":
        cnt = 0
        last_msg = ""
        async for last_msg in message.channel.history(limit=2):
            if (cnt == 0):
                cnt += 1
                continue
            await message.delete()
            await last_msg.add_reaction("🇷")
            await last_msg.add_reaction("🇦")
            await last_msg.add_reaction("🇹")
            await last_msg.add_reaction("🇮")
            await last_msg.add_reaction("🇴")
    if message.content.lower() == "-alea":
        juste_prix = random.randint(0, 1000)
    if message.content.lower() == "-alea stop":
        juste_prix = -1
    if (juste_prix != -1):
        if int(message.content) < juste_prix:
            await message.channel.send("plus haut")
        if int(message.content) > juste_prix:
            await message.channel.send("plus bas")
        if int(message.content) == juste_prix:
            await message.channel.send("c'est ça !")
            juste_prix = -1
client.run(secret)