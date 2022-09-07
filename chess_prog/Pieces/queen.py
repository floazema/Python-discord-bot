from Pieces.piece import Piece, Position


class Queen(Piece):
    def __init__(self, isWhite, x, y):
        super().__init__(isWhite, x, y)
        self.icon = ":regional_indicator_q:"

    def move(self, x: int, y: int, all_piece: list):
        if x == self.pos.x or y == self.pos.y:
            temp_x = self.pos.x
            temp_y = self.pos.y
            if not (
                (x == self.pos.x and y != self.pos.y)
                or (x != self.pos.x and y == self.pos.y)
            ):
                return False
            while temp_x != x and temp_y != y:
                temp_x += 1 if temp_x != x else 0
                temp_y += 1 if temp_y != y else 0
                if temp_x == x and temp_y == y:
                    break
                if not Position(temp_x, temp_y).is_empty(all_piece):
                    return False
            self.pos = Position(x, y)
            return True
        else:
            temp_x = self.pos.x
            temp_y = self.pos.y
            if x == self.pos.x and y == self.pos.y:
                return False
            if abs(self.pos.x - x) != abs(self.pos.y - y):
                return False
            while not self.pos.same_pos(Position(temp_x, temp_y)):
                if Position(temp_x, temp_y).is_empty(all_piece):
                    return False
                temp_x += 1 if temp_x < x else -1
                temp_y += 1 if temp_y < y else -1
            self.pos.x = x
            self.pos.y = y
            return True
