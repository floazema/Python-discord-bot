from Pieces.pawn import Piece


class Knight(Piece):
    def __init__(self, isWhite: bool, x: int, y: int):
        super().__init__(isWhite, x, y)
        self.icon = ":regional_indicator_n:"

    def move(self, x: int, y: int, all_piece: list):
        x -= self.pos.x
        y -= self.pos.y
        if abs(x) == 2 and abs(y) == 1 or abs(x) == 1 and abs(y) == 2:
            self.pos.x += x
            self.pos.y += y
            return True
        return False
