import random

from discord import Message
from discord.ext import commands

from bot.dictionnary import dictionnary


class Pendu(commands.Cog, name="PenduGame", description="Pendu Game"):
    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()
        self.bot = bot
        self.is_pendu = -1
        self.tentative = 11
        self.words = ""
        self.pendu_word = ""

    def replace_char(self, string: str, char: str, index: int):
        index_end = index + 1
        return string[:index] + char + string[index_end:]

    # ██████╗ ███████╗███╗   ██╗██████╗ ██╗   ██╗
    # ██╔══██╗██╔════╝████╗  ██║██╔══██╗██║   ██║
    # ██████╔╝█████╗  ██╔██╗ ██║██║  ██║██║   ██║
    # ██╔═══╝ ██╔══╝  ██║╚██╗██║██║  ██║██║   ██║
    # ██║     ███████╗██║ ╚████║██████╔╝╚██████╔╝
    # ╚═╝     ╚══════╝╚═╝  ╚═══╝╚═════╝  ╚═════╝
    @commands.command()
    async def pendu(self, ctx: commands.Context):
        self.tentative = 11
        self.pendu_word = str(
            dictionnary[random.randint(0, len(dictionnary) - 1)]
        )
        self.words = str("_" * len(self.pendu_word))
        self.words = self.pendu_word[0] + self.words[1:]
        self.is_pendu = 1
        for i in range(len(self.pendu_word)):
            if self.words[0] == self.pendu_word[i]:
                self.words = self.replace_char(
                    self.words, self.pendu_word[i], i
                )
        await ctx.channel.send("Pendu start")

    @commands.Cog.listener("on_message")
    async def wait_message_pendu(self, message: Message):
        if message.author.id == 991271491809316865:
            return
        if self.is_pendu != -1:
            is_win = 0
            is_correct = 0
            for i in range(len(self.pendu_word)):
                if message.content.lower() == self.pendu_word[i].lower():
                    self.words = self.replace_char(
                        self.words, self.pendu_word[i], i
                    )
                    is_correct = 1
                if self.words[i] == "_":
                    is_win = 1
            if is_correct == 0:
                self.tentative -= 1
            await message.channel.send(
                f"`{self.words}      tentative restantes : {self.tentative} !`"
            )
            if is_win == 0:
                await message.channel.send(
                    f"`Bien jouer le mot était bien : {self.words}` "
                )
                self.tentative = 11
                self.is_pendu = -1
            if self.tentative <= 0:
                await message.channel.send(
                    f"`Perdu, le mot était : {self.pendu_word} !`"
                )
                self.tentative = 11
                self.is_pendu = -1


async def setup(bot: commands.Bot):
    await bot.add_cog(Pendu(bot))
    print(f"cog loaded: {__file__}")


async def teardown(bot: commands.Bot):
    print(f"cog unloaded: {bot}{__file__}")
