from Pieces.piece import Piece, Position


class Bishop(Piece):
    def __init__(self, isWhite: bool, x: int, y: int):
        super().__init__(isWhite, x, y)
        self.icon = ":regional_indicator_b:"

    def move(self, x: int, y: int, all_piece: list["Piece"]) -> bool:
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
