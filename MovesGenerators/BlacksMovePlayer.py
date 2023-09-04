from RulesImplementation.ChessRulesImplementation import *


def black_move_player(initial_move, new_move, chessboard, piece_to_promote = False):
    legal_move = False  # looking if the played move is a possible move
    legal_pawn_move = False
    chessboard.mate = False
    chessboard.stalemate = False
    # we add the possibility of en passant if possible:
    if chessboard.en_passant_black:
        for element in chessboard.en_passant_move_black:
            coordinate_of_taken_piece = coordinate_transformation[element[-2:]]
            new_y = coordinate_of_taken_piece[0]
            new_x = coordinate_of_taken_piece[1]

            rank_to_column = dict(a=0, b=1, c=2, d=3, e=4, f=5, g=6, h=7)
            initial_x = rank_to_column[element[0]]
            chessboard.possible_moves_black.append([str(element), [4, initial_x, -1, "P", (new_y, new_x)]])

    while not legal_move:
        # Searching the move in the list of all possible moves of black
        for element in chessboard.possible_moves_black:

            if (element[1][0] == initial_move[0] and element[1][1] == initial_move[1] and element[1][4] == new_move):
                if piece_to_promote:
                    if element[0][-1] == piece_to_promote:
                        move_black = element[0]
                        previous_move = element[1]
                        legal_pawn_move = True
                        legal_move = True
                        break
                else:
                    move_black = element[0]
                    previous_move = element[1]
                    legal_pawn_move = True
                    legal_move = True
                    break
            else:
                # if there is no pawn to play, f.e. a4, then the following statements shouldn't be checked
                legal_pawn_move = False
        if not legal_pawn_move:
            print('illegal move, try something else')
            return False

        # if black pawn goes on the 5th rank, there CAN be en passant(of course if two steps by pawn were played)
        if move_black in ["a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5"]:

            # If pawn comes form 7th rank(thus 2 second row of matrix)
            if (previous_move[0] == 1):
                black_move_y_and_x_co = coordinate_transformation[move_black]
                move_black_x_co = black_move_y_and_x_co[1]
                move_black_y_co = black_move_y_and_x_co[0]
                # Considering the en passant BY white From the left side of the black pawn to right under the black pawn
                if not move_black == 'a5':

                    # Checking if there is a white pawn at the white side of the black pawn(seen from PERSPECTIVE OF WHITE°
                    # 'chessboard.current_chess_board[3][move_black_x_co - 1][1]' indicates the COLOR of the piece left of the
                    # black pawn. This must be STRICTLY bigger than zero, as it must be a white piece
                    if (chessboard.current_chess_board[3][ move_black_x_co - 1] == ("P", 1)):

                        # We are still need to check if the position results in the white king being in check;
                        # if this is the case, then the white move is illegal

                        chessboard.current_chess_board[3][move_black_x_co - 1] = ('B', 0)

                        chessboard.current_chess_board[3][move_black_x_co] = ('B', 0)

                        chessboard.current_chess_board[2][move_black_x_co] = ('P', 1)

                        # setting the color of the board back on white, as we are going to check whether the WHITE king
                        # is now in check
                        chessboard.color = 1
                        if not chessboard.schaak():
                            # Generating generic chess notation
                            chessboard.en_passant_move_white.append(str(
                                chess_board_letters[(3, move_black_x_co - 1)][0]) + 'x' \
                                                               + chess_board_letters[(move_black_y_co - 1,
                                                                                      move_black_x_co)])

                            # Giving the possibility for white to play en passant on the next move
                            chessboard.en_passant_white = True

                        # Undoing move
                        chessboard.current_chess_board[3][move_black_x_co - 1] = ('P', 1)

                        chessboard.current_chess_board[1][move_black_x_co] = ('P', -1)

                        chessboard.current_chess_board[2][move_black_x_co] = ('B', 0)

                        # putting back the color of the board on the right one
                        chessboard.color = -1

                # En passent from the right of the black pawn(from WHITE's perspective)
                if not move_black == 'h5':

                    # checking if there is a black pawn to take en-passant by a WHITE pawn on the RIGHT
                    if (chessboard.current_chess_board[3][move_black_x_co + 1] == ("P", 1)):

                        # We are still need to check if the position results in the white king being in check;
                        # if this is the case, then the white move is illegal

                        chessboard.current_chess_board[3][move_black_x_co + 1] = ('B', 0)

                        chessboard.current_chess_board[3][move_black_x_co] = ('B', 0)

                        chessboard.current_chess_board[2][move_black_x_co] = ('P', 1)

                        # setting the color of the board back on white, as we are going to check whether the WHITE king
                        # is now in check
                        chessboard.color = 1
                        if not chessboard.schaak():
                            # Generating generic chess notation
                            chessboard.en_passant_move_white.append(str(
                                chess_board_letters[(3, move_black_x_co + 1)][0]) + 'x' \
                                                               + chess_board_letters[(move_black_y_co - 1,
                                                                                      move_black_x_co)])

                            # Giving white the possibility to play en passant on next move
                            chessboard.en_passant_white = True

                        # undoing move

                        chessboard.current_chess_board[3][move_black_x_co + 1] = ('P', 1)

                        chessboard.current_chess_board[1][move_black_x_co] = ('P', -1)

                        chessboard.current_chess_board[2][move_black_x_co] = ('B', 0)

                        # putting back the color of the board on the right one
                        chessboard.color = -1

        # checking if en passant is even legal to play
        if (chessboard.en_passant_black and move_black in chessboard.en_passant_move_black):
            black_move_y_and_x_co = coordinate_transformation[move_black[2:]]
            black_move_y_co = black_move_y_and_x_co[0]
            black_move_x_co = black_move_y_and_x_co[1]

            # we need to convert the letters to the corresponding column in the matrix:
            rank_to_column = dict(a=0, b=1, c=2, d=3, e=4, f=5, g=6, h=7)
            # Saving the previous move: this is needed for undoing the move:
            # we need to save the en passant move too, this is done in the second entry of played_cell
            chessboard.played_cell = ('en_passant_black', move_black)

            # for example, if we take with the black pawn on the a-file a white pawn on the b-file, then we'd
            # write axb3, thus move_black[0] = a, this converts to the first column, so we've find the coordinate of
            # the black pawn: [4, 0]
            chessboard.played_cell_position = (4, rank_to_column[move_black[0]])

            # saving the position of the cell that has been taken, together with the piece taken
            chessboard.taken_cell = chessboard.current_chess_board[black_move_y_co][black_move_x_co]

            # black pawn is behind the white pawn, once the en passant move is played
            chessboard.taken_cell_position = (black_move_y_co - 1, black_move_x_co)

            chessboard.cells_having_pieces_black.remove((4, rank_to_column[move_black[0]]))

            chessboard.cells_having_pieces_white -= {(black_move_y_co - 1, black_move_x_co)}

            chessboard.cells_having_pieces_black.update({(black_move_y_co, black_move_x_co)})
            chessboard.en_passant_black = False
            chessboard.en_passant_move_black = []
            # saving move to list of played moves
            chessboard.played_moves.append(
                {'played_cell': chessboard.played_cell, 'played_cell_position': chessboard.played_cell_position,
                 'taken_cell': chessboard.taken_cell, 'taken_cell_position': chessboard.taken_cell_position,
                 'castling': {'white_can_castle_short': chessboard.white_can_castle_short,
                              'white_can_castle_long': chessboard.white_can_castle_long,
                              'black_can_castle_short': chessboard.black_can_castle_short,
                              'black_can_castle_long': chessboard.black_can_castle_long},
                 'en_passant': {'en_passant_white': chessboard.en_passant_white,
                                'en_passant_black': chessboard.en_passant_black,
                                'en_passant_move_white': chessboard.en_passant_move_white,
                                'en_passant_move_black': chessboard.en_passant_move_black},
                 'cells_having_pieces': {
                     'cells_having_pieces_white': chessboard.cells_having_pieces_white,
                     'cells_having_pieces_black': chessboard.cells_having_pieces_black}
                 }
            )


            # Taking the white pawn, which would be located BEHIND the NEW position of the black pawn. Since the origin
            # is located at a8, we need to decrement with one value the y-value
            chessboard.current_chess_board[black_move_y_co - 1][ black_move_x_co] = ("B", 0)

            # Emptying the cell on which the black pawn WAS
            chessboard.current_chess_board[4][rank_to_column[move_black[0]]] = ("B", 0)

            # Setting the pawn on his new cell
            chessboard.current_chess_board[black_move_y_co][black_move_x_co] = ("P", -1)
            legal_move = True
            chessboard.en_passant_black = True

        else:
            chessboard.en_passant_black = False
            chessboard.en_passant_move_black = []

        if not legal_move:
            # Checking if given move is in list of possible moves of black
            for elements in chessboard.possible_moves_black:
                if (elements[1][0] == initial_move[0] and elements[1][1] == initial_move[1] and elements[1][3] == new_move):

                    move_black = elements[0]
                    # Saving the previous move in the form earlier states: [x,y,z, 'str']
                    previous_move = elements[1]

                    # Move is legal, thus we get out of the while loop
                    legal_move = True

                    # setting the en passant back on False, as it would be already played until this point
                    chessboard.en_passant_black = False
                    chessboard.en_passant_move_black = []
                    break

            else:
                print('move BLACK', move_black)
                # cell = random.choice(total_moves_black)
                # move_black = cell[0]
                # previous_move = cell[1]
                print(chessboard.possible_moves_black)
                print(chessboard.current_chess_board)
                # If not legal move, the player is warned and can give in another move
                print("illegal move, please choose another move.")

    # Short castle
    if (move_black == "O-O"):

        # no castling is done after once castled
        chessboard.black_can_castle_short = False
        chessboard.black_can_castle_long = False

        # Saving the previous move: this is needed for undoing the move:
        # for castling, 4 squares need to be reset, so we need to have different code for this
        chessboard.played_cell = ("O-O_black", -100)
        chessboard.played_cell_position = (0, 4)

        # saving the position of the cell that has been taken, together with the piece taken
        chessboard.taken_cell = ("R", -5)
        chessboard.taken_cell_position = (0, 7)

        chessboard.cells_having_pieces_black -= {(0, 4), (0, 7)}
        chessboard.cells_having_pieces_black.update({(0,6), (0,5)})

        # saving move to list of played moves
        chessboard.played_moves.append(
            {'played_cell': chessboard.played_cell, 'played_cell_position': chessboard.played_cell_position,
             'taken_cell': chessboard.taken_cell, 'taken_cell_position': chessboard.taken_cell_position,
             'castling': {'white_can_castle_short': chessboard.white_can_castle_short,
                          'white_can_castle_long': chessboard.white_can_castle_long,
                          'black_can_castle_short': chessboard.black_can_castle_short,
                          'black_can_castle_long': chessboard.black_can_castle_long},
             'en_passant': {'en_passant_white': chessboard.en_passant_white,
                            'en_passant_black': chessboard.en_passant_black,
                            'en_passant_move_white': chessboard.en_passant_move_white,
                            'en_passant_move_black': chessboard.en_passant_move_black},
             'cells_having_pieces': {
                 'cells_having_pieces_white': chessboard.cells_having_pieces_white,
                 'cells_having_pieces_black': chessboard.cells_having_pieces_black}
             }
        )

        chessboard.current_chess_board[0][4] = ("B", 0)
        chessboard.current_chess_board[0][6] = ("K", -100)

        chessboard.current_chess_board[0][7] = ("B", 0)
        chessboard.current_chess_board[0][5] = ("R", -5)

        black_king_position = (0,6)
        chessboard.black_king_position = black_king_position


    # Long castle
    elif (move_black == "O-O-O"):

        # no castling is possible after once castled
        chessboard.black_can_castle_short = False
        chessboard.black_can_castle_long = False

        # Saving the previous move: this is needed for undoing the move:
        chessboard.played_cell = ("O-O-O_black", -100)
        chessboard.played_cell_position = (0, 4)

        # saving the position of the cell that has been taken, together with the piece taken
        chessboard.taken_cell = ("R", -5)
        chessboard.taken_cell_position = (0, 0)

        chessboard.cells_having_pieces_black -= {(0, 4), (0, 0)}
        chessboard.cells_having_pieces_black.update({(0, 2), (0, 3)})

        # saving move to list of played moves
        chessboard.played_moves.append(
            {'played_cell': chessboard.played_cell, 'played_cell_position': chessboard.played_cell_position,
             'taken_cell': chessboard.taken_cell, 'taken_cell_position': chessboard.taken_cell_position,
             'castling': {'white_can_castle_short': chessboard.white_can_castle_short,
                          'white_can_castle_long': chessboard.white_can_castle_long,
                          'black_can_castle_short': chessboard.black_can_castle_short,
                          'black_can_castle_long': chessboard.black_can_castle_long},
             'en_passant': {'en_passant_white': chessboard.en_passant_white,
                            'en_passant_black': chessboard.en_passant_black,
                            'en_passant_move_white': chessboard.en_passant_move_white,
                            'en_passant_move_black': chessboard.en_passant_move_black},
             'cells_having_pieces': {
                 'cells_having_pieces_white': chessboard.cells_having_pieces_white,
                 'cells_having_pieces_black': chessboard.cells_having_pieces_black}
             }
        )

        chessboard.current_chess_board[0][4] = ("B", 0)
        chessboard.current_chess_board[0][2] = ("K", -100)
        chessboard.current_chess_board[0][0] = ("B", 0)
        chessboard.current_chess_board[0][3] = ("R", -5)
        black_king_position = (0, 2)
        chessboard.black_king_position = black_king_position

    # promotion
    elif move_black[-2] == "=":
        chessboard.promotion_black(previous_move, move_black[-1], move_black[-4:-2])

    # applying move, the last two characters of the notation always says where the piece is going to!
    elif not chessboard.en_passant_black:
        chessboard.apply_move_black(move_black[-2:], previous_move)

    # setting the en passant back on False, as it would be already played until this point
    chessboard.en_passant_black = False
    chessboard.en_passant_move_black = []

    # It's going to be back white's turn, so we switch the color back to white
    chessboard.color = 1
    chessboard.possible_moves()
    # If after black's move, white doesn't have any moves anymore, than the game ends
    if (chessboard.possible_moves_white == [] and chessboard.schaak()):
        if chessboard.schaak():
            chessboard.mate = True
            return False
        else:
            chessboard.stalemate = True
            return False

    return True
