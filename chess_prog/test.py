from Pieces.bishop import Bishop
from Pieces.king import King
from Pieces.knight import Knight
from Pieces.pawn import Pawn
from Pieces.piece import Position
from Pieces.tower import Tower


def create_board():
    all_pieces = []
    for i in range(8):
        all_pieces.append(Pawn(True, i + 1, 7))
        all_pieces.append(Pawn(False, i + 1, 2))
    all_pieces.append(Tower(True, 1, 8))
    all_pieces.append(Tower(True, 8, 8))
    all_pieces.append(Tower(False, 8, 1))
    all_pieces.append(Tower(False, 1, 1))
    all_pieces.append(Bishop(True, 3, 8))
    all_pieces.append(Bishop(True, 6, 8))
    all_pieces.append(Bishop(False, 3, 1))
    all_pieces.append(Bishop(False, 6, 1))
    all_pieces.append(Knight(True, 2, 8))
    all_pieces.append(Knight(True, 7, 8))
    all_pieces.append(Knight(False, 2, 1))
    all_pieces.append(Knight(False, 7, 1))
    all_pieces.append(King(True, 5, 8))
    all_pieces.append(King(False, 5, 1))
    return all_pieces


def convert_algebric_in_pos(pos: str):
    return Position(ord(pos[0]) - 96, 9 - int(pos[1]))


def get_movement(cmd, all_piece, color):
    if cmd == "0-0":
        pass
    elif cmd == "0-0-0":
        pass
    else:
        if (
            len(cmd) != 5
            or sum(
                [
                    (i[0] in "abcdefgh" and i[1] in "12345678")
                    for i in cmd.split("-")
                ]
            )
            != 2
        ):
            return False
        if cmd[0:2] == cmd[3:5]:
            return False
        else:
            start_pos = convert_algebric_in_pos(cmd[0:2])
            arrival_pos = convert_algebric_in_pos(cmd[3:5])
            piece_to_move = None
            for i in all_piece:
                if i.pos.same_pos(start_pos) and i.white == color:
                    piece_to_move = i
            if not piece_to_move:
                return False
            for i in all_piece:
                if i.pos.same_pos(arrival_pos) and i.white != color:
                    return piece_to_move.eat(
                        arrival_pos.x, arrival_pos.y, all_piece
                    )
            print("p")
            return piece_to_move.move(arrival_pos.x, arrival_pos.y, all_piece)


a = create_board()
rd = True
while True:
    board = [[" " for _ in range(8)] for _ in range(8)]
    while True:
        if get_movement(input(), a, rd) is True:
            break
    for i in a:
        if i.white:
            board[i.pos.y - 1][i.pos.x - 1] = i.icon[-2]
        else:
            board[i.pos.y - 1][i.pos.x - 1] = i.icon[-2].upper()
    for i in board:
        print(i)
    a[0].pos.display()
    print(a[0].pos.y)
    rd = False if rd else True
