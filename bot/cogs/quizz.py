import random

from discord import Message
from discord.ext import commands

from bot import knowledge


class Quizz(commands.Cog, name="QuizzGame", description="Quizz Game"):
    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()
        self.bot = bot
        self.quiz = -1

    #  ██████╗ ██╗   ██╗██╗███████╗███████╗
    # ██╔═══██╗██║   ██║██║╚══███╔╝╚══███╔╝
    # ██║   ██║██║   ██║██║  ███╔╝   ███╔╝
    # ██║▄▄ ██║██║   ██║██║ ███╔╝   ███╔╝
    # ╚██████╔╝╚██████╔╝██║███████╗███████╗
    #  ╚══▀▀═╝  ╚═════╝ ╚═╝╚══════╝╚══════╝
    @commands.command()
    async def quizz(self, ctx: commands.Context):
        """Ask a knowledge question, and wait for response"""
        self.quiz = random.randint(0, len(knowledge.reponse) - 1)
        await ctx.send(knowledge.question[self.quiz])

    @commands.Cog.listener("on_message")
    async def wait_message_quizz(self, message: Message):
        if self.quiz != -1:
            if message.content.lower() in knowledge.reponse[self.quiz]:
                await message.channel.send(
                    f"{message.author.mention} Bravo tu as trouvé la réponse"
                )
                self.quiz = -1


async def setup(bot: commands.Bot):
    await bot.add_cog(Quizz(bot))
    print(f"cog loaded: {__file__}")


async def teardown(bot: commands.Bot):
    print(f"cog unloaded: {bot}{__file__}")
