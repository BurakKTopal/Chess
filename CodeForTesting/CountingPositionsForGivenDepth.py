from MovesGenerators.WhitesMove import *
from MovesGenerators.BlacksMove import *
import time

start_time = time.time()
# begin_position = [[['R', -5], ['N', -3], ['L', -3], ['Q', -9], ['K', -100], ['L', -3], ['N', -3], ['R', -5]],
#                [['P', -1], ['P', -1], ['P', -1], ['P', -1], ['P', -1], ['P', -1], ['P', -1], ['P', -1]],
#                [['B', 0], ['B', 0], ['B', 0], ['B', 0], ['B', 0], ['B', 0], ['B', 0], ['B', 0]],
#                [['B', 0], ['B', 0], ['B', 0], ['B', 0], ['B', 0], ['B', 0], ['B', 0], ['B', 0]],
#                [['B', 0], ['B', 0], ['B', 0], ['B', 0], ['B', 0], ['B', 0], ['B', 0], ['B', 0]],
#                [['B', 0], ['B', 0], ['B', 0], ['B', 0], ['B', 0], ['B', 0], ['B', 0], ['B', 0]],
#                [['P', 1], ['P', 1], ['P', 1], ['P', 1], ['P', 1], ['P', 1], ['P', 1], ['P', 1]],
#                [['R', 5], ['N', 3], ['L', 3], ['Q', 9], ['K', 100], ['L', 3], ['N', 3], ['R', 5]]]

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
# Test passed for depth 3: 8902
#test passed too(in video https://www.youtube.com/watch?v=U4ogK0MIzqk 10:12): 1486
# test passed too for depth 4: 197 281 positions looked up in 1399.98 seconds(appr 23 minutes). This is the same as:
# given in https://en.wikipedia.org/wiki/Shannon_number


# update on efficiency:
#197 316 moves on depth 4, now in 761 seconds(13 minutes), so we got 10 minutes saved


# On the interesting position: 1486 position in 2.1 seconds
# on depth 3: 61575, 86 seconds
# the standard chess position(begin position) on depth 4 gives 194 911 positions in 239.73 seconds!!



#after the addition of the castling(not being able to do after once done)
# we get 61 758 in depth 3 for the special position in 93,6 seconds.

# 62 515 in 108 seconds with the 'unmove()'

# 62 910 in 91,7 seconds with cleaning

# 63694 in 190 with dict sadly enough


# 194793 positions(depth 4) in 189.68916296958923 seconds!


# 197 702 positions(depth 4) in 129.37 seconds

# depth 3 (8902 positions) in 4.22 seconds!

print(move_generator(chessboard, 3))
#cProfile.run("move_generator(chessboard,3)")
end_time = time.time()
elapsed_time = print('elapsed time is: ', end_time - start_time)

