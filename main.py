from gc import callbacks
import secret, sys, discord, random, asyncio, time
from site import venv
from turtle import update
from discord.ext import commands
from discord.ui import Button, View
import data as quizz_data
import data as pendu_data
from emojis import Emojis

intents=discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="+", intents=intents)
emoji = Emojis()

@bot.event
async def on_ready():
    print("o==================================================================o")
    print("|                         JE SUIS PRET                             |")
    print("o==================================================================o")

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

# ███╗   ███╗███████╗███╗   ███╗ ██████╗      ██╗██╗
# ████╗ ████║██╔════╝████╗ ████║██╔═══██╗     ██║██║
# ██╔████╔██║█████╗  ██╔████╔██║██║   ██║     ██║██║
# ██║╚██╔╝██║██╔══╝  ██║╚██╔╝██║██║   ██║██   ██║██║
# ██║ ╚═╝ ██║███████╗██║ ╚═╝ ██║╚██████╔╝╚█████╔╝██║
# ╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝  ╚════╝ ╚═╝

# ███╗   ███╗ ██████╗ ████████╗██╗   ██╗███████╗
# ████╗ ████║██╔═══██╗╚══██╔══╝██║   ██║██╔════╝
# ██╔████╔██║██║   ██║   ██║   ██║   ██║███████╗
# ██║╚██╔╝██║██║   ██║   ██║   ██║   ██║╚════██║
# ██║ ╚═╝ ██║╚██████╔╝   ██║   ╚██████╔╝███████║
# ╚═╝     ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚══════╝

motus_data = {"answer": "", "running": False, "history": [], "index": 0, "last_message": None}

def check_word_in_motus(word: str, answer: str):
    output = ""

    for i, letter in enumerate(word):
        if letter == answer[i]:
            output += emoji.square.green
        elif letter in answer:
            output += emoji.square.orange
        else:
            output += emoji.square.black
    return output

def write_word_emojis(word: str):
    word_emojis = ""
    for letter in word:
        if (letter in emoji.letters):
            word_emojis += emoji.letters[letter]
        else:
            word_emojis += emoji.square.black
    return word_emojis

def display_history(history: list):
    history_emojis = ""
    for word in history:
        if (word == ""):
            history_emojis += emoji.square.blue * len(motus_data["answer"])
            history_emojis += "\n"
            history_emojis += emoji.square.black * len(motus_data["answer"])
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
    print("MOTUS: " + motus_data["answer"])
    motus_data["running"] = True
    motus_data["index"] = 0
    sent = await ctx.send(display_history(motus_data["history"]))
    motus_data["last_message"] = [sent.id, sent.channel.id]

@bot.listen('on_message')
async def wait_message_motus(message: discord.Message):
    global motus_data
    if (motus_data["running"] and message.author.id != 991271491809316865 and len(message.content) == len(motus_data["answer"]) and message.content.lower() in pendu_data.pendu_data):
        user_message = message.content.upper()
        motus_data["history"][motus_data["index"]] = user_message
        motus_data["index"] += 1
        channel = bot.get_channel(motus_data["last_message"][1])
        msg = await channel.fetch_message(motus_data["last_message"][0])
        sent = await message.channel.send(display_history(motus_data["history"]))
        motus_data["last_message"] = [sent.id, sent.channel.id]
        if (user_message == motus_data["answer"]):
            motus_data["running"] = False
            await message.channel.send("Bravo !")
            return
        if (motus_data["index"] == 6):
            await message.channel.send("Le mot était: " + motus_data["answer"])
            motus_data["running"] = False
            motus_data["answer"] = ""
            motus_data["history"] = ["" for i in range(6)]
            motus_data["index"] = 0
            return
        await msg.delete()

# ██████╗ ███████╗███╗   ██╗██████╗ ██╗   ██╗
# ██╔══██╗██╔════╝████╗  ██║██╔══██╗██║   ██║
# ██████╔╝█████╗  ██╔██╗ ██║██║  ██║██║   ██║
# ██╔═══╝ ██╔══╝  ██║╚██╗██║██║  ██║██║   ██║
# ██║     ███████╗██║ ╚████║██████╔╝╚██████╔╝
# ╚═╝     ╚══════╝╚═╝  ╚═══╝╚═════╝  ╚═════╝ 

is_pendu = -1
tentative = 11

def replace_char(string: str, char: str, index: int):
    return string[:index] + char + string[index + 1:]

@bot.command()
async def pendu(ctx: commands.Context):
    global pendu_word
    global is_pendu
    global words
    tentative = 11
    pendu_word = pendu_data.pendu_data[random.randint(0, len(pendu_data.pendu_data) - 1)]
    words="_"*len(pendu_word)
    words = pendu_word[0] + words[1:]
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
            tentative = 11
            is_pendu = -1
        if tentative <= 0:
            await message.channel.send(f"`Perdu, le mot était : {pendu_word} !`")
            tentative = 11
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

# ███████╗███╗   ██╗ █████╗ ██╗  ██╗███████╗
# ██╔════╝████╗  ██║██╔══██╗██║ ██╔╝██╔════╝
# ███████╗██╔██╗ ██║███████║█████╔╝ █████╗  
# ╚════██║██║╚██╗██║██╔══██║██╔═██╗ ██╔══╝  
# ███████║██║ ╚████║██║  ██║██║  ██╗███████╗
# ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝

is_snake = -1

class Snake:
    def __init__(self, userid: int, messageid: int, channelid: int):
        self.lastupdate = time.time()
        self.userid = userid
        self.messageid = messageid
        self.channelid = channelid
        self.screen = [[0 for i in range(9)] for j in range(9)]
        self.pos = [random.randint(3, 6), random.randint(3, 6)]
        self.dir = random.choice(["right", "left", "up", "down"])
        self.tail = []
        self.snake = {"body": emoji.square.green, "head": emoji.square.crossed_green, "background": emoji.square.black, "apple": emoji.square.red}

    def draw(self):
        line = ""
        for i, y in enumerate(self.screen):
            for j, x in enumerate(y):
                if i == self.pos[0] and j == self.pos[1]:
                    line += self.snake["head"]
                elif [i, j] in self.tail:
                    line += self.snake["body"]
                else:
                    line +=self.snake["background"]
            line += "\n"
        return line
    
    def update(self):
        print(self.tail)
        if self.dir == "right":
            self.pos[1] += 1
        elif self.dir == "left":
            self.pos[1] -= 1
        elif self.dir == "up":
            self.pos[0] -= 1
        elif self.dir == "down":
            self.pos[0] += 1
        if self.pos[0] < 0:
            self.pos[0] = 8
        elif self.pos[0] > 8:
            self.pos[0] = 0
        elif self.pos[1] < 0:
            self.pos[1] = 8
        elif self.pos[1] > 8:
            self.pos[1] = 0
        if self.pos in self.tail:
            return False
        self.tail.append(self.pos[:])
        if self.pos == [10, 10]:
            self.tail.append(self.pos[:])
        if len(self.tail) > 5:
            self.tail.pop(0)
        return True


@bot.command()
async def snake(ctx: commands.Context):
    print("starting a new snake game: ", ctx.author.name)
    snake = Snake(ctx.author.id, ctx.message.id, ctx.channel.id)

    async def quit(interaction):
        await interaction.message.delete()
        return True

    async def go_up(interaction):
        await interaction.response.defer()
        print("going up")
        if snake.dir != "down":
            snake.dir = "up"
    async def go_down(interaction):
        await interaction.response.defer()
        print("going down")
        if snake.dir != "up":
            snake.dir = "down"
    async def go_left(interaction):
        await interaction.response.defer()
        print("going left")
        if snake.dir != "right":
            snake.dir = "left"
    async def go_right(interaction):
        await interaction.response.defer()
        print("going right")
        if snake.dir != "left":
            snake.dir = "right"

    async def draw_buttons():
        view = View()

        buttons = []
        buttons.append(Button(label=" ", style=discord.ButtonStyle.gray))
        buttons.append(Button(label=" ", style=discord.ButtonStyle.green))
        buttons[1].callback = go_up
        buttons.append(Button(label=" ", style=discord.ButtonStyle.grey))
        buttons.append(Button(label=" ", style=discord.ButtonStyle.grey))
        buttons.append(Button(label=" ", style=discord.ButtonStyle.red))
        buttons[4].callback = quit

        buttons.append(Button(label=" ", style=discord.ButtonStyle.green))
        buttons[5].callback = go_left
        buttons.append(Button(label=" ", style=discord.ButtonStyle.grey))
        buttons.append(Button(label=" ", style=discord.ButtonStyle.green))
        buttons[7].callback = go_right
        buttons.append(Button(label=" ", style=discord.ButtonStyle.grey))
        buttons.append(Button(label=" ", style=discord.ButtonStyle.grey))

        buttons.append(Button(label=" ", style=discord.ButtonStyle.grey))
        buttons.append(Button(label=" ", style=discord.ButtonStyle.green))
        buttons[11].callback = go_down
        buttons.append(Button(label=" ", style=discord.ButtonStyle.grey))
        buttons.append(Button(label=" ", style=discord.ButtonStyle.grey))
        buttons.append(Button(label=" ", style=discord.ButtonStyle.grey))

        for button in buttons:
            view.add_item(button)
        return view



    msg = await ctx.send(snake.draw())
    while True:
        if (time.time() - snake.lastupdate) < 2.0:
            continue
        snake.lastupdate = time.time()
        if not snake.update():
            break
        await msg.edit(content=snake.draw(), view = await draw_buttons())

    

# ██████╗ ██╗   ██╗███╗   ██╗    ██████╗  ██████╗ ████████╗
# ██╔══██╗██║   ██║████╗  ██║    ██╔══██╗██╔═══██╗╚══██╔══╝
# ██████╔╝██║   ██║██╔██╗ ██║    ██████╔╝██║   ██║   ██║   
# ██╔══██╗██║   ██║██║╚██╗██║    ██╔══██╗██║   ██║   ██║   
# ██║  ██║╚██████╔╝██║ ╚████║    ██████╔╝╚██████╔╝   ██║   
# ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ╚═════╝  ╚═════╝    ╚═╝   

@bot.command()
@commands.has_role("BOT ADMIN")
async def stop(ctx: commands.Context):
    print(f"Stopping...\nStopped by {ctx.author.name} / {ctx.author.id}")
    await ctx.send(f"Stopping...\nStopped by {ctx.author.mention}")
    sys.exit(0)
bot.run(secret.secret)
