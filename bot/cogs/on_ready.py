from discord.ext import commands


class OnReady(
    commands.Cog, name="OnReady", description="Only react when ready"
):
    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()
        self.bot = bot

    @commands.Cog.listener("on_ready")
    async def on_ready(self):
        print(
            "o=============================================================o"
        )
        print(
            "|                         JE SUIS PRET                        |"
        )
        print(
            "o=============================================================o"
        )


async def setup(bot: commands.Bot):
    await bot.add_cog(OnReady(bot))
    print(f"cog loaded: {__file__}")


async def teardown(bot: commands.Bot):
    print(f"cog unloaded: {bot}{__file__}")
