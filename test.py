from email.message import Message
from itertools import count
from secret import *
from multiprocessing.connection import wait
from pydoc import cli
from discord.ext import commands
import discord

bot = commands.Bot(command_prefix='+')
client = discord.Client()

@client.event
async def on_ready():
    print("JE SUIS PRET")

@client.event
async def on_message(message):
    if message.content.lower() == "-free nitro":
        await message.channel.send("<https://www.youtube.com/watch?v=dQw4w9WgXcQ>")
    if message.content.lower() == "-help":
        await message.channel.send("demerde toi fdp")
    if message.content.lower() == "-ratio":
        if (message.reference) :
            message.reference.add_reaction("🇷")
        else :
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
client.run(secret)