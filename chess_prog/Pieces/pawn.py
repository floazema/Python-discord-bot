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
            for i in all_piece:
                if i.pos.same_pos(Position(self.pos.x, self.pos.y + y)):
                    return False
            if y == -1:
                self.pos.y -= 1
            elif y == -2:
                for i in all_piece:
                    if i.pos.same_pos(Position(self.pos.x, self.pos.y - 1)):
                        return False
                self.pos.y -= 2
            else:
                return False
        else:
            for i in all_piece:
                if i.pos.same_pos(i, Position(self.pos.x, self.pos.y + y)):
                    return False
            if y == 1:
                self.pos.y += 1
            elif y == 2:
                for i in all_piece:
                    if i.pos.same_pos(Position(self.pos.x, self.pos.y + 1)):
                        return False
                self.pos.y += 2
            else:
                return False
        self.start_pos = False
        return True
