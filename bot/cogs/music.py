import asyncio
import shlex
import subprocess  # nosec
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, List

import discord
import youtube_dl
from discord.ext import commands

ytdl_format_options = {
    "format": "bestaudio/best",
    "outtmpl": "%(extractor)s-%(id)s-%(title)s.%(ext)s",
    "restrictfilenames": True,
    "noplaylist": True,
    "nocheckcertificate": True,
    "ignoreerrors": False,
    "logtostderr": False,
    "quiet": True,
    "no_warnings": True,
    "default_search": "auto",
    "source_address": "0.0.0.0",  # nosec
}
youtube_dl.utils.bug_reports_message = lambda: ""
ffmpeg_options = {
    "before_options": " -reconnect 1 -reconnect_streamed 1 "
    "-reconnect_delay_max 5 -loglevel quiet",
    "options": "-vn -loglevel quiet",
}
ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get("title")
        self.url = data.get("url")

    @classmethod
    async def from_url(
        cls,
        url: str,
        *,
        loop: asyncio.AbstractEventLoop | None = None,
        stream=False,
        option: dict | None = None,
    ):
        loop = loop or asyncio.get_event_loop()
        option = option or {}
        data = await loop.run_in_executor(
            None, lambda: ytdl.extract_info(url, download=not stream)
        )
        if not data:
            raise RuntimeError("Could not find video")
        if data and "entries" in data:
            data = data["entries"][0]
        filename = data["url"] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **option), data=data)


class Song:
    def __init__(self) -> None:
        self.url = ""
        self.title = ""
        self.duration = ""
        self.thumbnail = ""

    @classmethod
    async def create(
        cls,
        url_or_search: str,
        num=0,
        *,
        loop: asyncio.AbstractEventLoop | None = None,
    ) -> "Song":
        self = Song()
        await self.info(url_or_search, num, loop=loop)
        return self

    async def info(
        self,
        url_or_search: str,
        num=0,
        *,
        loop: asyncio.AbstractEventLoop | None = None,
    ) -> "Song":
        def get_info():
            command = "youtube-dl -x --audio-format mp3"
            if url_or_search.startswith("http"):
                command += f" {url_or_search}"
            else:
                command += f" ytsearch{'' if num == 0 else num+1}:"
                command += f'"{url_or_search}"'
            command += " -e --get-thumbnail --get-duration -j --no-playlist"
            info = subprocess.run(  # nosec
                shlex.split(command),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
            ).stdout.split("\n")
            return info

        loop = loop or asyncio.get_event_loop()
        info = await loop.run_in_executor(ThreadPoolExecutor(), get_info)
        index_webpage_url = info[len(info) - 2].index("webpage_url")
        compteur_quote_mark = 0
        i = 0
        webpage_url = ""
        while compteur_quote_mark != 3:
            webpage_url += info[len(info) - 2][index_webpage_url + i]
            i += 1
            if webpage_url[-1] == '"':
                compteur_quote_mark += 1
        webpage_url = webpage_url.split()
        webpage_url = webpage_url[1].strip('"')
        self.title = info[len(info) - 5]
        self.thumbnail = info[len(info) - 4]
        self.duration = info[len(info) - 3]
        self.url = webpage_url
        return self

    @classmethod
    async def ytsearch(
        cls, query, *, loop: asyncio.AbstractEventLoop | None = None
    ) -> List[str]:
        def get_urls():
            command = [
                "youtube-dl",
                "-x",
                "--audio-format",
                "mp3",
                'ytsearch10:"' + query + '"',
                "-e",
                "--get-thumbnail",
                "--get-duration",
                "--no-playlist",
            ]
            return subprocess.run(  # nosec
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
            ).stdout

        loop = loop or asyncio.get_event_loop()
        urls = await loop.run_in_executor(ThreadPoolExecutor(), get_urls)
        r_list = []
        msg = ""
        info = []
        compteur = 0
        for i in urls:
            if i == "\n":
                info.append(msg)
                compteur += 1
                msg = ""
            else:
                msg += i
            if compteur == 3:
                r_list.append(info)
                info = []
                compteur = 0
        return r_list

    @classmethod
    async def yt_playlist_list_musique(
        cls, link, *, loop: asyncio.AbstractEventLoop | None = None
    ):
        def get_urls():
            command = ["youtube-dl", link, "-j"]
            l_info = subprocess.run(  # nosec
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
            ).stdout.split("\n")
            return l_info

        loop = loop or asyncio.get_event_loop()
        l_info = await loop.run_in_executor(ThreadPoolExecutor(), get_urls)
        list_link = []
        for info in l_info:
            if "webpage_url" in info:
                index_webpage_url = info.index("webpage_url")
                compteur_quote_mark = 0
                i = 0
                webpage_url = ""
                while compteur_quote_mark != 3:
                    webpage_url += info[index_webpage_url + i]
                    i += 1
                    if webpage_url[-1] == '"':
                        compteur_quote_mark += 1
                webpage_url = webpage_url.split()
                webpage_url = webpage_url[1].strip('"')
                list_link.append(webpage_url)
        print(list_link)
        return list_link

    @classmethod
    async def ytdownload(
        cls,
        query: str,
        num=0,
        *,
        loop: asyncio.AbstractEventLoop | None = None,
    ):
        def get_urls():
            command = "youtube-dl -x --audio-format mp3"
            if query.startswith("http"):
                command += f" {query}"
            else:
                command += f' ytsearch{num+1 if num != 0 else ""}:"{query}"'
            command += " --get-title --get-url --get-thumbnail --get-duration"
            command += " -j --no-playlist"
            info = subprocess.run(  # nosec
                shlex.split(command),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
            ).stdout.split("\n")
            index_webpage_url = info[len(info) - 2].index("webpage_url")
            compteur_quote_mark = 0
            i = 0
            webpage_url = ""
            while compteur_quote_mark != 3:
                webpage_url += info[len(info) - 2][index_webpage_url + i]
                i += 1
                if webpage_url[-1] == '"':
                    compteur_quote_mark += 1
            webpage_url = webpage_url.split()
            webpage_url = webpage_url[1].strip('"')
            # title , link, thumbnail, webpage_url
            return [
                info[len(info) - 5],
                info[len(info) - 4],
                info[len(info) - 3],
                webpage_url,
            ]

        loop = loop or asyncio.get_event_loop()
        r_list = await loop.run_in_executor(ThreadPoolExecutor(), get_urls)
        return r_list


class MusicClient:
    def __init__(self, message: discord.Message, bot: commands.Bot):
        if not message.guild:
            raise RuntimeError("Message not sent in server")
        self.voice_client = None
        self.guild_id = message.guild.id
        self.notif_channel = message.channel
        self.bot = bot
        self.playlist: List[Song] = []

    @classmethod
    async def create(cls, message: discord.Message, client) -> "MusicClient":
        if isinstance(message.author, discord.User):
            raise RuntimeError("Le message n'est pas envoyé dans un serveur")
        if not message.author.voice or not message.author.voice.channel:
            raise RuntimeError(
                "Le client n'est pas connecté à un salon vocal !"
            )
        self = MusicClient(message, client)
        self.voice_client = await message.author.voice.channel.connect()
        return self

    async def play(self, url: str) -> bool:
        if self.voice_client is None:
            return False
        try:
            player = await YTDLSource.from_url(
                url, loop=self.bot.loop, stream=True, option=ffmpeg_options
            )
            self.voice_client.play(player)
        except Exception as e:
            print(f"ERROR: {__file__}:{e}")
            return False
        return True

    async def add(self, url_or_search: str, num=0) -> None:
        info = await Song.create(url_or_search, num)
        self.playlist.append(info)

    async def disconnect(self) -> None:
        if self.voice_client is None:
            return
        await self.voice_client.disconnect()

    async def pause(self) -> None:
        if self.voice_client is None:
            return
        self.voice_client.pause()

    async def resume(self) -> None:
        if self.voice_client is None:
            return
        self.voice_client.resume()

    async def stop(self):
        if self.voice_client is None:
            return
        self.voice_client.stop()

    async def is_playing(self) -> bool:
        if self.voice_client is None:
            raise RuntimeError("No voice client")
        return self.voice_client.is_playing()

    async def is_paused(self) -> bool:
        if self.voice_client is None:
            raise RuntimeError("No voice client")
        return self.voice_client.is_paused()

    async def is_connected(self) -> bool:
        if self.voice_client is None:
            raise RuntimeError("No voice client")
        return self.voice_client.is_connected()


class Music(commands.Cog, name="Music", description="Music commands"):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.clients: Dict[str, MusicClient] = {}
        self.ctx1: commands.Context | None = None
        self.muse: Song | None = None
        self.compt_muse = 0

    async def get_client(self, message: discord.Message, client):
        if not message.guild:
            raise RuntimeError("Message not sent in server")
        if not str(message.guild.id) in self.clients:
            self.clients[str(message.guild.id)] = await MusicClient.create(
                message, client
            )
        return self.clients[str(message.guild.id)]

    @commands.command()
    async def play(self, ctx: commands.Context, *, url_or_search: str):
        """Play a music by keywords/link"""
        client = await self.get_client(ctx.message, self.bot)
        await client.add(url_or_search)
        if len(client.playlist) == 0:
            await ctx.send("The url/search found nothing")
            return
        await ctx.send(f"Added: `{client.playlist[-1].title}`")
        self.ctx1 = ctx
        self.compt_muse += 1
        if self.compt_muse == 1:
            await self.musique()

    @commands.command()
    async def now(self, ctx: commands.Context):
        """Show curently music played"""
        if self.muse is None:
            await ctx.send("No music")
            return
        emb = discord.Embed(
            title=f"{self.muse.title}",
            description=f"duration: {self.muse.duration}",
            color=0xD92626,
            url=f"{self.muse.url}",
        )
        emb.set_thumbnail(url=self.muse.thumbnail)
        await ctx.send(embed=emb)

    @commands.command()
    async def skip(self, ctx: commands.Context):
        """Pass to next music in playlist"""
        client = await self.get_client(ctx.message, self.bot)
        await client.stop()

    @commands.command()
    async def queue(self, ctx: commands.Context):
        """Show music in playlist"""
        client = await self.get_client(ctx.message, self.bot)
        alll = [] if self.muse is None else [self.muse]
        alll.extend(client.playlist)
        for i, song in enumerate(alll):
            emb = emb = discord.Embed(
                title=f"{i} : {song.title}",
                description=f"duration: {song.duration}",
                color=0xD92626,
                url=f"{song.url}",
            )
            emb.set_thumbnail(url=song.thumbnail)
            await ctx.send(embed=emb)
            await asyncio.sleep(1)

    @commands.command()
    async def stop_music(self, ctx: commands.Context):
        """Stop and leave the vocal"""
        client = await self.get_client(ctx.message, self.bot)
        if await client.is_playing():
            await client.pause()
        client.playlist.clear()
        await client.stop()

    async def musique(self):
        if self.ctx1 is None:
            return
        music_client = await self.get_client(self.ctx1.message, self.bot)
        while len(music_client.playlist) > 0:
            self.muse = music_client.playlist[0]
            del music_client.playlist[0]
            is_ok = await music_client.play(self.muse.url)

            if is_ok:
                embed = discord.Embed(
                    title=self.muse.title, url=self.muse.url, color=0xAB3636
                )
                embed.set_thumbnail(url=self.muse.thumbnail)
                embed.add_field(
                    name="Now Playing!", value=f"time: {self.muse.duration}"
                )
                await self.ctx1.send(embed=embed)
            else:
                await self.ctx1.send(
                    "une erreur s'est produite lors de "
                    f"la lecture de cette musique: {str(self.muse.url)}"
                )
            while (
                await music_client.is_playing()
                or await music_client.is_paused()
            ):
                await asyncio.sleep(2)
        self.compt_muse = 0
        self.muse = None
        await music_client.disconnect()


async def setup(bot: commands.Bot):
    await bot.add_cog(Music(bot))
    print(f"cog loaded: {__file__}")


async def teardown(bot: commands.Bot):
    print(f"cog unloaded: {bot}{__file__}")
