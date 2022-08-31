from Pieces.piece import Piece, Position

class Pawn(Piece):
    def __init__(self, is_white, x, y):
        super().__init__(is_white, x, y)
        self.start_pos = True
        self.icon = ":regional_indicator_p:"
    
    def move(self, x, y, all_piece):
        y -= self.pos.y
        x -= self.pos.x
        if self.white:
            if x:
                return False
            elif y == -1:
                for i in all_piece:
                    if i.pos.same_pos(Position(self.pos.x, self.pos.y + y)):
                        return False
                self.pos.y -= 1
            elif y == -2:
                for i in all_piece:
                    if i.pos.same_pos(Position(self.pos.x, self.pos.y + y)):
                        return False
                    if i.pos.same_pos(Position(self.pos.x, self.pos.y - 1)):
                        return False
                self.pos.y -= 2
            else:
                return False
        else:
            if x:
                return False
            elif y == 1:
                for i in all_piece:
                    if i.pos.same_pos(i, Position(self.pos.x, self.pos.y + y)):
                        return False
                self.pos.y += 1
            elif y == 2:
                for i in all_piece:
                    if i.pos.same_pos(Position(self.pos.x, self.pos.y + y)):
                        return False
                    if i.pos.same_pos(Position(self.pos.x, self.pos.y + 1)):
                        return False
                self.pos.y += 2
            else:
                return False
        self.start_pos = False
        return True
