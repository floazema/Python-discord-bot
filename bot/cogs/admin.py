from discord.ext import commands


class Admin(commands.Cog, name="Admin", description="Admin commands"):
    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()
        self.bot = bot

    @commands.command()
    @commands.has_role("BOT ADMIN")
    async def stop(self, ctx: commands.Context):
        """Stop the bot"""
        print(f"Stopping...\nStopped by {ctx.author.name} / {ctx.author.id}")
        await ctx.send(f"Stopping...\nStopped by {ctx.author.mention}")
        await self.bot.close()


async def setup(bot: commands.Bot):
    await bot.add_cog(Admin(bot))
    print(f"cog loaded: {__file__}")


async def teardown(bot: commands.Bot):
    print(f"cog unloaded: {bot}{__file__}")
