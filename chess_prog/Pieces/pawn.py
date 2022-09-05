from Pieces.piece import Piece, Position


class Pawn(Piece):
    def __init__(self, is_white: bool, x: int, y: int):
        super().__init__(is_white, x, y)
        self.start_pos = True
        self.icon = ":regional_indicator_p:"

    def move(self, x: int, y: int, all_piece: list) -> bool:
        y -= self.pos.y
        x -= self.pos.x
        if x:
            return False
        if self.white:
            if not Position(self.pos.x, self.pos.y + y).is_empty(all_piece):
                return False
            if y == -1:
                self.pos.y -= 1
            elif y == -2:
                if not Position(self.pos.x, self.pos.y - 1).is_empty(
                    all_piece
                ):
                    return False
                self.pos.y -= 2
            else:
                return False
        else:
            if not Position(self.pos.x, self.pos.y + y).is_empty(all_piece):
                return False
            if y == 1:
                self.pos.y += 1
            elif y == 2:
                if not Position(self.pos.x, self.pos.y + 1).is_empty(
                    all_piece
                ):
                    return False
                self.pos.y += 2
            else:
                return False
        self.start_pos = False
        return True

    def eat(self, x: int, y: int, all_piece: list):
        if (self.white and y - self.pos.y != -1) or (
            not self.white and y - self.pos.y != 1
        ):
            return False
        if x - self.pos.x == 1 or x - self.pos.x == -1:
            for i in all_piece:
                if i.pos.same_pos(Position(x, y)):
                    all_piece.remove(i)
                    self.pos = Position(x, y)
                    return True
            return False
