import random
import time

from discord import ButtonStyle
from discord.ext import commands
from discord.ui import Button, View

from bot.emojis import Emojis

emoji = Emojis()


class Snake:
    def __init__(self, userid: int, messageid: int, channelid: int):
        self.lastupdate = time.time()
        self.userid = userid
        self.messageid = messageid
        self.channelid = channelid
        self.screen = [[0 for _ in range(9)] for _ in range(9)]
        self.pos = [random.randint(3, 6), random.randint(3, 6)]
        self.dir = random.choice(["right", "left", "up", "down"])
        self.tail = []
        self.snake = {
            "body": emoji.square.green,
            "head": emoji.square.crossed_green,
            "background": emoji.square.black,
            "apple": emoji.square.red,
        }

    def draw(self):
        line = ""
        for i, y in enumerate(self.screen):
            for j, _ in enumerate(y):
                if i == self.pos[0] and j == self.pos[1]:
                    line += self.snake["head"]
                elif [i, j] in self.tail:
                    line += self.snake["body"]
                else:
                    line += self.snake["background"]
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


class SnakeGame(commands.Cog, name="SnakeGame", description="Snake Game!"):
    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()
        self.bot = bot
        self.is_snake = -1

    # ███████╗███╗   ██╗ █████╗ ██╗  ██╗███████╗
    # ██╔════╝████╗  ██║██╔══██╗██║ ██╔╝██╔════╝
    # ███████╗██╔██╗ ██║███████║█████╔╝ █████╗
    # ╚════██║██║╚██╗██║██╔══██║██╔═██╗ ██╔══╝
    # ███████║██║ ╚████║██║  ██║██║  ██╗███████╗
    # ╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
    @commands.command()
    async def snake(self, ctx: commands.Context):
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
            buttons.append(Button(label=" ", style=ButtonStyle.gray))
            buttons.append(Button(label=" ", style=ButtonStyle.green))
            buttons[1].callback = go_up
            buttons.append(Button(label=" ", style=ButtonStyle.grey))
            buttons.append(Button(label=" ", style=ButtonStyle.grey))
            buttons.append(Button(label=" ", style=ButtonStyle.red))
            buttons[4].callback = quit

            buttons.append(Button(label=" ", style=ButtonStyle.green))
            buttons[5].callback = go_left
            buttons.append(Button(label=" ", style=ButtonStyle.grey))
            buttons.append(Button(label=" ", style=ButtonStyle.green))
            buttons[7].callback = go_right
            buttons.append(Button(label=" ", style=ButtonStyle.grey))
            buttons.append(Button(label=" ", style=ButtonStyle.grey))

            buttons.append(Button(label=" ", style=ButtonStyle.grey))
            buttons.append(Button(label=" ", style=ButtonStyle.green))
            buttons[11].callback = go_down
            buttons.append(Button(label=" ", style=ButtonStyle.grey))
            buttons.append(Button(label=" ", style=ButtonStyle.grey))
            buttons.append(Button(label=" ", style=ButtonStyle.grey))

            for button in buttons:
                view.add_item(button)
            return view

        msg = await ctx.send(snake.draw())
        while True:
            if (time.time() - snake.lastupdate) < 2.0:
                continue
            snake.lastupdate = time.time()
            if not snake.update():
                await msg.edit(content=snake.draw() + "\nYou lost!")
                return
            await msg.edit(content=snake.draw(), view=await draw_buttons())


async def setup(bot: commands.Bot):
    await bot.add_cog(SnakeGame(bot))
    print(f"cog loaded: {__file__}")


async def teardown(bot: commands.Bot):
    print(f"cog unloaded: {bot}{__file__}")
