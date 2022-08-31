letters = {
    "A": ":regional_indicator_a:",
    "B": ":regional_indicator_b:",
    "C": ":regional_indicator_c:",
    "D": ":regional_indicator_d:",
    "E": ":regional_indicator_e:",
    "F": ":regional_indicator_f:",
    "G": ":regional_indicator_g:",
    "H": ":regional_indicator_h:",
    "I": ":regional_indicator_i:",
    "J": ":regional_indicator_j:",
    "K": ":regional_indicator_k:",
    "L": ":regional_indicator_l:",
    "M": ":regional_indicator_m:",
    "N": ":regional_indicator_n:",
    "O": ":regional_indicator_o:",
    "P": ":regional_indicator_p:",
    "Q": ":regional_indicator_q:",
    "R": ":regional_indicator_r:",
    "S": ":regional_indicator_s:",
    "T": ":regional_indicator_t:",
    "U": ":regional_indicator_u:",
    "V": ":regional_indicator_v:",
    "W": ":regional_indicator_w:",
    "X": ":regional_indicator_x:",
    "Y": ":regional_indicator_y:",
    "Z": ":regional_indicator_z:",
}


class Squares:
    def __init__(self):
        self.orange = ":orange_square:"
        self.blue = ":blue_square:"
        self.green = ":green_square:"
        self.black = ":black_large_square:"
        self.red = ":red_square:"
        self.crossed_green = ":negative_squared_cross_mark:"


class Chess:
    def __init__(self):
        class Black:
            def __init__(self):
                self.pawn = "👦🏿"
                self.knight = "🐴"
                self.bishop = "👨🏿‍🎤"
                self.tower = "💂🏿‍♀️"
                self.queen = "👸🏿"
                self.king = "🤴🏿"
                self.empty = ":black_large_square:"

        class White:
            def __init__(self):
                self.pawn = "👦🏻"
                self.knight = "🦄"
                self.bishop = "👨🏻‍🎤"
                self.tower = "💂🏻‍♀️"
                self.queen = "👸🏻"
                self.king = "🤴🏻"
                self.empty = ":white_large_square:"

        self.black = Black()
        self.white = White()


# ███╗   ███╗███████╗███╗   ███╗ ██████╗      ██╗██╗
# ████╗ ████║██╔════╝████╗ ████║██╔═══██╗     ██║██║
# ██╔████╔██║█████╗  ██╔████╔██║██║   ██║     ██║██║
# ██║╚██╔╝██║██╔══╝  ██║╚██╔╝██║██║   ██║██   ██║██║
# ██║ ╚═╝ ██║███████╗██║ ╚═╝ ██║╚██████╔╝╚█████╔╝██║
# ╚═╝     ╚═╝╚══════╝╚═╝     ╚═╝ ╚═════╝  ╚════╝ ╚═╝
class Emojis:
    def __init__(self):
        self.square = Squares()
        self.letters = letters
        self.chess = Chess()


# 🤴🏻🤴🏿
# 👸🏻👸🏿
# 👦🏻👦🏿
# 💂🏻‍♀️💂🏿‍♀️
# 👨🏻‍🎤👨🏿‍🎤
# 🦄🐴
# ⬜️⬛️
