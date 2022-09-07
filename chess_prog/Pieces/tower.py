from Pieces.piece import Piece, Position


class Tower(Piece):
    def __init__(self, is_white: bool, x: int, y: int):
        super().__init__(is_white, x, y)
        self.start_pos = True
        self.icon = ":regional_indicator_r:"

    def move(self, x: int, y: int, all_pieces: list) -> bool:
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
            if not Position(temp_x, temp_y).is_empty(all_pieces):
                return False
        self.pos = Position(x, y)
        return True
