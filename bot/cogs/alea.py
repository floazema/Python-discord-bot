import random

from discord import Message
from discord.ext import commands


class Alea(commands.Cog, name="Juste Prix", description="Juste Prix le jeux"):
    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()
        self.bot = bot
        self.juste_prix = -1

    #      ██╗██╗   ██╗███████╗████████╗███████╗    ██████╗ ██████╗ ██╗██╗  ██╗
    #      ██║██║   ██║██╔════╝╚══██╔══╝██╔════╝    ██╔══██╗██╔══██╗██║╚██╗██╔╝
    #      ██║██║   ██║███████╗   ██║   █████╗      ██████╔╝██████╔╝██║ ╚███╔╝
    # ██   ██║██║   ██║╚════██║   ██║   ██╔══╝      ██╔═══╝ ██╔══██╗██║ ██╔██╗
    # ╚█████╔╝╚██████╔╝███████║   ██║   ███████╗    ██║     ██║  ██║██║██╔╝ ██╗
    #  ╚════╝  ╚═════╝ ╚══════╝   ╚═╝   ╚══════╝    ╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝
    @commands.command()
    async def alea(self, ctx: commands.Context, stop=""):
        """Pick a random number between 0 and 1000,
        i will tell to the next message if they are close to it.
        if you specify any argument after this command, it will stop the alea
        """
        if stop != "":
            self.juste_prix = -1
        else:
            self.juste_prix = random.randint(0, 1000)
        await ctx.channel.send("Just Prix started")

    @commands.Cog.listener("on_message")
    async def wait_message_juste_prix(self, message: Message):
        if self.juste_prix != -1:
            if int(message.content) < self.juste_prix:
                await message.channel.send("plus haut")
            if int(message.content) > self.juste_prix:
                await message.channel.send("plus bas")
            if int(message.content) == self.juste_prix:
                await message.channel.send("c'est ça !")
                self.juste_prix = -1


async def setup(bot: commands.Bot):
    await bot.add_cog(Alea(bot))
    print(f"cog loaded: {__file__}")


async def teardown(bot: commands.Bot):
    print(f"cog unloaded: {bot}{__file__}")
