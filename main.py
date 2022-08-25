import secret
from discord.ext import commands
import discord
import random
import data as quizz_data
import data as pendu_data

intents=discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="+", intents=intents)

@bot.event
async def on_ready():
    print("JE SUIS PRET")


#      ██╗██╗   ██╗███████╗████████╗███████╗    ██████╗ ██████╗ ██╗██╗  ██╗
#      ██║██║   ██║██╔════╝╚══██╔══╝██╔════╝    ██╔══██╗██╔══██╗██║╚██╗██╔╝
#      ██║██║   ██║███████╗   ██║   █████╗      ██████╔╝██████╔╝██║ ╚███╔╝ 
# ██   ██║██║   ██║╚════██║   ██║   ██╔══╝      ██╔═══╝ ██╔══██╗██║ ██╔██╗ 
# ╚█████╔╝╚██████╔╝███████║   ██║   ███████╗    ██║     ██║  ██║██║██╔╝ ██╗
#  ╚════╝  ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝    ╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝
                            
juste_prix = -1

@bot.command()
async def alea(ctx: commands.Context, stop=""):
    """Pick a random number between 0 and 1000, i will tell to the next message if they are close to it.
    if you specify any argument after this command, it will stop the alea
    """
    global juste_prix
    if stop != "":
        juste_prix = -1
    else:
        juste_prix = random.randint(0, 1000)

@bot.listen('on_message')
async def wait_message_juste_prix(message: discord.Message):
    global juste_prix
    if (juste_prix != -1):
        if int(message.content) < juste_prix:
            await message.channel.send("plus haut")
        if int(message.content) > juste_prix:
            await message.channel.send("plus bas")
        if int(message.content) == juste_prix:
            await message.channel.send("c'est ça !")
            juste_prix = -1

# ██████╗ ███████╗███╗   ██╗██████╗ ██╗   ██╗
# ██╔══██╗██╔════╝████╗  ██║██╔══██╗██║   ██║
# ██████╔╝█████╗  ██╔██╗ ██║██║  ██║██║   ██║
# ██╔═══╝ ██╔══╝  ██║╚██╗██║██║  ██║██║   ██║
# ██║     ███████╗██║ ╚████║██████╔╝╚██████╔╝
# ╚═╝     ╚══════╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ 

is_pendu = -1
tentative = 7

def replace_char(string: str, char: str, index: int):
    return string[:index] + char + string[index + 1:]

@bot.command()
async def pendu(ctx: commands.Context):
    global pendu_word
    global is_pendu
    global words
    tentative = 8
    pendu_word = pendu_data.pendu_data[random.randint(0, len(pendu_data.pendu_data) - 1)]
    words="_"*len(pendu_word)
    words = pendu_word[0] + words[1:]
    print(pendu_word)
    print(words)
    is_pendu = 1
    for i in range(len(pendu_word)):
        if (words[0] == pendu_word[i]):
            words = replace_char(words, pendu_word[i], i)

@bot.listen('on_message')
async def wait_message_pendu(message: discord.Message):
    if (message.author.id == 991271491809316865):
        return
    global words
    global pendu_word
    global is_pendu
    global tentative
    if (is_pendu != -1):
        is_win = 0
        is_correct = 0
        for i in range(len(pendu_word)):
            if (message.content.lower() == pendu_word[i].lower()):
                words = replace_char(words, pendu_word[i], i)
                is_correct = 1
            if (words[i] == "_"):
                is_win = 1
        if is_correct == 0:
            tentative -= 1
        await message.channel.send(f"`{words}      tentative restantes : {tentative} !`")
        if is_win == 0:
            await message.channel.send(f"`Bien jouer le mot était bien : {words}` ")
            tentative = 8
            is_pendu = -1
        if tentative == 0:
            await message.channel.send(f"`Perdu, le mot était : {words} !`")
            tentative = 8
            is_pendu = -1

#  ██████╗ ██╗   ██╗██╗███████╗███████╗
# ██╔═══██╗██║   ██║██║╚══███╔╝╚══███╔╝
# ██║   ██║██║   ██║██║  ███╔╝   ███╔╝ 
# ██║▄▄ ██║██║   ██║██║ ███╔╝   ███╔╝  
# ╚██████╔╝╚██████╔╝██║███████╗███████╗
#  ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝╚══════╝

quiz = -1

@bot.command()
async def quizz(ctx: commands.Context):
    """Ask a knowledge question, and wait for response"""
    global quiz
    quiz = random.randint(0, len(quizz_data.reponse) - 1)
    await ctx.send(quizz_data.question[quiz])

@bot.listen('on_message')
async def wait_message_quizz(message: discord.Message):
    global quiz
    if (quiz != -1):
        if message.content.lower() in quizz_data.reponse[quiz]:
            await message.channel.send(f"{message.author.mention} Bravo tu as trouvé la réponse")
            quiz = -1

# ██████╗  █████╗ ████████╗██╗ ██████╗ 
# ██╔══██╗██╔══██╗╚══██╔══╝██║██╔═══██╗
# ██████╔╝███████║   ██║   ██║██║   ██║
# ██╔══██╗██╔══██║   ██║   ██║██║   ██║
# ██║  ██║██║  ██║   ██║   ██║╚██████╔╝
# ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝ 

@bot.command()
async def ratio(ctx: commands.Context):
    """Put R A T I O emoji to the message above"""
    cnt = 0
    last_msg = ""
    message = ctx.message
    if message == None:
        return
    await message.delete()
    async for last_msg in ctx.history(limit=1):
        await last_msg.add_reaction("🇷")
        await last_msg.add_reaction("🇦")
        await last_msg.add_reaction("🇹")
        await last_msg.add_reaction("🇮")
        await last_msg.add_reaction("🇴")

# ██████╗ ██╗   ██╗███╗   ██╗    ██████╗  ██████╗ ████████╗
# ██╔══██╗██║   ██║████╗  ██║    ██╔══██╗██╔═══██╗╚══██╔══╝
# ██████╔╝██║   ██║██╔██╗ ██║    ██████╔╝██║   ██║   ██║   
# ██╔══██╗██║   ██║██║╚██╗██║    ██╔══██╗██║   ██║   ██║   
# ██║  ██║╚██████╔╝██║ ╚████║    ██████╔╝╚██████╔╝   ██║   
# ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ╚═════╝  ╚═════╝    ╚═╝   
                                                         
bot.run(secret.secret)
