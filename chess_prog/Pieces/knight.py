from Pieces.pawn import Piece, Position


class Knight(Piece):
    def __init__(self, isWhite, x, y):
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

    def eat(self, x: int, y: int, all_piece: list):
        for i in all_piece:
            if Position(x, y).same_pos(i.pos):
                temp = i
        if self.move(x, y, all_piece):
            all_piece.remove(temp)
            return True
        return False
