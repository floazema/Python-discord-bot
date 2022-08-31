from Pieces.piece import Piece, Position

class Tower(Piece):
    def __init__(self, is_white, x, y):
        super().__init__(is_white, x, y)
        self.start_pos = True
        self.icon = ":regional_indicator_r:"
    
    def move(self, x, y, all_pieces):
        if x < 1 or x > 8 or y < 1 or y > 8:
            return False
        elif x == self.pos.x and y == self.pos.y:
            return False
        elif x == self.pos.x and y != self.pos.y:
            for i in range(min(y, self.pos.y), max(y, self.pos.y)+1):
                for j in all_pieces:
                    if j.pos.same_pos(Position(x, i)) and not j.pos.same_pos(self.pos):
                        return False
            self.pos = Position(x, y)
        elif x != self.pos.x and y == self.pos.y:
            for i in range(min(x, self.pos.x), max(x, self.pos.x) + 1):
                for j in all_pieces:
                    if j.pos.same_pos(Position(i, y)) and not j.pos.same_pos(self.pos):
                        return False
            self.pos = Position(x, y)
        else:
            return False
        return True
