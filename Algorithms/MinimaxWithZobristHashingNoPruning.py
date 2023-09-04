from Evaluation.EvaluationFunction import *
from Evaluation.ZobristHashing import *
from MovesGenerators.WhitesMove import *
from MovesGenerators.BlacksMove import *

def minimax_with_zobrist_hashing_no_pruning(chessboard, depth, maximizingPlayer):
    # Calculate the Zobrist hash:
    zhash = zobrist_hash(chessboard)

    # Search hash in transposition table of the chessboard
    if zhash in chessboard.transposition_table:
        chessboard.counting += 1
        eval, best_move = chessboard.transposition_table[zhash]

        return eval, best_move

    if chessboard.mate:
        return -4000 * chessboard.color, None
    if chessboard.stalemate:
        return 2000 * chessboard.color, None
    if depth == 0:
        return eval_board(chessboard), None

    best_move = None
    if maximizingPlayer:
        max_eval = -float('inf')
        chessboard.color = 1
        moves = chessboard.possible_moves_white
        for move in moves:
            chessboard.color = 1

            # Make the move
            white_turn(move[0], chessboard)

            # Recursive minimax call
            eval_score, _ = minimax_with_zobrist_hashing_no_pruning(chessboard, depth - 1, False)

            # Undo the move
            black_turn("undo", chessboard)

            if eval_score > max_eval:
                max_eval = eval_score
                best_move = move[0]

        chessboard.transposition_table[zhash] = (max_eval, best_move)
        return max_eval, best_move

    else:
        min_eval = float('inf')
        chessboard.color = -1
        moves = chessboard.possible_moves_black
        for move in moves:
            chessboard.color = -1
            # Make the move
            black_turn(move[0], chessboard)

            # Recursive minimax call
            eval_score, _ = minimax_with_zobrist_hashing_no_pruning(chessboard, depth - 1, True)

            # Undo the move
            white_turn("undo", chessboard)

            if eval_score < min_eval:
                min_eval = eval_score
                best_move = move[0]

        chessboard.transposition_table[zhash] = (min_eval, best_move)
        return min_eval, best_move