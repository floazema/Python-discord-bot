import os

from discord import File
from discord.ext import commands
from PIL import Image

help_message = """
```
+chess [option | mention] [mention]
Options:
    -help : Display this message
    -history : Display the history of the game (not implemented)
Mention:
    The user who will play the game with you
```
"""


class Chess:
    def __init__(self, players, ctx):
        self.players = players
        self.ctx = ctx
        self.blacks = [
            Image.open("assets/chess/16x16/BlackPieces_Simplified.png")
            .convert("RGBA")
            .crop((i * 16, 0, (i + 1) * 16, 16))
            for i in range(6)
        ]
        self.whites = [
            Image.open("assets/chess/16x16/WhitePieces_Simplified.png")
            .convert("RGBA")
            .crop((i * 16, 0, (i + 1) * 16, 16))
            for i in range(6)
        ]
        self.pieces = {
            "BlackPawn": self.blacks[0],
            "BlackKnight": self.blacks[1],
            "BlackTower": self.blacks[2],
            "BlackBishop": self.blacks[3],
            "BlackQueen": self.blacks[4],
            "BlackKing": self.blacks[5],
            "WhitePawn": self.whites[0],
            "WhiteKnight": self.whites[1],
            "WhiteTower": self.whites[2],
            "WhiteBishop": self.whites[3],
            "WhiteQueen": self.whites[4],
            "WhiteKing": self.whites[5],
            "": None,
        }
        self.pieceskeys = list(self.pieces.keys())
        self.board = self.generate_board()

    def generate_board(self):
        board = []
        for i in range(8):
            row = []
            for j in range(8):
                if (i + j) % 2 == 0:
                    row.append("")
                else:
                    row.append("")
            board.append(row)
        board[0] = [
            self.pieceskeys[2],
            self.pieceskeys[1],
            self.pieceskeys[3],
            self.pieceskeys[5],
            self.pieceskeys[4],
            self.pieceskeys[3],
            self.pieceskeys[1],
            self.pieceskeys[2],
        ]
        board[1] = [self.pieceskeys[0] for _ in range(8)]
        board[6] = [self.pieceskeys[6] for _ in range(8)]
        board[7] = [
            self.pieceskeys[8],
            self.pieceskeys[7],
            self.pieceskeys[9],
            self.pieceskeys[11],
            self.pieceskeys[10],
            self.pieceskeys[9],
            self.pieceskeys[7],
            self.pieceskeys[8],
        ]
        return board

    def print_board(self, board_img):
        board_img.paste(
            Image.open("assets/chess/boards/board_plain_04.png").convert(
                "RGBA"
            ),
            (0, 0),
        )
        for i, y in enumerate(self.board):
            for j, x in enumerate(y):
                if self.pieces[x] is not None:
                    board_img.paste(
                        self.pieces[x],
                        (j * 16 + 7, i * 16 + 7),
                        self.pieces[x],
                    )
        return board_img


class ChessGame(commands.Cog, name="ChessGame", description="Chess Game"):
    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()
        self.bot = bot

    #  ██████╗██╗  ██╗███████╗███████╗███████╗
    # ██╔════╝██║  ██║██╔════╝██╔════╝██╔════╝
    # ██║     ███████║█████╗  ███████╗███████╗
    # ██║     ██╔══██║██╔══╝  ╚════██║╚════██║
    # ╚██████╗██║  ██║███████╗███████║███████║
    #  ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝

    @commands.command()
    async def chess(self, ctx: commands.Context):
        f"""{help_message}"""
        help = False
        players = []
        try:
            opt = ctx.message.content.split(" ")[1]
            if opt == "-help" or opt == "-h":
                help = True
                await ctx.send(help_message)
                print("[CHESS] help message sent")
        except Exception:
            print("[CHESS] no option")
        try:
            players.append(ctx.author.id)
            players.append(ctx.message.mentions[0].id)
            print(players)
        except Exception:
            if not help:
                await ctx.send("Vous devez mentionner un autre joueur")
            return
        await ctx.send(
            "NEW GAME: <@"
            + str(players[0])
            + "> VS <@"
            + str(players[1])
            + ">"
        )
        board_img = Image.new("RGBA", (142, 142))
        board_img.paste(
            Image.open("assets/chess/boards/board_plain_04.png").convert(
                "RGBA"
            ),
            (0, 0),
        )
        chess_game = Chess(players, ctx)
        print(
            f"[CHESS] game created between [{players[0]} ",
            f"/ {ctx.author.name}] and [{players[1]} / ",
            f"{ctx.message.mentions[0].name}]",
        )
        chess_game.print_board(board_img).resize((284, 284)).save(
            f"assets/chess/{players[0]}_{players[1]}.png"
        )
        await ctx.send(
            file=File(
                open(f"assets/chess/{players[0]}_{players[1]}.png", "rb")
            )
        )
        os.remove(f"assets/chess/{players[0]}_{players[1]}.png")


async def setup(bot: commands.Bot):
    await bot.add_cog(ChessGame(bot))
    print(f"cog loaded: {__file__}")


async def teardown(bot: commands.Bot):
    print(f"cog unloaded: {bot}{__file__}")
