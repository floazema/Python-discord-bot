from Pieces.pawn import Pawn
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
    return all_pieces

def move_the_good_piece(x, y, piece, all_piece, rd):
    if piece.upper() == "R":
        for i in all_piece:
            if (x == i.pos.x or y == i.pos.y) and i.icon[-2] == "r" and rd == i.white:
                return i.move(x, y, a)
    if piece.upper() == "":
        for i in all_piece:
            if (x == i.pos.x) and i.icon[-2] == "p" and rd == i.white:
                print(i.pos.x, i.pos.y)
                return i.move(x, y, a)
    return False

def transform_cmd_in_move(cmd, all_piece, rd):
    if len(cmd) == 2:
        if cmd[0] in "abcdefgh" and cmd[1] in "12345678":
            return move_the_good_piece(ord(cmd[0]) - 96, 9 - int(cmd[1]), "", all_piece, rd)
        else:
            return False

a=create_board()
rd = True
while True:
    board = [[" " for i in range(8)] for i in range(8)]
    while True:
        if transform_cmd_in_move(input(), a, rd) == True:
            break
    for i in a:
        if i.white:
            board[i.pos.y - 1][i.pos.x - 1] = i.icon[-2]
        else:
            board[i.pos.y - 1][i.pos.x - 1] = i.icon[-2].upper()
    for i in board:print(i)
    rd = False if rd else True
