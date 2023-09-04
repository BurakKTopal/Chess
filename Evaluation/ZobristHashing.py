import random
def zobrist_board(chessboard):
    list_of_cells = [('R', -5), ('N', -3), ('L', -3), ('Q', -9), ('K', -100),
                     ('R', 5), ('N', 3), ('L', 3), ('Q', 9), ('K', 100), ('P', 1), ('P', -1)]
    board = [[{} for _ in range(8)] for _ in range(8)]
    for i in range(8):
        for k in range(8):
            for piece in list_of_cells:
                board[i][k][piece] = random.randrange(int(10E10))
    en_passant = {}
    for col in ["a", "b", "c", "d", "e", "f", "g", "h"]:
        en_passant[col] = random.randrange(int(10E10))
    castle = {}
    for col in ["white_can_castle_short", "white_can_castle_long", "black_can_castle_short",
                "black_can_castle_long"]:
        castle[col] = random.randrange(int(10E10))
    return


def zobrist_hash(chessboard):
    h = 0
    for element in chessboard.cells_having_pieces_white:
        i, k = element
        h = h ^ chessboard.zobrist_board[i][k][chessboard.current_chess_board[i][k]]
    for element in chessboard.cells_having_pieces_black:
        i, k = element
        h = h ^ chessboard.zobrist_board[i][k][chessboard.current_chess_board[i][k]]
    if chessboard.white_can_castle_short:
        h = h ^ chessboard.zobrist_castle["white_can_castle_short"]
    if chessboard.white_can_castle_long:
        h = h ^ chessboard.zobrist_castle["white_can_castle_long"]
    if chessboard.black_can_castle_short:
        h = h ^ chessboard.zobrist_castle["black_can_castle_short"]
    if chessboard.black_can_castle_long:
        h = h ^ chessboard.zobrist_castle["black_can_castle_long"]
    if chessboard.en_passant_white:
        h = h ^ chessboard.zobrist_en_passant[chessboard.en_passant_move_white[0][-2]]
    if chessboard.en_passant_black:
        h = h ^ chessboard.zobrist_en_passant[chessboard.en_passant_move_black[0][-2]]
    return h
