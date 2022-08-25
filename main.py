import secret
from discord.ext import commands
import discord
import random
import data as quizz_data
import data as pendu_data

def replace_char(string: str, char: str, index: int):
    return string[:index] + char + string[index + 1:]

intents=discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="+", intents=intents)
juste_prix = -1
quiz = -1
is_pendu = -1

class Emojis:
    def __init__(self):
        self.orange_square = ":orange_square:"
        self.green_square = ":green_square:"
        self.black_large_square = ":black_large_square:"
        self.blue_square = ":blue_square:"
        self.letters = {
            "A": ":regional_indicator_a:",
            "B": ":regional_indicator_b:",
            "C": ":regional_indicator_c:",
            "D": ":regional_indicator_d:",
            "E": ":regional_indicator_e:",
            "F": ":regional_indicator_f:",
            "G": ":regional_indicator_g:",
            "H": ":regional_indicator_h:",
            "I": ":regional_indicator_i:",
            "J": ":regional_indicator_j:",
            "K": ":regional_indicator_k:",
            "L": ":regional_indicator_l:",
            "M": ":regional_indicator_m:",
            "N": ":regional_indicator_n:",
            "O": ":regional_indicator_o:",
            "P": ":regional_indicator_p:",
            "Q": ":regional_indicator_q:",
            "R": ":regional_indicator_r:",
            "S": ":regional_indicator_s:",
            "T": ":regional_indicator_t:",
            "U": ":regional_indicator_u:",
            "V": ":regional_indicator_v:",
            "W": ":regional_indicator_w:",
            "X": ":regional_indicator_x:",
            "Y": ":regional_indicator_y:",
            "Z": ":regional_indicator_z:",
        }
emoji = Emojis()

@bot.event
async def on_ready():
    print("JE SUIS PRET")


#      ██╗██╗   ██╗███████╗████████╗███████╗    ██████╗ ██████╗ ██╗██╗  ██╗
#      ██║██║   ██║██╔════╝╚══██╔══╝██╔════╝    ██╔══██╗██╔══██╗██║╚██╗██╔╝
#      ██║██║   ██║███████╗   ██║   █████╗      ██████╔╝██████╔╝██║ ╚███╔╝ 
# ██   ██║██║   ██║╚════██║   ██║   ██╔══╝      ██╔═══╝ ██╔══██╗██║ ██╔██╗ 
# ╚█████╔╝╚██████╔╝███████║   ██║   ███████╗    ██║     ██║  ██║██║██╔╝ ██╗
#  ╚════╝  ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝    ╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝
                                                                         
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

@bot.command()
async def pendu(ctx: commands.Context):
    """Pendu :D"""
    global pendu_word
    global is_pendu
    global words
    pendu_word = pendu_data.pendu_data[random.randint(0, len(pendu_data.pendu_data) - 1)]
    words="_"*len(pendu_word)
    words = pendu_word[0] + words[1:]
    print(pendu_word)
    print(words)
    is_pendu = 1
    for i in range(len(pendu_word)):
        if (words[0] == pendu_word[i]):
            words = pendu_word[i] + words[1:]
    await ctx.send(f"`{words}`")

@bot.listen('on_message')
async def wait_message_pendu(message: discord.Message):


    global words
    global pendu_word
    global is_pendu
    if (is_pendu != -1 and len(message.content) == 1):
        a = 0
        for i in range(len(pendu_word)):
            if (message.content.lower() == pendu_word[i].lower()):
                words = replace_char(words, pendu_word[i], i)
            if (words[i] == "_"):
                a = 1
        await message.channel.send(f"`{words}`")
        if a == 0:
            await message.channel.send(f"`Bien jouer le mot était bien : {words}` !")

#  ██████╗ ██╗   ██╗██╗███████╗███████╗
# ██╔═══██╗██║   ██║██║╚══███╔╝╚══███╔╝
# ██║   ██║██║   ██║██║  ███╔╝   ███╔╝ 
# ██║▄▄ ██║██║   ██║██║ ███╔╝   ███╔╝  
# ╚██████╔╝╚██████╔╝██║███████╗███████╗
#  ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝╚══════╝

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

# ███╗   ███╗ ██████╗ ████████╗██╗   ██╗███████╗
# ████╗ ████║██╔═══██╗╚══██╔══╝██║   ██║██╔════╝
# ██╔████╔██║██║   ██║   ██║   ██║   ██║███████╗
# ██║╚██╔╝██║██║   ██║   ██║   ██║   ██║╚════██║
# ██║ ╚═╝ ██║╚██████╔╝   ██║   ╚██████╔╝███████║
# ╚═╝     ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚══════╝

motus_data = {"answer": "", "running": False, "history": [], "index": 0}

def check_word_in_motus(word: str, answer: str):
    output = ""

    for i, letter in enumerate(word):
        if letter == answer[i]:
            output += emoji.green_square
        elif letter in answer:
            output += emoji.orange_square
        else:
            output += emoji.black_large_square
    return output

def write_word_emojis(word: str):
    word_emojis = ""
    for letter in word:
        if (letter in emoji.letters):
            word_emojis += emoji.letters[letter]
        else:
            word_emojis += emoji.black_large_square
    return word_emojis

def display_history(history: list):
    history_emojis = ""
    for word in history:
        if (word == ""):
            history_emojis += emoji.blue_square * len(motus_data["answer"])
            history_emojis += "\n"
            history_emojis += emoji.black_large_square * len(motus_data["answer"])
            history_emojis += "\n"
        else:
            history_emojis += write_word_emojis(word)
            history_emojis += "\n"
            history_emojis += check_word_in_motus(word, motus_data["answer"])
            history_emojis += "\n"
    return history_emojis

@bot.command()
async def motus(ctx: commands.Context):
    global motus_data
    motus_data["history"] = ["" for i in range(6)]
    motus_data["answer"] = (pendu_data.pendu_data[random.randint(0, len(pendu_data.pendu_data) - 1)]).upper()
    print("Motus: " + motus_data["answer"])
    motus_data["running"] = True
    motus_data["index"] = 0
    await ctx.send(display_history(motus_data["history"]))

@bot.listen('on_message')
async def wait_message_motus(message: discord.Message):
    global motus_data
    if (motus_data["running"] and message.author.id != 991271491809316865 and len(message.content) == len(motus_data["answer"])):
        user_message = message.content.upper()
        motus_data["history"][motus_data["index"]] = user_message
        motus_data["index"] += 1
        print(motus_data["history"])
        await message.channel.send(display_history(motus_data["history"]))
        if (motus_data["index"] == 6):
            message.channel.send("Le mot était: " + motus_data["answer"])
            motus_data["running"] = False
            motus_data["answer"] = ""
            motus_data["history"] = ["" for i in range(6)]
            motus_data["index"] = 0

# ██████╗ ██╗   ██╗███╗   ██╗    ██████╗  ██████╗ ████████╗
# ██╔══██╗██║   ██║████╗  ██║    ██╔══██╗██╔═══██╗╚══██╔══╝
# ██████╔╝██║   ██║██╔██╗ ██║    ██████╔╝██║   ██║   ██║   
# ██╔══██╗██║   ██║██║╚██╗██║    ██╔══██╗██║   ██║   ██║   
# ██║  ██║╚██████╔╝██║ ╚████║    ██████╔╝╚██████╔╝   ██║   
# ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ╚═════╝  ╚═════╝    ╚═╝   
                                                         
bot.run(secret.secret)
