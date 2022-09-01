class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def same_pos(self, second_position) -> bool:
        if self.x == second_position.x and self.y == second_position.y:
            return True
        else:
            return False

    def display(self):
        print(chr(self.x + 96) + str(9 - self.y))


class Piece:
    def __init__(self, isWhite: bool, x: int, y: int):
        self.white = isWhite
        self.pos = Position(x, y)
