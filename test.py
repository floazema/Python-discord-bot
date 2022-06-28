import secret
from discord.ext import commands
import discord
import random
import quizz as quizz_data

bot = commands.Bot(command_prefix='+')
juste_prix = -1
quiz = -1

@bot.event
async def on_ready():
    print("JE SUIS PRET")

@bot.command()
async def ratio(ctx: commands.Context):
    """Put R A T I O emoji to the message above"""
    cnt = 0
    last_msg = ""
    message = ctx.message
    if message == None:
        return
    await message.delete()
    async for last_msg in ctx.history(limit=2):
        if (cnt == 0):
            cnt += 1
            continue
        await last_msg.add_reaction("🇷")
        await last_msg.add_reaction("🇦")
        await last_msg.add_reaction("🇹")
        await last_msg.add_reaction("🇮")
        await last_msg.add_reaction("🇴")

@bot.command()
async def alea(ctx: commands.Context, stop=""):
    """Pick a random number between 0 and 1000, i will tell to the next message if they are close to it"""
    global juste_prix
    if stop != "":
        juste_prix = -1
    else:
        juste_prix = random.randint(0, 1000)

@bot.command()
async def quizz(ctx: commands.Context):
    """Ask a knowledge question, and wait for response"""
    global quiz
    quiz = random.randint(0, len(quizz_data.reponse) - 1)
    await ctx.send(quizz_data.question[quiz])

@bot.listen('on_message')
async def on_message_i_think(message: discord.Message):
    global juste_prix
    global quiz
    if message.content.lower() == "-help":
        await message.channel.send("command: +help")
    if message.content.lower() == "-ratio":
        await message.channel.send("command: +ratio")
    if message.content.lower() == "-alea":
        await message.channel.send("command: +alea")
    if message.content.lower() == "-alea stop":
        await message.channel.send("command: +alea")
    if message.content.lower() == "-quizz":
        await message.channel.send("command: +quizz")
    if (juste_prix != -1):
        if int(message.content) < juste_prix:
            await message.channel.send("plus haut")
        if int(message.content) > juste_prix:
            await message.channel.send("plus bas")
        if int(message.content) == juste_prix:
            await message.channel.send("c'est ça !")
            juste_prix = -1
    if (quiz != -1):
        if message.content.lower() in quizz_data.reponse[quiz]:
            await message.channel.send(f"{message.author.mention} Bravo tu as trouvé la réponse")
            quiz = -1

bot.run(secret.secret)
