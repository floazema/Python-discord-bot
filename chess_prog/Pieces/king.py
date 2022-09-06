from Pieces.piece import Piece, Position


class King(Piece):
    def __init__(self, isWhite: bool, x: int, y: int):
        super().__init__(isWhite, x, y)
        self.icon = ":regional_indicator_k:"
    
    def move(self, x: int, y: int, all_piece: list):
        x -= self.pos.x
        y -= self.pos.y
        if abs(x) > 1 or abs(y) > 1 or x == y == 0:
            return False
        self.pos.x += x
        self.pos.y += y
        return True
    
    def eat(self, x: int, y: int, all_piece: list):
        temp = None
        for i in all_piece:
            if Position(x, y).same_pos(i.pos) and self.white != i.white:
                temp = i
        if not temp:
            return False
        if self.move(x, y, all_piece):
            all_piece.remove(temp)
            return True
        return False
