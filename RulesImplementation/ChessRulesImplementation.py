import numpy as np

"""
                                        CHESS made by Burak Kucuktopal
"""

"""
Defining the chess board
    LEGEND:
    R: rook, N: knight, L: bishop, Q: queen, K: king, B: blank space, P: pawn
    Point system used respectively(in absolute value):
    5,3,3,9,100, 0, 1"""
chess_board = [
    [('R', -5), ('N', -3), ('L', -3), ('Q', -9), ('K', -100), ('L', -3), ('N', -3), ('R', -5)],
    [('P', -1), ('P', -1), ('P', -1), ('P', -1), ('P', -1), ('P', -1), ('P', -1), ('P', -1)],
    [('B', 0), ('B', 0), ('B', 0), ('B', 0), ('B', 0), ('B', 0), ('B', 0), ('B', 0)],
    [('B', 0), ('B', 0), ('B', 0), ('B', 0), ('B', 0), ('B', 0), ('B', 0), ('B', 0)],
    [('B', 0), ('B', 0), ('B', 0), ('B', 0), ('B', 0), ('B', 0), ('B', 0), ('B', 0)],
    [('B', 0), ('B', 0), ('B', 0), ('B', 0), ('B', 0), ('B', 0), ('B', 0), ('B', 0)],
    [('P', 1), ('P', 1), ('P', 1), ('P', 1), ('P', 1), ('P', 1), ('P', 1), ('P', 1)],
    [('R', 5), ('N', 3), ('L', 3), ('Q', 9), ('K', 100), ('L', 3), ('N', 3), ('R', 5)]
]
coordinate_transformation = {
    "a8": (0, 0), "b8": (0, 1), "c8": (0, 2), "d8": (0, 3), "e8": (0, 4), "f8": (0, 5), "g8": (0, 6), "h8": (0, 7),
    "a7": (1, 0), "b7": (1, 1), "c7": (1, 2), "d7": (1, 3), "e7": (1, 4), "f7": (1, 5), "g7": (1, 6), "h7": (1, 7),
    "a6": (2, 0), "b6": (2, 1), "c6": (2, 2), "d6": (2, 3), "e6": (2, 4), "f6": (2, 5), "g6": (2, 6), "h6": (2, 7),
    "a5": (3, 0), "b5": (3, 1), "c5": (3, 2), "d5": (3, 3), "e5": (3, 4), "f5": (3, 5), "g5": (3, 6), "h5": (3, 7),
    "a4": (4, 0), "b4": (4, 1), "c4": (4, 2), "d4": (4, 3), "e4": (4, 4), "f4": (4, 5), "g4": (4, 6), "h4": (4, 7),
    "a3": (5, 0), "b3": (5, 1), "c3": (5, 2), "d3": (5, 3), "e3": (5, 4), "f3": (5, 5), "g3": (5, 6), "h3": (5, 7),
    "a2": (6, 0), "b2": (6, 1), "c2": (6, 2), "d2": (6, 3), "e2": (6, 4), "f2": (6, 5), "g2": (6, 6), "h2": (6, 7),
    "a1": (7, 0), "b1": (7, 1), "c1": (7, 2), "d1": (7, 3), "e1": (7, 4), "f1": (7, 5), "g1": (7, 6), "h1": (7, 7)
}

# Chess board in letters
chess_board_letters = {
    (0, 0): "a8", (0, 1): "b8", (0, 2): "c8", (0, 3): "d8",
    (0, 4): "e8", (0, 5): "f8", (0, 6): "g8", (0, 7): "h8",
    (1, 0): "a7", (1, 1): "b7", (1, 2): "c7", (1, 3): "d7",
    (1, 4): "e7", (1, 5): "f7", (1, 6): "g7", (1, 7): "h7",
    (2, 0): "a6", (2, 1): "b6", (2, 2): "c6", (2, 3): "d6",
    (2, 4): "e6", (2, 5): "f6", (2, 6): "g6", (2, 7): "h6",
    (3, 0): "a5", (3, 1): "b5", (3, 2): "c5", (3, 3): "d5",
    (3, 4): "e5", (3, 5): "f5", (3, 6): "g5", (3, 7): "h5",
    (4, 0): "a4", (4, 1): "b4", (4, 2): "c4", (4, 3): "d4",
    (4, 4): "e4", (4, 5): "f4", (4, 6): "g4", (4, 7): "h4",
    (5, 0): "a3", (5, 1): "b3", (5, 2): "c3", (5, 3): "d3",
    (5, 4): "e3", (5, 5): "f3", (5, 6): "g3", (5, 7): "h3",
    (6, 0): "a2", (6, 1): "b2", (6, 2): "c2", (6, 3): "d2",
    (6, 4): "e2", (6, 5): "f2", (6, 6): "g2", (6, 7): "h2",
    (7, 0): "a1", (7, 1): "b1", (7, 2): "c1", (7, 3): "d1", (7, 4): "e1", (7, 5): "f1", (7, 6): "g1", (7, 7): "h1"
}

white_king_position = "e1"

black_king_position = "e8"


class knight:
    """
    Bringing the horsey in the game
    """

    def __init__(self, initial_position, new_position, current_chess_board, color):
        self.initial_position = initial_position
        self.new_position = new_position
        self.color = color
        self.current_chess_board = current_chess_board

    def if_illegal_move(self):
        initial_y, initial_x = map(int, self.initial_position)
        new_y, new_x = map(int, (self.new_position[1], self.new_position[4]))

        if new_y < 0 or new_y > 7 or new_x < 0 or new_x > 7:
            return True

        cell_value = self.current_chess_board[new_y][new_x][1]

        if np.sign(cell_value) * self.color <= 0:
            y_diff = abs(initial_y - new_y)
            x_diff = abs(initial_x - new_x)

            if (y_diff == 2 and x_diff == 1) or (y_diff == 1 and x_diff == 2):
                return False
            else:
                return True
        else:
            return True


class board:
    def __init__(self, current_chess_board, color, black_king_position=(0, 4), white_king_position=(7, 4),
                 en_passant_white=False, en_passant_move_white=[],
                 en_passant_black=False, en_passant_move_black=[],
                 possible_moves_white=[], possible_moves_black=[],
                 white_can_castle_short=True, white_can_castle_long=True,
                 black_can_castle_short=True, black_can_castle_long=True, played_cell=[],
                 played_cell_position=[], taken_cell=[], taken_cell_position=[], played_moves=[],
                 cells_having_pieces_white={(6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7),
                                            (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7)},
                 cells_having_pieces_black={(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
                                            (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7)},
                 is_in_check=False, mate=False, stalemate=False, zobrist_board=[],
                 zobrist_en_passant={}, zobrist_castle={}, transposition_table={},
                 middlegame=True, endgame=False):

        self.current_chess_board = current_chess_board
        self.color = color
        self.cells_having_pieces_white = cells_having_pieces_white
        self.cells_having_pieces_black = cells_having_pieces_black

        # check, mate and stalemate
        self.is_in_check = is_in_check
        self.mate = mate
        self.stalemate = stalemate


        # middlegame and endgame
        self.middlegame = middlegame
        self.endgame = endgame

        # counting number of transpositions
        self.counting = 0

        # Zobrist hashing
        self.zobrist_board = zobrist_board
        self.zobrist_en_passant = zobrist_en_passant
        self.zobrist_castle = zobrist_castle
        self.transposition_table = transposition_table

        # variables for saving en passant
        self.en_passant_white = en_passant_white
        self.en_passant_black = en_passant_black

        self.en_passant_move_white = en_passant_move_white
        self.en_passant_move_black = en_passant_move_black

        # Saving position of the black and white king
        self.black_king_position = black_king_position
        self.white_king_position = white_king_position

        # saving possible positions:
        self.possible_moves_white = possible_moves_white
        self.possible_moves_black = possible_moves_black

        # saving if castling is still possible for white
        self.white_can_castle_short = white_can_castle_short
        self.white_can_castle_long = white_can_castle_long

        # saving if castling is still possible for black
        self.black_can_castle_short = black_can_castle_short
        self.black_can_castle_long = black_can_castle_long

        # saving the earlier position
        self.played_cell = played_cell
        self.played_cell_position = played_cell_position
        self.taken_cell = taken_cell
        self.taken_cell_position = taken_cell_position

        # list of played moves
        self.played_moves = played_moves

    def horizontal_check(self, cell_y, cell_x):
        """
        checking if king is horizontally being checked
        """
        if not (0 <= cell_y <= 7 and 0 <= cell_x <= 7):
            return -1
        if self.is_in_check or \
                (cell_y, cell_x) in self.cells_having_pieces_black or (
        cell_y, cell_x) in self.cells_having_pieces_white:
            cell_piece, cell_value = self.current_chess_board[cell_y][cell_x]
            if cell_piece in ("Q", "R") and np.sign(cell_value) != self.color:
                return 1  # King is attacked
            elif cell_piece == "B":
                return 0
            else:
                return -1
        else:
            return 0

    def vertical_checks(self, cell_y, cell_x):
        """
        checking if king is vertically being checked
        """
        if not (0 <= cell_y <= 7 and 0 <= cell_x <= 7):
            return -1
        if self.is_in_check or \
                (cell_y, cell_x) in self.cells_having_pieces_black or (
        cell_y, cell_x) in self.cells_having_pieces_white:
            cell_piece, cell_value = self.current_chess_board[cell_y][cell_x]
            if cell_piece in ("Q", "R") and np.sign(cell_value) != self.color:
                return 1  # King is attacked

            elif cell_piece == "B":
                return 0
            else:
                return -1  # Piece blocks the path but cannot attack the king

        else:
            return 0


    def diagonal_checks(self, cell_y, cell_x, king_y, king_x):
        """
        checking if king is diagonally being checked
        """
        if not (0 <= cell_y <= 7 and 0 <= cell_x <= 7):
            return -1
        if self.is_in_check or \
                (cell_y, cell_x) in self.cells_having_pieces_black or (
        cell_y, cell_x) in self.cells_having_pieces_white:
            cell = self.current_chess_board[cell_y][cell_x]
            cell_piece = cell[0]
            cell_value = cell[1]
            sign_of_cell = np.sign(cell_value)
            if sign_of_cell != self.color:
                if cell_piece in ("Q", "L"):
                    return 1  # King is attacked by queen of bishop

                elif cell == ("P", sign_of_cell):
                    dy = cell_y - king_y
                    dx = cell_x - king_x
                    if dy == sign_of_cell and (dx == 1 or dx == -1):
                        return 1 # King is attacked by pawn, accordingly to the color of the king
                    else:
                        return -1

                elif cell_piece == "B":
                    return 0

                else:
                    return -1

            elif cell_piece == "B":
                return 0
            else:
                return -1  # Blocked by same-colored piece but cannot attack the king
        else:
            return 0

    def diagonal_moves(self, initial_position, new_position, direction):
        """
        Checking if diagonal move is legal by looking if there are pieces between begin and end point
        """
        initial_y, initial_x = map(int, initial_position)
        new_y, new_x = map(int, (new_position[1], new_position[4]))
        piece_inbetween = 0

        for x in range(min(initial_x, new_x) + 1, max(initial_x, new_x)):
            y = direction * (x - initial_x) + initial_y
            if not (0 <= y <= 7 and 0 <= x <= 7):
                break
            if (y, x) in self.cells_having_pieces_black or (y, x) in self.cells_having_pieces_white:
                piece_inbetween += 1
                break

        return piece_inbetween

    def horizontal_and_vertical_moves(self, initial_position, new_position):
        """
        Checking if horizontal moves is legal by looking if there are pieces between begin and end point
        """
        initial_y, initial_x = map(int, initial_position)
        new_y, new_x = map(int, (new_position[1], new_position[4]))

        piece_inbetween = 0

        dy = new_y - initial_y
        dx = new_x - initial_x

        step_x = 1 if dx > 0 else -1
        step_y = 1 if dy > 0 else -1

        if dy == 0:
            for x in range(initial_x + step_x, new_x, step_x):
                if not (0 <= x <= 7):
                    break
                if (initial_y, x) in self.cells_having_pieces_black or (initial_y, x) in self.cells_having_pieces_white:
                    piece_inbetween += 1
                    break

        elif dx == 0:
            for y in range(initial_y + step_y, new_y, step_y):
                if not (0 <= y <= 7):
                    break
                if (y, initial_x) in self.cells_having_pieces_black or (y, initial_x) in self.cells_having_pieces_white:
                    piece_inbetween += 1
                    break

        return piece_inbetween

    def is_in_line_of_sight(self, initial_y, initial_x, new_y, new_x):
        """
        Only pieces which are horizontally, vertically or diagonally in the way of the king, are in line of sight.
        This is important, as only these pieces should be checked if they left the king in check once moved.
        Note that if the king IS already in check, that we cannot do this, as the king can be doubled checked.
        """
        king_y, king_x = (self.white_king_position if self.color == 1 else self.black_king_position)
        dy_initial = initial_y - king_y
        dx_initial = initial_x - king_x

        dy_new = new_y - king_y
        dx_new = new_x - king_x
        step_x = 1 if dx_initial > 0 else -1
        step_y = 1 if dy_initial > 0 else -1

        if self.is_in_check:
            return False
        elif dy_initial == 0:
            if dy_new == 0:
                return True
            else:
                for i in range(king_x + step_x, initial_x, step_x):
                    if (dy_initial, i) in self.cells_having_pieces_black or (
                    dy_initial, i) in self.cells_having_pieces_white:
                        return True
        elif dx_initial == 0:
            if dx_new == 0:
                return True
            else:
                for i in range(king_x + step_y, initial_x, step_y):
                    if (i, dx_initial) in self.cells_having_pieces_black or (
                    i, dx_initial) in self.cells_having_pieces_white:
                        return True

        elif dx_initial / dy_initial == -1:
            if dx_new == -dy_new:
                return True
            else:
                for x in range(king_x + step_x, initial_x, step_x):
                    y = -1 * (x - king_x) + king_y
                    if (y, x) in self.cells_having_pieces_black or (x, dx_initial) in self.cells_having_pieces_white:
                        return True

        elif dx_initial / dy_initial == 1:
            if dx_new == dy_new:
                return True
            else:
                for x in range(king_x + step_x, initial_x, step_x):
                    y = 1 * (x - king_x) + king_y
                    if (y, x) in self.cells_having_pieces_black or (x, dx_initial) in self.cells_having_pieces_white:
                        return True
        return False

    def looking_if_check(self, initial_position, new_position):
        """
        Looking if move is legal by checking if own king is put in check after hypothetical move is played.
        """

        initial_y, initial_x = map(int, initial_position)
        new_y, new_x = map(int, (new_position[1], new_position[4]))

        if self.is_in_line_of_sight(initial_y, initial_x, new_y, new_x):
            return False

        played_piece, played_piece_points = self.current_chess_board[initial_y][initial_x]
        taken_piece, taken_piece_points = self.current_chess_board[new_y][new_x]

        self.current_chess_board[new_y][new_x] = (played_piece, played_piece_points)
        self.current_chess_board[initial_y][initial_x] = ("B", 0)

        is_in_check = self.if_in_check()

        self.current_chess_board[new_y][new_x] = (taken_piece, taken_piece_points)
        self.current_chess_board[initial_y][initial_x] = (played_piece, played_piece_points)

        return is_in_check

    def possible_moves(self):
        """
        gives all the possible moves, by move ordering, we have put the piece takes which are preferable first, and then
        the 'non-taking' moves. At last, the moves which are not preferrable to play, but can still be tactictly preferable
        at further moves.
        """
        # Initializing the lists
        list_possible_moves_queen_takes = []
        list_possible_moves_queen = []

        list_possible_moves_rook = []
        list_possible_moves_rook_takes = []
        list_possible_moves_rook_takes_higher = []
        list_possible_moves_bishop = []
        list_possible_moves_bishop_takes = []
        list_possible_moves_bishop_takes_higher = []
        list_possible_moves_pawn = []
        list_possible_moves_pawn_takes = []
        list_possible_moves_pawn_takes_higher = []
        list_possible_moves_king = []
        list_possible_moves_king_takes = []
        list_possible_moves_king_takes_higher = []
        list_possible_moves_knight = []
        list_possible_moves_knight_takes = []
        list_possible_moves_knight_takes_higher = []
        number_of_queen_calls = 0
        # flags to see if white or black can promote
        promoting_white = False
        promoting_black = False
        # Iterating through all cells of the chess board
        non_empty_cells = self.cells_having_pieces_white if self.color == 1 else self.cells_having_pieces_black
        non_empty_cells_enemy = self.cells_having_pieces_black if self.color == 1 else self.cells_having_pieces_white

        self.is_in_check = self.if_in_check()
        for tuple in non_empty_cells:
            y_pos_piece, x_pos_piece = tuple
            # Getting the piece and its color of the current cell on which the for-loop is.
            cell = self.current_chess_board[y_pos_piece][x_pos_piece]
            piece = cell[0]
            color = np.sign(cell[1])
            # If we have a king at hand
            if (piece == "K"):
                if self.color == 1:
                    initial_y_x_co = self.white_king_position
                else:
                    initial_y_x_co = self.black_king_position

                initial_y_co = initial_y_x_co[0]
                initial_x_co = initial_y_x_co[1]
                # A king can only describe a 3x3 square around himself
                for a in range(-1, 2):
                    for b in range(-1, 2):

                        # checking if the grid around the king is within boundaries
                        if (0 <= y_pos_piece + a <= 7 and 0 <= x_pos_piece + b <= 7):

                            # Checking if move is legal
                            # king cannot go on square which has the same color as his
                            if (y_pos_piece + a, x_pos_piece + b) in non_empty_cells:
                                continue

                            # Updating the new chess board with the new position of the king on it, to check if it possible, because if this move results in putting the king in check, it can't be done.
                            # saving the taken piece's initial:
                            taken_piece = self.current_chess_board[y_pos_piece + a][x_pos_piece + b][0]
                            # Saving the piece's value
                            taken_piece_points = self.current_chess_board[y_pos_piece + a][x_pos_piece + b][1]

                            # Updating the chessboard
                            self.current_chess_board[y_pos_piece + a][x_pos_piece + b] = ("K", 100 * self.color)
                            self.current_chess_board[initial_y_co][initial_x_co] = ("B", 0)

                            if self.color == 1:

                                self.white_king_position = (y_pos_piece + a, x_pos_piece + b)
                                king_x, king_y = self.white_king_position
                                enemy_king_x, enemy_king_y = self.black_king_position
                            else:

                                self.black_king_position = (y_pos_piece + a, x_pos_piece + b)
                                king_x, king_y = self.black_king_position
                                enemy_king_x, enemy_king_y = self.white_king_position

                            # Checking if king is in check in new position or that the two kings are in each others illegal
                            # proximimty
                            if self.if_in_check() or (abs(king_x - enemy_king_x) <= 1 and abs(king_y - enemy_king_y) <= 1):
                                # If true, than the position should be reset to the initial board before the king move
                                self.current_chess_board[initial_y_co][initial_x_co] = ("K", 100 * self.color)
                                self.current_chess_board[y_pos_piece + a][x_pos_piece + b] = (
                                    taken_piece, taken_piece_points)

                                # setting back the position of the king
                                if self.color == 1:
                                    self.white_king_position = (initial_y_co, initial_x_co)
                                else:
                                    self.black_king_position = (initial_y_co, initial_x_co)
                                continue

                            else:
                                # If true, than the position should be reset to the initial board before the king move
                                self.current_chess_board[initial_y_co][initial_x_co] = ("K", 100 * self.color)
                                self.current_chess_board[y_pos_piece + a][x_pos_piece + b] = (
                                    taken_piece, taken_piece_points)

                                # setting back the position of the king
                                if self.color == 1:
                                    self.white_king_position = (initial_y_co, initial_x_co)
                                else:
                                    self.black_king_position = (initial_y_co, initial_x_co)

                                if (self.current_chess_board[y_pos_piece + a][x_pos_piece + b][1] * color < 0):
                                    notation = "K" + 'x' + str(
                                        chess_board_letters[(y_pos_piece + a, x_pos_piece + b)])

                                    # Appending to list of possible move in the correct list based on the color
                                    # of the king.
                                    list_possible_moves_king_takes.append(
                                        [notation, [y_pos_piece, x_pos_piece, color * 100, "K", (y_pos_piece + a,
                                                                                                 x_pos_piece + b)]])

                                # If king cannot take anything, then we simply have the notation K + coordinate
                                else:
                                    notation = "K" + str(chess_board_letters[(y_pos_piece + a, x_pos_piece + b)])

                                    # Appending to correct list
                                    list_possible_moves_king.append(
                                        [notation, [y_pos_piece, x_pos_piece, color * 100, "K", (y_pos_piece + a,
                                                                                                 x_pos_piece + b)]])




            # Covering case if the piece is a queen
            elif (piece == "Q"):
                list_moves, list_moves_takes = queen([y_pos_piece, x_pos_piece], self.current_chess_board,
                                                     color, self).possible_moves()
                list_possible_moves_queen = list_possible_moves_queen + list_moves
                list_possible_moves_queen_takes = list_possible_moves_queen_takes + list_moves_takes

                # this is important as if there is only one call, then we DON'T need to check for multiplicates for
                # the queen
                number_of_queen_calls += 1

            elif (piece == "L"):
                list_moves, list_moves_takes, list_moves_takes_higher = bishop([y_pos_piece, x_pos_piece], color,
                                                                              self).possible_moves()
                list_possible_moves_bishop = list_possible_moves_bishop + list_moves
                list_possible_moves_bishop_takes = list_possible_moves_bishop_takes + list_moves_takes
                list_possible_moves_bishop_takes_higher = list_possible_moves_bishop_takes_higher + list_moves_takes_higher



            elif (piece == "R"):

                list_moves, list_moves_takes, list_moves_takes_higher = rook([y_pos_piece, x_pos_piece],
                                                                              color, self).possible_moves()
                list_possible_moves_rook = list_possible_moves_rook + list_moves
                list_possible_moves_rook_takes = list_possible_moves_rook_takes + list_moves_takes
                list_possible_moves_rook_takes_higher = list_possible_moves_rook_takes_higher + list_moves_takes_higher


            elif (piece == "P"):
                # absolute value displacement vector of pawn, pawn can only go one square diagonally, or two from begin
                # position
                if color == 1:
                    possible_moves_pawn = [(-1, 0), (-1, -1), (-2, 0), (-1, 1)]
                elif color == -1:
                    possible_moves_pawn = [(1, 0), (1, 1), (2, 0), (1, -1)]

                # Going through all possible moves for the pawn
                for move in possible_moves_pawn:
                    y_pos = move[0]
                    x_pos = move[1]
                    # Checking bounderies
                    if (0 <= y_pos_piece + y_pos <= 7 and 0 <= x_pos_piece + x_pos <= 7):

                        # Checking if move is legal
                        if not (pawn([y_pos_piece, x_pos_piece],
                                     str([y_pos_piece + y_pos, x_pos_piece + x_pos])
                                , color, self).if_illegal_move()):
                            # if there is a piece with opposite color on the cell on which our piece wants to move,
                            # then there must be added an 'x' in the notation f.e. "pawn on d4 takes e5" -> dxe5

                            if self.is_in_check:
                                condition = (self.current_chess_board[y_pos_piece + y_pos][x_pos_piece + x_pos][
                                                 1] * color < 0)
                            else:
                                condition = (y_pos_piece + y_pos, x_pos_piece + x_pos) in non_empty_cells_enemy

                            if condition:
                                notation = str(chess_board_letters[(y_pos_piece, x_pos_piece)][0]) + 'x' + \
                                           str(chess_board_letters[(y_pos_piece + y_pos, x_pos_piece + x_pos)])

                                list_possible_moves_pawn_takes.append(
                                    [notation, [y_pos_piece, x_pos_piece, color, "P",
                                                (y_pos_piece + y_pos, x_pos_piece + x_pos)]])
                                # appending to correct list
                                if (color == 1):
                                    # if the white pawn is on the 8-th rank, than it can promote
                                    if notation[2:] in ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"]:
                                        promoting_white = True

                                elif (color == -1):
                                    # if the black pawn is on the first rank, than it can promote

                                    if notation[2:] in ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"]:
                                        promoting_black = True

                            else:
                                notation = str(chess_board_letters[(y_pos_piece + y_pos, x_pos_piece + x_pos)])

                                list_possible_moves_pawn.append(
                                    [notation, [y_pos_piece, x_pos_piece, color, "P",
                                                (y_pos_piece + y_pos, x_pos_piece + x_pos)]])

                                # appending to correct list
                                if (color == 1):
                                    if notation in ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"]:
                                        promoting_white = True

                                elif (color == -1):
                                    if notation in ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"]:
                                        promoting_black = True


            elif (piece == "N"):
                # writing down the possible moves that a knight can make.
                possible_moves_knight = [(-2, -1), (-1, -2), (1, 2), (2, 1), (-2, 1), (-1, 2), (2, -1), (1, -2)]
                # making grid around the knight and look if move is possible

                for move in possible_moves_knight:
                    y_pos = move[0]
                    x_pos = move[1]
                    if (0 <= y_pos_piece + y_pos <= 7 and 0 <= x_pos_piece + x_pos <= 7):
                        # Checking if move is legal
                        if not knight([y_pos_piece, x_pos_piece],
                                     str([y_pos_piece + y_pos, x_pos_piece + x_pos]),
                                     self.current_chess_board, color).if_illegal_move():

                            # checking if move is NOT setting our king in check
                            if not self.looking_if_check([y_pos_piece, x_pos_piece], str(
                                    [y_pos_piece + y_pos,
                                     x_pos_piece + x_pos])):
                                value_of_cell = self.current_chess_board[y_pos_piece + y_pos][x_pos_piece + x_pos][1]
                                if (value_of_cell * color < 0):
                                    if value_of_cell >= 3:
                                        notation = "N" + 'x' + str(
                                            chess_board_letters[(y_pos_piece + y_pos, x_pos_piece + x_pos)])

                                        list_possible_moves_knight_takes_higher.append(
                                            [notation, [y_pos_piece, x_pos_piece, color * 3, "N",
                                                        (y_pos_piece + y_pos, x_pos_piece + x_pos)]])
                                    else:
                                        notation = "N" + 'x' + str(
                                            chess_board_letters[(y_pos_piece + y_pos, x_pos_piece + x_pos)])

                                        list_possible_moves_knight_takes.append(
                                            [notation, [y_pos_piece, x_pos_piece, color * 3, "N",
                                                        (y_pos_piece + y_pos, x_pos_piece + x_pos)]])

                                else:
                                    notation = "N" + str(
                                        chess_board_letters[(y_pos_piece + y_pos, x_pos_piece + x_pos)])

                                    list_possible_moves_knight.append(
                                        [notation, [y_pos_piece, x_pos_piece, color * 3, "N",
                                                    (y_pos_piece + y_pos, x_pos_piece + x_pos)]])

        # promoting a pawn
        # Checking if white can promote
        if promoting_white:
            # Putting the promotions in the list of possible moves WITHOUT taking the opponent's piece
            indices_promoting_notation = []
            for i in range(0, len(list_possible_moves_pawn)):
                position = list_possible_moves_pawn[i][1]

                # Move written down in chess notation
                move = list_possible_moves_pawn[i][0]

                # if the move is in the following list, then there is the possibility to promote
                if move[-2:] in ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"]:
                    for element in ["R", "N", "B", "Q"]:
                        list_possible_moves_pawn.append([move + '=' + element, position])

                    # deleting the move, because it is bad notation('a8' is not a valid notation
                    # This move has index i because we have inserted 4 extra moves
                    indices_promoting_notation.append(i)

            # the bad notations (like 'a8' or fxg8) must be deleted. Since by each deletion, the indices change too,
            # we must keep track fo the number of deleted elements
            deleted_elements = 0
            for index in indices_promoting_notation:
                list_possible_moves_pawn.pop(index - deleted_elements)
                deleted_elements +=1


            indices_promoting_notation = []
            for i in range(0, len(list_possible_moves_pawn_takes)):
                position = list_possible_moves_pawn_takes[i][1]

                # Move written down in chess notation
                move = list_possible_moves_pawn_takes[i][0]

                # if the move is in the following list, then there is the possibility to promote
                if move[-2:] in ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8"]:
                    for element in ["R", "N", "B", "Q"]:
                        list_possible_moves_pawn_takes.append([move + '=' + element, position])

                    # deleting the move, because it is bad notation('a8' is not a valid notation
                    # This move has index i because we have inserted 4 extra moves
                    indices_promoting_notation.append(i)

            deleted_elements = 0
            for index in indices_promoting_notation:
                list_possible_moves_pawn_takes.pop(index - deleted_elements)
                deleted_elements +=1

        # Checking if black can promote
        if promoting_black:
            indices_promoting_notation = []
            for i in range(0, len(list_possible_moves_pawn)):

                # Saving the data/position, e.g. the next argument of the list_possible_moves_black[i]
                position = list_possible_moves_pawn[i][1]

                # Move written down in chess notation
                move = list_possible_moves_pawn[i][0]

                if move[-2:] in ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"]:
                    for element in ["R", "N", "B", "Q"]:
                        list_possible_moves_pawn.append([move + '=' + element, position])

                    # deleting the move, because it is bad notation('a8' is not a valid notation
                    # This move has index i because we have inserted 4 extra moves
                    indices_promoting_notation.append(i)

            deleted_elements = 0
            for index in indices_promoting_notation:
                list_possible_moves_pawn.pop(index - deleted_elements)
                deleted_elements +=1

            indices_promoting_notation = []
            for i in range(0, len(list_possible_moves_pawn_takes)):

                # Saving the data/position, e.g. the next argument of the list_possible_moves_black[i]
                position = list_possible_moves_pawn_takes[i][1]

                # Move written down in chess notation
                move = list_possible_moves_pawn_takes[i][0]

                if move[-2:] in ["a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"]:
                    for element in ["R", "N", "B", "Q"]:
                        list_possible_moves_pawn_takes.append([move + '=' + element, position])

                    # deleting the move, because it is bad notation('a8' is not a valid notation
                    # This move has index i because we have inserted 4 extra moves
                    indices_promoting_notation.append(i)

            deleted_elements = 0
            for index in indices_promoting_notation:
                list_possible_moves_pawn_takes.pop(index - deleted_elements)
                deleted_elements +=1

        # adding the possible moves, keeping the move ordering(supposedly best move first, then the worst ones)
        list_of_possible_moves = list_possible_moves_pawn_takes + list_possible_moves_knight_takes_higher + list_possible_moves_rook_takes_higher+ \
                                  list_possible_moves_bishop_takes_higher + list_possible_moves_pawn + \
                                 list_possible_moves_knight + list_possible_moves_bishop + list_possible_moves_rook + \
                                 list_possible_moves_queen + list_possible_moves_king + list_possible_moves_queen_takes + \
                                 list_possible_moves_bishop_takes + list_possible_moves_knight_takes + list_possible_moves_rook_takes + list_possible_moves_king_takes

        # Castling short
        if self.white_can_castle_short and self.color == 1:
            if self.castle_short():
                list_of_possible_moves.insert(0, ["O-O", [7, 4, 100, "K", (7, 6)]])

        # castling long
        if self.white_can_castle_long and self.color == 1:
            if self.castle_long():
                list_of_possible_moves.insert(0, ["O-O-O", [7, 4, 100, "K", (7, 2)]])

        # Castling short
        if self.black_can_castle_short and self.color == -1:
            if self.castle_short():
                list_of_possible_moves.insert(0, ["O-O", [0, 4, -100, "K", (0, 6)]])

        # castling long
        if self.black_can_castle_short and self.color == -1:
            if self.castle_long():
                list_of_possible_moves.insert(0, ["O-O-O", [0, 4, -100, "K", (0, 2)]])

        # Making a list of all possible moves containing two lists: one having the possible moves for white, the other
        # for black respectively
        if self.color == 1:
            list_possible_moves_white = list_of_possible_moves
            list_possible_moves_black = []
            self.possible_moves_white = list_possible_moves_white
        else:
            list_possible_moves_white = []
            list_possible_moves_black = list_of_possible_moves
            self.possible_moves_black = list_possible_moves_black

        total_moves = [list_possible_moves_white, list_possible_moves_black]

        return total_moves

    def if_in_check(self):
        """
        Function to check whether some king is in check
        :return: True if king in question is in check, False if not.

        """

        if self.color != 0:
            if self.color == 1:
                king_position_y_co, king_position_x_co = self.white_king_position
                cells_having_pieces_of_enemy = self.cells_having_pieces_black

            else:

                king_position_y_co, king_position_x_co = self.black_king_position
                cells_having_pieces_of_enemy = self.cells_having_pieces_white

            # main tactic: looking at all the lines from where the king could be attacked,
            # We arge going through all possibilities. As all pieces, excluding the knight, can go through pieces,
            # it is sufficient to look UNTIL we find a piece in a certain direction.

            # Going from left to right w.r.t. the king. We are considering 'left' and 'right' from the white player's
            # perspective

            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

            for y_step, x_step in directions:
                for step in range(1, 8):
                    y_pos, x_pos = y_step * step, x_step * step
                    if y_step == 0:
                        total_checks = self.horizontal_check(king_position_y_co, king_position_x_co + x_pos)
                    else:
                        total_checks = self.vertical_checks(king_position_y_co + y_pos, king_position_x_co)

                    if total_checks == 1:
                        return True
                    elif total_checks == -1:
                        break

            diagonal_moves = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

            for y_step, x_step in diagonal_moves:
                y_pos, x_pos = y_step, x_step
                while 0 <= king_position_x_co + x_pos <= 7 and 0 <= king_position_y_co + y_pos <= 7:
                    total_checks = self.diagonal_checks(king_position_y_co + y_pos, king_position_x_co + x_pos,
                                                        king_position_y_co, king_position_x_co)

                    if total_checks == 1:
                        return True
                    elif total_checks == -1:
                        break
                    y_pos += y_step
                    x_pos += x_step

            # We need to consider a knight attacking the king too
            # writing down the possible moves that a knight can make.
            possible_moves_knight = [(-2, -1), (-1, -2), (1, 2), (2, 1), (-2, 1), (-1, 2), (2, -1), (1, -2)]

            for move_y, move_x in possible_moves_knight:
                cell_y_co, cell_x_co = king_position_y_co + move_y, king_position_x_co + move_x

                # only looking at the cell, if this is of the other color
                if not (0 <= cell_y_co <= 7 and 0 <= cell_x_co <= 7):
                    continue
                if (cell_y_co, cell_x_co) in cells_having_pieces_of_enemy or self.is_in_check:
                    piece_on_cell, color_of_piece = self.current_chess_board[cell_y_co][cell_x_co]
                    if piece_on_cell == "N" and color_of_piece * self.color < 0:
                        return True

            return False

    def castle_short(self):
        """
        Function to allow to castle short, writing down the cases according to the color
        :return: True, if we can, False if not
        Note that king can only castle if not in check
        """
        if self.color == 1:
            return (
                    self.current_chess_board[7][4] == ("K", 100) and
                    self.current_chess_board[7][5] == ("B", 0) and
                    self.current_chess_board[7][6] == ("B", 0) and
                    self.current_chess_board[7][7][0] == "R" and not self.is_in_check
            )
        elif self.color == -1:
            return (
                    self.current_chess_board[0][4] == ("K", -100) and
                    self.current_chess_board[0][5] == ("B", 0) and
                    self.current_chess_board[0][6] == ("B", 0) and
                    self.current_chess_board[0][7][0] == "R" and not self.is_in_check
            )
        else:
            return False

    def castle_long(self):
        """
        Function to allow to castle long, writing down the cases according to the color
        :return: True, if we can, False if not
        """
        if self.color == 1:
            return (
                    self.current_chess_board[7][4] == ("K", 100) and
                    self.current_chess_board[7][3] == self.current_chess_board[7][2] == self.current_chess_board[7][
                        1] == ("B", 0) and
                    self.current_chess_board[7][0][0] == "R" and not self.is_in_check
            )
        elif self.color == -1:
            return (
                    self.current_chess_board[0][4] == ("K", -100) and
                    self.current_chess_board[0][3] == self.current_chess_board[0][2] == self.current_chess_board[0][
                        1] == (
                        "B", 0) and
                    self.current_chess_board[0][0][0] == "R" and not self.is_in_check
            )
        else:
            return False

    def unmove(self):
        """
        redo move
        """
        if self.played_cell[0] == "O-O_white":
            self.current_chess_board[7][4] = ("K", 100)
            self.current_chess_board[7][6] = ("B", 0)
            self.current_chess_board[7][7] = ("R", 5)
            self.current_chess_board[7][5] = ("B", 0)
            self.white_king_position = (7, 4)
            self.cells_having_pieces_white -= {(7, 6), (7, 5)}
            self.cells_having_pieces_white.update({(7, 4), (7, 7)})
            return

        elif self.played_cell[0] == "O-O-O_white":
            self.current_chess_board[7][4] = ("K", 100)
            self.current_chess_board[7][2] = ("B", 0)

            self.current_chess_board[7][0] = ("R", 5)
            self.current_chess_board[7][3] = ("B", 0)
            self.white_king_position = (7, 4)

            self.cells_having_pieces_white -= {(7, 2), (7, 3)}
            self.cells_having_pieces_white.update({(7, 4), (7, 0)})
            return

        elif self.played_cell[0] == "en_passant_white":
            self.current_chess_board[self.played_cell_position[0]][self.played_cell_position[1]] = ('P', 1)
            self.current_chess_board[self.taken_cell_position[0]][self.taken_cell_position[1]] = ('P', -1)
            # we also need to remove the white pawn that was placed in front of the black pawn(so one y-co lower)
            self.current_chess_board[self.taken_cell_position[0] - 1][self.taken_cell_position[1]] = ("B", 0)

            self.cells_having_pieces_white.remove((self.taken_cell_position[0] - 1, self.taken_cell_position[1]))
            self.cells_having_pieces_black.update({self.taken_cell_position})
            self.cells_having_pieces_white.update({self.played_cell_position})
            return

        if self.played_cell[0] == "O-O_black":
            self.current_chess_board[0][4] = ("K", -100)
            self.current_chess_board[0][6] = ("B", 0)
            self.current_chess_board[0][7] = ("R", -5)
            self.current_chess_board[0][5] = ("B", 0)
            self.black_king_position = (0, 4)

            self.cells_having_pieces_black -= {(0, 6), (0, 5)}
            self.cells_having_pieces_black.update({(0, 4), (0, 7)})
            return

        elif self.played_cell[0] == "O-O-O_black":
            self.current_chess_board[0][4] = ("K", -100)
            self.current_chess_board[0][2] = ("B", 0)

            self.current_chess_board[0][0] = ("R", -5)
            self.current_chess_board[0][3] = ("B", 0)
            self.black_king_position = (0, 4)

            self.cells_having_pieces_black -= {(0, 2), (0, 3)}
            self.cells_having_pieces_black.update({(0, 4), (0, 0)})
            return

        elif self.played_cell[0] == "en_passant_black":
            self.current_chess_board[self.played_cell_position[0]][self.played_cell_position[1]] = ('P', -1)
            self.current_chess_board[self.taken_cell_position[0]][self.taken_cell_position[1]] = ('P', 1)
            # we also need to remove the white pawn that was placed in front of the black pawn(so one y-co lower)
            self.current_chess_board[self.taken_cell_position[0] + 1][self.taken_cell_position[1]] = ("B", 0)

            self.cells_having_pieces_black.remove((self.taken_cell_position[0] + 1, self.taken_cell_position[1]))
            self.cells_having_pieces_white.update({self.taken_cell_position})
            self.cells_having_pieces_black.update({self.played_cell_position})
            return

        # setting back the position
        if self.played_cell == ("B", -3) or self.played_cell == ("B", 3):
            self.played_cell = ("L", 3) if self.color == 1 else ("L", -3)

        if self.played_cell[1] > 0:
            # removing the squares on which there are pieces, adding the piece in advance
            self.cells_having_pieces_white.update({self.played_cell_position})
            self.cells_having_pieces_white.remove(self.taken_cell_position)
            if not self.taken_cell == ('B', 0):
                self.cells_having_pieces_black.update({self.taken_cell_position})

        elif self.played_cell[1] < 0:
            # removing the squares on which there are pieces, adding the piece in advance
            self.cells_having_pieces_black.update({self.played_cell_position})
            self.cells_having_pieces_black -= {self.taken_cell_position}
            if not self.taken_cell == ('B', 0):
                self.cells_having_pieces_white.update({self.taken_cell_position})

        self.current_chess_board[self.played_cell_position[0]][self.played_cell_position[1]] = self.played_cell
        self.current_chess_board[self.taken_cell_position[0]][self.taken_cell_position[1]] = self.taken_cell

        # if the king is moved, then we need to reset their position too
        if self.played_cell == ("K", 100):
            self.white_king_position = (self.played_cell_position[0], self.played_cell_position[1])
        elif self.played_cell == ("K", -100):
            self.black_king_position = (self.played_cell_position[0], self.played_cell_position[1])

        return

    def apply_move_white(self, move_white_coordinate, previous_move):
        """
        Playing move for white
        """
        # Only the last two symbols are useful for the coordinate transformation
        white_move_y_and_x_co = coordinate_transformation[move_white_coordinate]
        move_white_x_co = white_move_y_and_x_co[1]
        move_white_y_co = white_move_y_and_x_co[0]

        # Saving the previous move: this is needed for undoing the move:
        self.played_cell = (previous_move[3], previous_move[2])
        self.played_cell_position = (previous_move[0], previous_move[1])

        # saving the position of the cell that has been taken, together with the piece taken
        self.taken_cell = self.current_chess_board[move_white_y_co][move_white_x_co]
        self.taken_cell_position = (move_white_y_co, move_white_x_co)

        self.cells_having_pieces_white.remove(self.played_cell_position)
        self.cells_having_pieces_black -= {self.taken_cell_position}
        self.cells_having_pieces_white.update({self.taken_cell_position})

        # Saving moved piece and its value
        moved_piece = previous_move[3]
        value_of_piece = previous_move[2]

        # savings king position if king is played
        if moved_piece == "K":
            self.white_king_position = coordinate_transformation[move_white_coordinate]
            self.white_can_castle_short = False
            self.white_can_castle_long = False

        elif moved_piece == "R" and (self.white_can_castle_long or self.white_can_castle_short):
            # checking if the rook comes from the a-file, if this rook moves, then LONG castling cannot be done
            if previous_move[1] == 0:
                self.white_can_castle_long = False

            # checking if the rook comes from the h-file, if this rook moves, then SHORT castling cannot be done
            elif previous_move[1] == 7:
                self.white_can_castle_short = False

        # saving move to list of played moves
        self.played_moves.append(
            {'played_cell': self.played_cell, 'played_cell_position': self.played_cell_position,
             'taken_cell': self.taken_cell, 'taken_cell_position': self.taken_cell_position,
             'castling': {'white_can_castle_short': self.white_can_castle_short,
                          'white_can_castle_long': self.white_can_castle_long,
                          'black_can_castle_short': self.black_can_castle_short,
                          'black_can_castle_long': self.black_can_castle_long},
             'en_passant': {'en_passant_white': self.en_passant_white,
                            'en_passant_black': self.en_passant_black,
                            'en_passant_move_white': self.en_passant_move_white,
                            'en_passant_move_black': self.en_passant_move_black},
             'cells_having_pieces': {
                 'cells_having_pieces_white': self.cells_having_pieces_white,
                 'cells_having_pieces_black': self.cells_having_pieces_black}
             }
        )

        # Updating chess board
        self.current_chess_board[previous_move[0]][previous_move[1]] = ("B", 0)
        self.current_chess_board[move_white_y_co][move_white_x_co] = (moved_piece, value_of_piece)
        return

    def promotion_white(self, previous_move, promotion_piece, move_white_coordinate):
        """
        Playing promotion move for white
        """
        white_move_y_and_x_co = coordinate_transformation[move_white_coordinate]
        move_white_x_co = white_move_y_and_x_co[1]
        move_white_y_co = white_move_y_and_x_co[0]

        # Saving the previous move: this is needed for undoing the move:
        self.played_cell = (previous_move[3], previous_move[2])
        self.played_cell_position = (previous_move[0], previous_move[1])

        # saving the position of the cell that has been taken, together with the piece taken
        self.taken_cell = self.current_chess_board[move_white_y_co][move_white_x_co]
        self.taken_cell_position = (move_white_y_co, move_white_x_co)

        self.cells_having_pieces_white.remove(self.played_cell_position)
        self.cells_having_pieces_black -= {self.taken_cell_position}
        self.cells_having_pieces_white.update({self.taken_cell_position})

        # saving move to list of played moves
        self.played_moves.append(
            {'played_cell': self.played_cell, 'played_cell_position': self.played_cell_position,
             'taken_cell': self.taken_cell, 'taken_cell_position': self.taken_cell_position,
             'castling': {'white_can_castle_short': self.white_can_castle_short,
                          'white_can_castle_long': self.white_can_castle_long,
                          'black_can_castle_short': self.black_can_castle_short,
                          'black_can_castle_long': self.black_can_castle_long},
             'en_passant': {'en_passant_white': self.en_passant_white,
                            'en_passant_black': self.en_passant_black,
                            'en_passant_move_white': self.en_passant_move_white,
                            'en_passant_move_black': self.en_passant_move_black},
             'cells_having_pieces': {
                 'cells_having_pieces_white': self.cells_having_pieces_white,
                 'cells_having_pieces_black': self.cells_having_pieces_black}
             }
        )

        self.current_chess_board[previous_move[0]][previous_move[1]] = ("B", 0)

        # Promoting accordingly
        points_pieces_white = {"Q": 9, "R": 5, "N": 3}

        if not promotion_piece == "B":
            self.current_chess_board[0][move_white_x_co] = (promotion_piece, points_pieces_white[promotion_piece])
        else:
            self.current_chess_board[0][move_white_x_co] = ("L", 3)
        return

    def apply_move_black(self, move_black_coordinate, previous_move):
        """
        Playing move for black
        """
        black_move_y_and_x_co = coordinate_transformation[move_black_coordinate]
        move_black_x_co = black_move_y_and_x_co[1]
        move_black_y_co = black_move_y_and_x_co[0]

        # Saving the previous move: this is needed for undoing the move:
        self.played_cell = (previous_move[3], previous_move[2])
        self.played_cell_position = (previous_move[0], previous_move[1])

        # saving the position of the cell that has been taken, together with the piece taken
        self.taken_cell = self.current_chess_board[move_black_y_co][move_black_x_co]
        self.taken_cell_position = (move_black_y_co, move_black_x_co)

        self.cells_having_pieces_black.remove(self.played_cell_position)
        self.cells_having_pieces_white -= {self.taken_cell_position}
        self.cells_having_pieces_black.update({self.taken_cell_position})

        # saving move to list of played moves
        self.played_moves.append(
            {'played_cell': self.played_cell, 'played_cell_position': self.played_cell_position,
             'taken_cell': self.taken_cell, 'taken_cell_position': self.taken_cell_position,
             'castling': {'white_can_castle_short': self.white_can_castle_short,
                          'white_can_castle_long': self.white_can_castle_long,
                          'black_can_castle_short': self.black_can_castle_short,
                          'black_can_castle_long': self.black_can_castle_long},
             'en_passant': {'en_passant_white': self.en_passant_white,
                            'en_passant_black': self.en_passant_black,
                            'en_passant_move_white': self.en_passant_move_white,
                            'en_passant_move_black': self.en_passant_move_black},
             'cells_having_pieces': {
                 'cells_having_pieces_white': self.cells_having_pieces_white,
                 'cells_having_pieces_black': self.cells_having_pieces_black}
             }
        )

        # Saving the moved black piece
        moved_piece = previous_move[3]
        value_of_moved_piece = previous_move[2]

        if moved_piece == "K":
            self.black_king_position = coordinate_transformation[move_black_coordinate]
            self.black_can_castle_short = False
            self.black_can_castle_long = False

        elif moved_piece == "R" and (self.black_can_castle_long or self.black_can_castle_short):
            # checking if the rook comes from the a-file, if this rook moves, then LONG castling cannot be done
            if previous_move[1] == 0:
                self.black_can_castle_long = False

            # checking if the rook comes from the h-file, if this rook moves, then SHORT castling cannot be done
            elif previous_move[1] == 7:
                self.black_can_castle_short = False

        self.current_chess_board[previous_move[0]][previous_move[1]] = ("B", 0)
        self.current_chess_board[move_black_y_co][move_black_x_co] = (moved_piece, value_of_moved_piece)
        return

    def promotion_black(self, previous_move, promotion_piece, black_move_coordinate):
        """
        Playing promotion move for black
        """
        black_move_y_and_x_co = coordinate_transformation[black_move_coordinate]
        black_move_y_co = black_move_y_and_x_co[0]
        black_move_x_co = black_move_y_and_x_co[1]
        # Saving the previous move: this is needed for undoing the move:
        self.played_cell = (previous_move[3], previous_move[2])
        self.played_cell_position = (previous_move[0], previous_move[1])

        # saving the position of the cell that has been taken, together with the piece taken
        self.taken_cell = self.current_chess_board[7][black_move_x_co]
        self.taken_cell_position = (7, black_move_x_co)

        self.cells_having_pieces_black.remove(self.played_cell_position)
        self.cells_having_pieces_white -= {self.taken_cell_position}
        self.cells_having_pieces_black.update({self.taken_cell_position})

        # saving move to list of played moves

        self.played_moves.append(
            {'played_cell': self.played_cell, 'played_cell_position': self.played_cell_position,
             'taken_cell': self.taken_cell, 'taken_cell_position': self.taken_cell_position,
             'castling': {'white_can_castle_short': self.white_can_castle_short,
                          'white_can_castle_long': self.white_can_castle_long,
                          'black_can_castle_short': self.black_can_castle_short,
                          'black_can_castle_long': self.black_can_castle_long},
             'en_passant': {'en_passant_white': self.en_passant_white,
                            'en_passant_black': self.en_passant_black,
                            'en_passant_move_white': self.en_passant_move_white,
                            'en_passant_move_black': self.en_passant_move_black},
             'cells_having_pieces': {
                 'cells_having_pieces_white': self.cells_having_pieces_white,
                 'cells_having_pieces_black': self.cells_having_pieces_black}
             }
        )

        self.current_chess_board[previous_move[0]][previous_move[1]] = ("B", 0)

        # Promoting accordingly
        points_pieces_black = {"Q": -9, "R": -5, "N": -3}

        if not promotion_piece == "B":
            self.current_chess_board[7][black_move_x_co] = (promotion_piece, points_pieces_black[promotion_piece])
        else:
            self.current_chess_board[7][black_move_x_co] = ("L", -3)

        return


class rook:
    """
    Introducing the rook
    """

    def __init__(self, initial_position, color, chessboard):
        self.initial_position = initial_position
        self.color = color
        self.current_chess_board = chessboard.current_chess_board

        self.chessboard = chessboard

    def if_illegal_move(self, new_position):
        """
        :param new_position: new position of the rook
        :return: 1 if move is illegal, but there is no need to further search in the direction,
        0 if move is legal,
        -1 if the move is illegal, but there is need to go further as the piece that checks the king could
        still be on the direction
        """
        if (len(new_position) > 6):
            return True
        new_y_co = int(new_position[1])
        new_x_co = int(new_position[4])

        # Cell on which the rook wants to land on
        cell = self.current_chess_board[new_y_co][new_x_co]

        value_of_cell = cell[1]
        sign_of_cell = np.sign(value_of_cell)
        # pieces_inbetween must be equal to 0, otherwise it would imply that the rook would jump over pieces. The rook
        # can also not take his own piece.
        pieces_inbetween = self.chessboard.horizontal_and_vertical_moves(self.initial_position, new_position)
        if (pieces_inbetween) >= 1 or (sign_of_cell == (self.color)):
            return 1

        # checking that the new move doesn't result in setting his own king in check
        elif self.chessboard.looking_if_check(self.initial_position, new_position):
            if sign_of_cell == 0:
                return -1
            else:
                return 1

        else:
            return 0

    def possible_moves(self):
        """
        Giving possible moves of the rook
        """
        list_of_possible_moves = []
        list_of_possible_moves_takes = []
        list_of_possible_moves_takes_higher = []
        y_pos_piece, x_pos_piece = self.initial_position

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

        for dy, dx in directions:
            for step in range(1, 8):
                new_y = y_pos_piece + dy * step
                new_x = x_pos_piece + dx * step

                if not (0 <= new_y < 8 and 0 <= new_x < 8):
                    break

                response = self.if_illegal_move(str([new_y, new_x]))

                if response == 1:
                    break
                elif response == -1:
                    continue

                cell = self.current_chess_board[new_y][new_x]
                value_of_cell = cell[1]
                coordinate = chess_board_letters[(new_y, new_x)]

                if value_of_cell * self.color < 0:
                    if value_of_cell >= 5:
                        notation = "R" + 'x' + str(coordinate)
                        list_of_possible_moves_takes_higher.append(
                            [notation, [y_pos_piece, x_pos_piece, 5 * self.color, "R",
                                        (new_y, new_x)]])
                    else:
                        notation = "R" + 'x' + str(coordinate)
                        list_of_possible_moves_takes.append([notation, [y_pos_piece, x_pos_piece, 5 * self.color, "R",
                                                                        (new_y, new_x)]])
                else:
                    notation = "R" + str(coordinate)

                    list_of_possible_moves.append([notation, [y_pos_piece, x_pos_piece, 5 * self.color, "R",
                                                              (new_y, new_x)]])

        return list_of_possible_moves, list_of_possible_moves_takes, list_of_possible_moves_takes_higher


class pawn:
    def __init__(self, initial_position, new_position, color, chessboard):
        self.initial_position = initial_position
        self.new_position = new_position
        self.color = color
        self.current_chess_board = chessboard.current_chess_board

        self.chessboard = chessboard

    def if_illegal_move(self):
        # defining the coordinates of the new and previous positions
        initial_y_co = int(self.initial_position[0])
        initial_x_co = int(self.initial_position[1])
        new_y_co = int(self.new_position[1])
        new_x_co = int(self.new_position[4])

        # going through all different cases

        # If the pawn is going diagonally
        if initial_x_co != new_x_co:
            if self.color * self.current_chess_board[new_y_co][new_x_co][1] >= 0:
                return True
            elif self.chessboard.looking_if_check(self.initial_position, self.new_position):
                return True
            else:
                return False

        else:
            # pawn can only make 2 steps from the begin position(this is the second row(index:1) for black and the second to last
            # for white(index:6))
            if new_y_co - initial_y_co == 2 and not initial_y_co == 1:
                return True

            elif initial_y_co - new_y_co == 2 and not initial_y_co == 6:
                return True

            # pawn cannot jump in the begin position over other chess pieces.
            elif (initial_y_co == 1 and new_y_co == 3 and
                  self.current_chess_board[2][new_x_co][1] != 0):
                return True

            elif (initial_y_co == 6 and new_y_co == 4 and new_x_co == initial_x_co and
                  self.current_chess_board[5][new_x_co][1] != 0):
                return True

            elif (self.current_chess_board[new_y_co][new_x_co][
                      1] != 0):  # pawn can't go through other pieces. It can go deviate only if there is a piece to capture.
                return True

            # checking if this new position results in a check of the king
            elif self.chessboard.looking_if_check(self.initial_position, self.new_position):
                return True
            else:
                return False


class bishop:
    def __init__(self, initial_position, color, chessboard):
        self.initial_position = initial_position
        self.color = color
        self.current_chess_board = chessboard.current_chess_board
        self.chessboard = chessboard

    def if_illegal_move(self, new_position):
        """

        :param new_position: new position of the piece
        :return: 1 if move is illegal, but there is no need to further search in the direction,
                0 if move is legal,
                -1 if the move is illegal, but there is need to go further as the piece that checks the king could
                still be on the direction
        """

        # defining the coordinates of the new and previous positions
        initial_y_co = int(self.initial_position[0])
        initial_x_co = int(self.initial_position[1])
        new_y_co = int(new_position[1])
        new_x_co = int(new_position[4])

        if (initial_x_co < new_x_co and new_y_co < initial_y_co) or (
                new_x_co < initial_x_co and initial_y_co < new_y_co):  # the bishop is going to the right side
            pieces_inbetween = self.chessboard.diagonal_moves(self.initial_position, new_position, -1)

        else:  # the bishop is going to the left side
            pieces_inbetween = self.chessboard.diagonal_moves(self.initial_position, new_position, 1)

        # value_of_cell on new coordinate
        sign_of_cell = np.sign(self.current_chess_board[new_y_co][new_x_co][1])

        # if there are pieces between the begin and endpoint, then the move is illegal
        if pieces_inbetween >= 1 or (sign_of_cell == self.color):
            return 1

        # We check if the king is in check after this move, if it is then there is to consider two things:
        # -if the new position takes a piece of a different color and still results in check, then further investigations
        # in this direction will result in checks

        # - if the new position is on an empty square, then there still could be an enemy piece on the same directions
        # which places the king in check
        elif self.chessboard.looking_if_check(self.initial_position, new_position):
            if sign_of_cell == 0:
                return -1
            else:
                return 1

        else:
            return 0

    def possible_moves(self):
        """
        Giving possible moves for the bishop
        """
        list_of_possible_moves = []
        list_of_possible_moves_takes = []
        list_of_possible_moves_takes_higher = []
        y_pos_piece, x_pos_piece = self.initial_position
        diagonal_directions = [(-1, -1), (-1, 1), (1, 1), (1, -1)]

        for dy, dx in diagonal_directions:
            new_y, new_x = y_pos_piece + dy, x_pos_piece + dx

            while 0 <= new_y < 8 and 0 <= new_x < 8:
                response = self.if_illegal_move(str([new_y, new_x]))

                if response == 1:
                    break
                elif response == -1:
                    new_y += dy
                    new_x += dx
                    continue

                cell = self.current_chess_board[new_y][new_x]
                value_of_cell = cell[1]
                coordinate = chess_board_letters[(new_y, new_x)]

                if value_of_cell * self.color < 0:
                    if abs(value_of_cell) >= 3:
                        notation = "Bx" + str(coordinate)
                        list_of_possible_moves_takes_higher.append(
                            [notation, [y_pos_piece, x_pos_piece, 3 * self.color, "L",
                                        (new_y, new_x)]])
                    else:
                        notation = "Bx" + str(coordinate)
                        list_of_possible_moves_takes.append([notation, [y_pos_piece, x_pos_piece, 3 * self.color, "L",
                                                                        (new_y, new_x)]])
                else:
                    notation = "B" + str(coordinate)

                    list_of_possible_moves.append([notation, [y_pos_piece, x_pos_piece, 3 * self.color, "L",
                                                              (new_y, new_x)]])

                new_y += dy
                new_x += dx

        return list_of_possible_moves, list_of_possible_moves_takes, list_of_possible_moves_takes_higher


class queen:
    """
    Defining the queen
    """

    def __init__(self, initial_position, current_chess_board, color, chessboard):
        """
        :param initial_position: this is the position of the queen BEFORE the move(datatype: 'list')
        :param new_position: this is the position of the queen AFTER the move(datatype: 'str')
        :param current_chess_board: current chess board, BEFORE the move
        """
        self.initial_position = initial_position
        self.chessboard = chessboard
        # color of the queen
        self.color = color
        self.current_chess_board = current_chess_board

        self.white_king_position = white_king_position
        self.black_king_position = black_king_position

    def if_illegal_move(self, new_position):
        """
        :return: 1 if move is illegal, but there is no need to further search in the direction,
                0 if move is legal,
                -1 if the move is illegal, but there is need to go further as the piece that checks the king could
                still be on the direction
        """

        initial_y_co = int(self.initial_position[0])
        initial_x_co = int(self.initial_position[1])
        new_y_co = int(new_position[1])
        new_x_co = int(new_position[4])

        # A queen cannot jump over pieces, thus we need to need a counter that increases everytime there is a piece
        # between begin and end position
        pieces_inbetween = 0

        # Queen is going along a diagonal from the left bottom to the right top, from white's perspective
        if ((initial_x_co < new_x_co and new_y_co < initial_y_co) or (
                new_x_co < initial_x_co and initial_y_co < new_y_co)):
            # Checking if piece inbetween on diagonal
            pieces_inbetween = self.chessboard.diagonal_moves(self.initial_position, new_position, -1)
        # Queen is going along a diagonal from the right bottom to the left top, from the side of white
        elif ((new_x_co < initial_x_co and new_y_co < initial_y_co) or (
                initial_y_co < new_y_co and initial_x_co < new_x_co)):
            # Checking if piece inbetween on diagonal
            pieces_inbetween = self.chessboard.diagonal_moves(self.initial_position, new_position, 1)


        ##the horizontal/vertical movements:
        elif (initial_y_co == new_y_co or initial_x_co == new_x_co):
            pieces_inbetween = self.chessboard.horizontal_and_vertical_moves(self.initial_position, new_position)

        sign_of_cell = np.sign(self.current_chess_board[new_y_co][new_x_co][1])
        # If there is at least one piece between the begin and endpoint, then the move is illegal
        if (pieces_inbetween >= 1 or (sign_of_cell == (self.color))):
            return 1
        # Checking if move results in the king being in check(-> illegal move)
        elif (self.chessboard.looking_if_check(self.initial_position, new_position)):
            if sign_of_cell == 0:
                return -1
            else:
                return 1

        # If all the statements above mentioned are false, the move is legal
        else:
            return 0

    def possible_moves(self):
        """
        possible moves of queen
        For move ordering, we've made also use of list_of_possible_moves_takes and list_of_possible_moves
        """
        list_of_possible_moves_takes = []
        list_of_possible_moves = []
        y_pos_piece, x_pos_piece = self.initial_position

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

        for dy, dx in directions:
            for step in range(1, 8):
                new_y = y_pos_piece + dy * step
                new_x = x_pos_piece + dx * step

                if not (0 <= new_y < 8 and 0 <= new_x < 8):
                    break

                response = self.if_illegal_move(str([new_y, new_x]))

                if response == 1:
                    break
                elif response == -1:
                    continue

                cell = self.current_chess_board[new_y][new_x]
                value_of_cell = cell[1]
                coordinate = chess_board_letters[(new_y, new_x)]

                if value_of_cell * self.color < 0:
                    notation = "Qx" + str(coordinate)
                    list_of_possible_moves_takes.append([notation, [y_pos_piece, x_pos_piece, 9 * self.color, "Q",
                                                                    (new_y, new_x)]])
                else:
                    notation = "Q" + str(coordinate)
                    list_of_possible_moves.append([notation, [y_pos_piece, x_pos_piece, 9 * self.color, "Q",
                                                              (new_y, new_x)]])

        diagonal_directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dy, dx in diagonal_directions:
            for step in range(1, 8):
                new_y, new_x = y_pos_piece + dy * step, x_pos_piece + dx * step

                if not (0 <= new_y < 8 and 0 <= new_x < 8):
                    break

                response = self.if_illegal_move(str([new_y, new_x]))

                if response == 1:
                    break
                elif response == -1:
                    continue
                elif response == 0:
                    cell = self.current_chess_board[new_y][new_x]
                    value_of_cell = cell[1]
                    coordinate = chess_board_letters[(new_y, new_x)]

                    if value_of_cell * self.color < 0:
                        notation = "Qx" + str(coordinate)
                        list_of_possible_moves_takes.append([notation, [y_pos_piece, x_pos_piece, 9 * self.color, "Q",
                                                                        (new_y, new_x)]])
                    else:
                        notation = "Q" + str(coordinate)

                        list_of_possible_moves.append([notation, [y_pos_piece, x_pos_piece, 9 * self.color, "Q",
                                                                  (new_y, new_x)]])

        return list_of_possible_moves, list_of_possible_moves_takes
