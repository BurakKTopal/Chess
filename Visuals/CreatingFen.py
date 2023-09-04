import numpy as np

def fen_in_subsection(FEN_in_one_subsection, initial_of_piece, color_piece):
    """
    :param FEN_in_one_subsection: FEN between two slashes(/)
    :param initial_of_piece: The initial of the piece, such as 'Q' for queen
    :param color_piece: Color of the piece
    :return: the updated FEN in one subsection(thus between two slashes)
    """
    if color_piece == 1:
        # Need to write in CAPITAL if white piece
        return FEN_in_one_subsection + initial_of_piece.upper()

    elif color_piece == -1:
        # Need to write NON-capital if black piece
        return FEN_in_one_subsection + initial_of_piece.lower()


def making_fen(current_chess_board):
    """
    A FEN is a way to encode the current chess board, more info: https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation
    :param current_chess_board:
    :return:
    """
    FEN = ""
    for row in range(0, 8):
        # number of blanks/(empty cells) between pieces per row
        total_blanks = 0

        # FEN notation for one row
        FEN_in_one_subsection = ''

        for col in range(0, 8):

            # Looking at which piece we have at hand
            initial_of_piece = current_chess_board[row][col][0]

            # If there is no piece(thus a blank space 'B')
            if (initial_of_piece == "B"):
                total_blanks += 1
                FEN_in_one_subsection = FEN_in_one_subsection

            else:

                # Looking if piece is black or white
                color_piece = np.sign(current_chess_board[row][col][1])

                # If blanks are different from zero, than we add it to the row.
                if (total_blanks != 0):
                    FEN_in_one_subsection = FEN_in_one_subsection + str(total_blanks)
                    total_blanks = 0

                # We used different initials for the bishop( 'B' for notation, but 'L' in the chessboard_matrix)
                if not initial_of_piece == "L":
                    FEN_in_one_subsection = fen_in_subsection(FEN_in_one_subsection, initial_of_piece, color_piece)

                # If we have the bishop at hand
                else:
                    FEN_in_one_subsection = fen_in_subsection(FEN_in_one_subsection, "B", color_piece)

        # We need to add the number of blank cells AFTER  the last piece in every row. This is done by counting how many
        # occupied cells(from the 8) there are in one row. Substracting this from 8 gives the number of empty cells
        # after the last piece(looking from left to right from WHITE's perspective)
        number_of_occupied_cells = 0
        for n in range(0, len(FEN_in_one_subsection)):

            if (FEN_in_one_subsection[n]) in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                number_of_occupied_cells = number_of_occupied_cells + int(FEN_in_one_subsection[n])
            else:
                number_of_occupied_cells += 1
        if (number_of_occupied_cells < 8):
            FEN_in_one_subsection = FEN_in_one_subsection + str(8 - number_of_occupied_cells)

        FEN = FEN + "/" + FEN_in_one_subsection
        # We still have the "/" as first element
    return FEN[1:]
