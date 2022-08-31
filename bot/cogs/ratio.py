from discord.ext import commands


class Fun(commands.Cog, name="Fun", description="Fun commands"):
    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()
        self.bot = bot

    # ██████╗  █████╗ ████████╗██╗ ██████╗
    # ██╔══██╗██╔══██╗╚══██╔══╝██║██╔═══██╗
    # ██████╔╝███████║   ██║   ██║██║   ██║
    # ██╔══██╗██╔══██║   ██║   ██║██║   ██║
    # ██║  ██║██║  ██║   ██║   ██║╚██████╔╝
    # ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝ ╚═════╝
    @commands.command()
    async def ratio(self, ctx: commands.Context):
        """Put R A T I O emoji to the message above"""
        if ctx.message is None:
            return
        await ctx.message.delete()
        async for last_msg in ctx.history(limit=1):
            for reaction in ["🇷", "🇦", "🇹", "🇮", "🇴"]:
                await last_msg.add_reaction(reaction)


async def setup(bot: commands.Bot):
    await bot.add_cog(Fun(bot))
    print(f"cog loaded: {__file__}")


async def teardown(bot: commands.Bot):
    print(f"cog unloaded: {bot}{__file__}")
