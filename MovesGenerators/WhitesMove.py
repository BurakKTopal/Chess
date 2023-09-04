from RulesImplementation.ChessRulesImplementation import *


def white_turn(move_white, chessboard):

    # Initializing legal move of person on 'false'
    chessboard.mate = False
    chessboard.stalemate = False
    legal_move = False
    legal_pawn_move = False

    if chessboard.en_passant_white:
        for element in chessboard.en_passant_move_white:
            coordinate_of_taken_piece = coordinate_transformation[element[-2:]]
            new_y = coordinate_of_taken_piece[0]
            new_x = coordinate_of_taken_piece[1]

            rank_to_column = dict(a=0, b=1, c=2, d=3, e=4, f=5, g=6, h=7)
            initial_x = rank_to_column[element[0]]
            chessboard.possible_moves_white.append([str(element), [3, initial_x, 1, "P", (new_y, new_x)]])

    # while move is illegal, we keep asking for a new move
    while not (legal_move):

        # introducing undo move
        if move_white == "undo":
            undo_black = True
            break
        else:
            # we only at this point re-initialize the en passant, as by the undo move, this could still happen again
            # re-initializing the en passant of black
            undo_black = False

        # We need to consider en passant if the person plays two steps with his pawn(thus a4, b4, ... or h4 in generic
        # notation)
        if move_white in ["a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4"]:

            # Searching for the move in the list of possible moves
            for elements in chessboard.possible_moves_white:

                # Searching for the move in the 'possible_list', because the elements of this list also contains the
                # position from WHERE the pieces CAN move. Thus giving a way to retrace the steps of the piece.
                if (elements[0] == move_white):
                    # Saving the list [x,y,z, 'str'], where x and y are the index in the of the PREVIOUS position of the
                    # piece on the chess board(x -> row, y-> column). z is the value of the piece and 'str' is
                    # the letter that is uniquely given to each piece.
                    previous_move = elements[1]
                    legal_pawn_move = True
                    legal_move = True
                    break
                else:
                    legal_pawn_move = False
            if not legal_pawn_move:
                print('illegal move, try something else')
                continue
            # if the previous move was on the 2nd row(not this is the 7th row of the matrix)
            # then there CAN be the possibility of en passant.
            if (previous_move[0] == 6):

                # chessboard.if_en_passant_white()
                # x-axis along horizontal line from white's perspective, y-axis vertically from a8 TO a1 and a8 cell
                # as origin
                x_coordinate_white_piece = coordinate_transformation[move_white][1]
                y_coordinate_white_piece = coordinate_transformation[move_white][0]

                # Invoking the coordinate_transformation function which serves to transform the generic chess notation
                # in the corresponding matrix indices. This coordinate transformation is used to make it possible to take
                # from left upper corner TO the right under corner BY black(seen from WHITE's perspective), as this is
                # not possible if the pawn would be on a4
                if not move_white == 'a4':

                    # 'chessboard.current_chess_board[4][x_coordinate_white_piece - 1][1]' is the value of the black piece
                    # at the left of the white pawn
                    if (chessboard.current_chess_board[4][x_coordinate_white_piece - 1] == ("P", -1)):
                        # If there is a black pawn at the LEFT side of white, then en passant could be played, ONLY
                        # if this doesn't result in the black king being in check

                        # Updating(hypothetically) if black WOULD take en passant te next move
                        chessboard.current_chess_board[4][ x_coordinate_white_piece - 1] = ('B', 0)

                        chessboard.current_chess_board[5][ x_coordinate_white_piece] = ('P', -1)

                        chessboard.current_chess_board[4][x_coordinate_white_piece] = ('B', 0)

                        # checking that the black king wouldn't be in check
                        chessboard.color = -1
                        if not chessboard.schaak():
                            # Writing en_passant_move in generic chess notation
                            chessboard.en_passant_move_black.append(str(
                                chess_board_letters[(4, x_coordinate_white_piece - 1)][0]) + 'x' \
                                                               + chess_board_letters[(y_coordinate_white_piece + 1,
                                                                                      x_coordinate_white_piece)])

                            # Setting en passant on True to give black a chance to take en passant on his NEXT move
                            chessboard.en_passant_black = True

                        # Undoing move
                        chessboard.current_chess_board[4][x_coordinate_white_piece - 1] = ('P', -1)

                        chessboard.current_chess_board[5][x_coordinate_white_piece] = ('B', 0)

                        chessboard.current_chess_board[6][x_coordinate_white_piece] = ('P', 1)

                        # setting back the color of the board on white, as we are still in white's turn
                        chessboard.color = 1

                # Case to do en passant from the right of the white pawn(from white's perspective)
                if not move_white == 'h4':
                    if (chessboard.current_chess_board[4][x_coordinate_white_piece + 1] == (
                    "P", -1)):  # checking if there is a black pawn to take en-passant.
                        # If there is a black pawn at the LEFT side of white, then en passant could be played, ONLY
                        # if this doesn't result in the black king being in check

                        # Updating(hypothetically) if black WOULD take en passant te next move
                        chessboard.current_chess_board[4][x_coordinate_white_piece + 1] = ('B', 0)

                        chessboard.current_chess_board[5][x_coordinate_white_piece] = ('P', -1)

                        chessboard.current_chess_board[4][x_coordinate_white_piece] = ('B', 0)

                        # checking that the black king wouldn't be in check
                        chessboard.color = -1
                        if not chessboard.schaak():
                            # Forming generic chess notation
                            chessboard.en_passant_move_black.append(str(
                                chess_board_letters[(4, x_coordinate_white_piece + 1)][0]) + 'x' \
                                                               + chess_board_letters[(y_coordinate_white_piece + 1,
                                                                                      x_coordinate_white_piece)])

                            # Setting en passant on True to give black a chance to take en passant on his NEXT move
                            chessboard.en_passant_black = True

                        # Undoing move
                        chessboard.current_chess_board[4][ x_coordinate_white_piece + 1] = ('P', -1)

                        chessboard.current_chess_board[5][x_coordinate_white_piece] = ('B', 0)

                        chessboard.current_chess_board[6][ x_coordinate_white_piece] = ('P', 1)

                        # putting back the color of the board on the right one
                        chessboard.color = 1

        # If white can play en passant and it plays it
        if (chessboard.en_passant_white and move_white in chessboard.en_passant_move_white):
            # Saving the coordinates of the move of white
            white_move_y_and_x_co = coordinate_transformation[move_white[2:]]
            white_move_y_co = white_move_y_and_x_co[0]
            white_move_x_co = white_move_y_and_x_co[1]

            # Saving the previous move: this is needed for undoing the move:
            chessboard.played_cell = ('en_passant_white', move_white)

            rank_to_column = dict(a=0, b=1, c=2, d=3, e=4, f=5, g=6, h=7)

            # for example, if we take with the white pawn on the f-file a black pawn on the g-file, then we'd
            # write fxg6, thus move_white[0] = f, this converts to the first column, so we'd find the coordinate of
            # the black pawn: [3, 5]
            chessboard.played_cell_position = (3, rank_to_column[move_white[0]])

            # saving the position of the cell that has been taken, together with the piece taken
            chessboard.taken_cell = chessboard.current_chess_board[white_move_y_co + 1][white_move_x_co]

            # black pawn is behind the white pawn, once the en passant move is played
            chessboard.taken_cell_position = (white_move_y_co + 1, white_move_x_co)

            chessboard.cells_having_pieces_white.remove((3, rank_to_column[move_white[0]]))
            #removing the piece in blacks list of cells having pieces
            chessboard.cells_having_pieces_black -= {(white_move_y_co + 1, white_move_x_co)}
            chessboard.cells_having_pieces_white.update({(white_move_y_co, white_move_x_co)})
            chessboard.en_passant_white = False
            chessboard.en_passant_move_white = []


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

            # Removing the black pawn, by setting its cell to an empty one, because the white pawn goes one AFTER the black pawn
            # we need to add a step so that it considers the black pawn BEHIND the white pawn, once the move is played.
            chessboard.current_chess_board[white_move_y_co + 1][white_move_x_co] = ("B", 0)

            # Turning the cell on which the white pawn was previously on a blank one
            chessboard.current_chess_board[3][rank_to_column[move_white[0]]] = ("B", 0)

            # Setting the white pawn on the right cell on the board
            chessboard.current_chess_board[white_move_y_co][white_move_x_co] = ("P", 1)
            legal_move = True
            chessboard.en_passant_white = True

        # Adding an else because if en passant isn't played, then we still need to play the move at another stage
        # as this move is conditioned on the en passant, is must be set on false
        else:
            chessboard.en_passant_white = False
            chessboard.en_passant_move_white = []

        if not legal_move:
            # Checking if given move is in list of possible moves of white
            for elements in chessboard.possible_moves_white:
                if (elements[0] == move_white):
                    # Saving the previous move in the form earlier states: [x,y,z, 'str']
                    previous_move = elements[1]
                    #print('number of possible moves for white:', len(chessboard.possible_moves_white))

                    # Move is legal, thus we get out of the while loop
                    legal_move = True
                    chessboard.en_passant_white = False
                    chessboard.en_passant_move_white = []
                    break
            else:
                print('move WHITE', move_white)
                # cell = random.choice(chessboard.possible_moves_white)
                # move_white = cell[0]
                # previous_move = cell[1]
                print(chessboard.possible_moves_white)
                print(chessboard.current_chess_board)
                # If not legal move, the player is warned and can give in another move
                print("illegal move, please choose another move.")

    # Setting the chess board accordingly once validated that played move is legit

    if not undo_black:

        # Short castling
        if (move_white == "O-O"):
            chessboard.white_can_castle_short = False
            chessboard.white_can_castle_short = False
            # Saving the previous move: this is needed for undoing the move:
            # for castling, 4 squares need to be reset, so we need to have different code for this
            chessboard.played_cell = ["O-O_white", 100]
            chessboard.played_cell_position = (7, 4)

            # saving the position of the cell that has been taken, together with the piece taken
            chessboard.taken_cell = ("R", 5)
            chessboard.taken_cell_position = (7, 7)

            chessboard.cells_having_pieces_white -= {(7, 4), (7,7)}
            chessboard.cells_having_pieces_white.update({(7,6), (7,5)})
            # adding move to list of played moves
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
            chessboard.current_chess_board[7][4] = ("B", 0)
            chessboard.current_chess_board[7][6] = ("K", 100)

            chessboard.current_chess_board[7][7] = ("B", 0)
            chessboard.current_chess_board[7][5] = ("R", 5)
            white_king_position = (7,6)
            chessboard.white_king_position = white_king_position

        # Long castling
        elif (move_white == "O-O-O"):
            # castling is not possible after once castled
            chessboard.white_can_castle_long = False
            chessboard.white_can_castle_short = False
            # Saving the previous move: this is needed for undoing the move:
            chessboard.played_cell = ("O-O-O_white", 100)
            chessboard.played_cell_position = (7, 4)

            # saving the position of the cell that has been taken, together with the piece taken
            chessboard.taken_cell = ("R", 5)
            chessboard.taken_cell_position = (7, 0)


            chessboard.cells_having_pieces_white -= {(7, 4), (7, 0)}
            chessboard.cells_having_pieces_white.update({(7,2), (7,3)})


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

            chessboard.current_chess_board[7][4] = ("B", 0)
            chessboard.current_chess_board[7][2] = ("K", 100)

            chessboard.current_chess_board[7][0] = ("B", 0)
            chessboard.current_chess_board[7][3] = ("R", 5)

            white_king_position = (7,2)
            chessboard.white_king_position = white_king_position

        # promotion
        elif move_white[-2] == "=":
            chessboard.promotion_white(previous_move, move_white[-1], move_white[-4:-2])

        # applying move, the last two characters of the notation always says where the piece is going to!
        elif not chessboard.en_passant_white:
            chessboard.apply_move_white(move_white[-2:], previous_move)

        # setting the en passant back on False, as it would be already played until this point
        chessboard.en_passant_white = False
        chessboard.en_passant_move_white = []

        # Displaying chess board using Forsyth–Edwards Notation(FEN),
        # see https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation
        #display_chess_board(making_fen(chessboard.current_chess_board))

        # Board's color must be switched to -1, as we are going to check if black is being checkmated
        chessboard.color = -1
        chessboard.possible_moves()
        # If black has no moves AND is in check, then the game ends, white wins, there can still be the case that
        # only an en passant could save the game
        if (chessboard.possible_moves_black == []):
            if chessboard.schaak():
                chessboard.mate = True
            else:
                chessboard.stalemate = True

    # if black there was an undo, then we set the position back
    else:
        chessboard.unmove()

        # chessboard.played_moves contains the elements of following structure: [played_cell, played_cell_position,
        #                                                                        taken_cell, taken_cell_position]

        if len(chessboard.played_moves) > 1:
            # deleting the last move:
            chessboard.played_moves.pop(-1)

        # taking the move that was played before that one
        previous_move = chessboard.played_moves[-1]

        # saving the played cells

        chessboard.played_cell = previous_move['played_cell']
        chessboard.played_cell_position = previous_move['played_cell_position']
        chessboard.taken_cell = previous_move['taken_cell']
        chessboard.taken_cell_position = previous_move['taken_cell_position']

        previous_move_en_passant = previous_move['en_passant']

        chessboard.en_passant_white = previous_move_en_passant['en_passant_white']
        chessboard.en_passant_black = previous_move_en_passant['en_passant_black']

        if chessboard.en_passant_white:
            chessboard.en_passant_move_white = previous_move_en_passant['en_passant_move_white']
        elif chessboard.en_passant_black:
            chessboard.en_passant_move_black = previous_move_en_passant['en_passant_move_black']

        # incorporating the castling:
        previous_move_castling = previous_move['castling']

        chessboard.white_can_castle_short = previous_move_castling['white_can_castle_short']
        chessboard.white_can_castle_long = previous_move_castling['white_can_castle_long']
        chessboard.black_can_castle_short = previous_move_castling['black_can_castle_short']
        chessboard.black_can_castle_long = previous_move_castling['black_can_castle_long']

        cells_having_pieces = previous_move['cells_having_pieces']
        chessboard.cells_having_pieces_black = cells_having_pieces['cells_having_pieces_black']
        chessboard.cells_having_pieces_white = cells_having_pieces['cells_having_pieces_white']


        #display_chess_board(making_fen(chessboard.current_chess_board))
        # Board's color must be switched to -1, as we are going to check if black is being checkmated
        chessboard.color = -1

        chessboard.possible_moves()
    return