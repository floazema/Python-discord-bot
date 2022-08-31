import random

from discord import CategoryChannel, ForumChannel, Message, StageChannel
from discord.abc import PrivateChannel
from discord.ext import commands

from bot.dictionnary import dictionnary
from bot.emojis import Emojis

emoji = Emojis()

bannedClass = (ForumChannel, CategoryChannel, StageChannel, PrivateChannel)


class Motus(commands.Cog, name="MotusGame", description="Motus commands"):
    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()
        self.bot = bot
        self.motus_data = {
            "answer": "",
            "running": False,
            "history": [],
            "index": 0,
            "last_message": None,
        }

    def check_word_in_motus(self, word: str, answer: str):
        output = ""

        for i, letter in enumerate(word):
            if letter == answer[i]:
                output += emoji.square.green
            elif letter in answer:
                output += emoji.square.orange
            else:
                output += emoji.square.white
        return output

    def write_word_emojis(self, word: str):
        word_emojis = ""
        for letter in word:
            if letter in emoji.letters:
                word_emojis += emoji.letters[letter]
            else:
                word_emojis += emoji.square.black
        return word_emojis

    def display_history(self, history: list):
        history_emojis = ""
        answer = self.motus_data["answer"]
        for word in history:
            if word == "":
                history_emojis += (
                    "\n".join(
                        (
                            emoji.square.blue * len(answer),
                            emoji.square.black * len(answer),
                        )
                    )
                    + "\n"
                )
            else:
                history_emojis += (
                    "\n".join(
                        (
                            self.write_word_emojis(word),
                            self.check_word_in_motus(word, answer),
                        )
                    )
                    + "\n"
                )
        return history_emojis

    # ███╗   ███╗ ██████╗ ████████╗██╗   ██╗███████╗
    # ████╗ ████║██╔═══██╗╚══██╔══╝██║   ██║██╔════╝
    # ██╔████╔██║██║   ██║   ██║   ██║   ██║███████╗
    # ██║╚██╔╝██║██║   ██║   ██║   ██║   ██║╚════██║
    # ██║ ╚═╝ ██║╚██████╔╝   ██║   ╚██████╔╝███████║
    # ╚═╝     ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚══════╝
    @commands.command()
    async def motus(self, ctx: commands.Context):
        self.motus_data["history"] = ["" for _ in range(6)]
        self.motus_data["answer"] = (
            dictionnary[random.randint(0, len(dictionnary) - 1)]
        ).upper()
        print(f"MOTUS: {self.motus_data['answer']}")
        self.motus_data["running"] = True
        self.motus_data["index"] = 0
        sent = await ctx.send(self.display_history(self.motus_data["history"]))
        self.motus_data["last_message"] = [sent.id, sent.channel.id]

    @commands.Cog.listener("on_message")
    async def wait_message_motus(self, message: Message):
        if (
            self.motus_data["running"]
            and message.author.id != 991271491809316865
            and len(message.content) == len(self.motus_data["answer"])
            and message.content.lower() in dictionnary
        ):
            user_message = message.content.upper()
            self.motus_data["history"][self.motus_data["index"]] = user_message
            self.motus_data["index"] += 1
            channel = self.bot.get_channel(self.motus_data["last_message"][1])
            if not channel or isinstance(channel, bannedClass):
                return
            last_id = self.motus_data["last_message"][0]
            msg = await channel.fetch_message(last_id)
            sent = await message.channel.send(
                self.display_history(self.motus_data["history"])
            )
            self.motus_data["last_message"] = [sent.id, sent.channel.id]
            if user_message == self.motus_data["answer"]:
                self.motus_data["running"] = False
                await message.channel.send("Bravo !")
                return
            if self.motus_data["index"] == 6:
                answer = self.motus_data["answer"]
                await message.channel.send(f"Le mot était: {answer}")
                self.motus_data["running"] = False
                self.motus_data["answer"] = ""
                self.motus_data["history"] = ["" for _ in range(6)]
                self.motus_data["index"] = 0
                return
            await msg.delete()


async def setup(bot: commands.Bot):
    await bot.add_cog(Motus(bot))
    print(f"cog loaded: {__file__}")


async def teardown(bot: commands.Bot):
    print(f"cog unloaded: {bot}{__file__}")
