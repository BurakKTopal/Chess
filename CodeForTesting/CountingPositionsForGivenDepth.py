from MovesGenerators.WhitesMove import *
from MovesGenerators.BlacksMove import *
import time

start_time = time.time()
begin_position = [
    [('R', -5), ('N', -3), ('L', -3), ('Q', -9), ('K', -100), ('L', -3), ('N', -3), ('R', -5)],
    [('P', -1), ('P', -1), ('P', -1), ('P', -1), ('P', -1), ('P', -1), ('P', -1), ('P', -1)],
    [('B', 0), ('B', 0), ('B', 0), ('B', 0), ('B', 0), ('B', 0), ('B', 0), ('B', 0)],
    [('B', 0), ('B', 0), ('B', 0), ('B', 0), ('B', 0), ('B', 0), ('B', 0), ('B', 0)],
    [('B', 0), ('B', 0), ('B', 0), ('B', 0), ('B', 0), ('B', 0), ('B', 0), ('B', 0)],
    [('B', 0), ('B', 0), ('B', 0), ('B', 0), ('B', 0), ('B', 0), ('B', 0), ('B', 0)],
    [('P', 1), ('P', 1), ('P', 1), ('P', 1), ('P', 1), ('P', 1), ('P', 1), ('P', 1)],
    [('R', 5), ('N', 3), ('L', 3), ('Q', 9), ('K', 100), ('L', 3), ('N', 3), ('R', 5)]
]

counts = 0

#defining the chessboard, and white begins, so the color of the kings player is white
chessboard = board(begin_position, 1, black_can_castle_short=False, black_can_castle_long=False)
chessboard.possible_moves()

def move_generator(chessboard, depth):
    counts = 0
    if depth == 0:
        return 1
    if depth%2 ==1:
        chessboard.color = 1
        moves = chessboard.possible_moves_white
    else:
        chessboard.color = -1
        moves = chessboard.possible_moves_black

    for move in moves:

        if depth%2 ==1:
            chessboard.color = 1
            white_turn(move[0], chessboard)
            counts += move_generator(chessboard, depth - 1)
            black_turn("undo", chessboard)
        else:
            chessboard.color = -1
            black_turn(move[0], chessboard)
            counts += move_generator(chessboard, depth - 1)
            white_turn("undo", chessboard)




    return counts
print(move_generator(chessboard, 3))
#cProfile.run("move_generator(chessboard,3)")
end_time = time.time()
elapsed_time = print('elapsed time is: ', end_time - start_time)

