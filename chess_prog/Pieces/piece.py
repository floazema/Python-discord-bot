class Position:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def same_pos(self, second_position: "Position") -> bool:
        if self.x == second_position.x and self.y == second_position.y:
            return True
        else:
            return False

    def display(self):
        print(chr(self.x + 96) + str(9 - self.y))

    def is_empty(self, all_pieces: list["Piece"]):
        for i in all_pieces:
            if self.same_pos(i.pos):
                return False
        return True


class Piece:
    def __init__(self, isWhite: bool, x: int, y: int):
        self.white = isWhite
        self.pos = Position(x, y)

    def move(self, x: int, y: int, all_piece: list["Piece"]) -> bool:
        raise NotImplementedError("not impl")

    def eat(self, x: int, y: int, all_piece: list["Piece"]):
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
