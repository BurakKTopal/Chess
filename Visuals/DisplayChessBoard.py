from chessboard import display
def display_chess_board(FEN):
    """
    Displayment function of the chess board
    :param FEN: Forsyth–Edwards Notation of current chess board
    :return: displays the chess board
    """
    # Displaying chess board
    if_move = True
    check = ''
    valid_fen = str(FEN)

    game_board = display.start()

    while if_move:
        display.update(valid_fen, game_board)
        if (check == ''):
            if_move = False
